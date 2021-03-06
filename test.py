import pandas as pd
import numpy as np
import os 
from scipy.stats import uniform, exponweib
from scipy.special import gamma
from scipy.optimize import curve_fit

N_SUBSYS = 30
STEPS = 100
LIMIT = 101*STEPS
times = np.arange(0, LIMIT, STEPS)

#if not os.path.exists('./output'):
 #   os.mkdir('./output')

  #  print("Directory")

class WeibullFailure():
    def __init__(self):
        N_TRAINS = 92
        LOWER_BETA = 0.9
        RANGE_BETA = 0.3
        LOWER_LOGSCALE = 4
        RANGE_LOGSCALE = 1.5
        LOWER_SIZE = 4
        RANGE_SIZE = 8
        gensize = N_TRAINS * int(uniform.rvs(LOWER_SIZE, RANGE_SIZE))
        genbeta = uniform.rvs(LOWER_BETA, RANGE_BETA)
        genscale = np.power(10, uniform.rvs(LOWER_LOGSCALE, RANGE_LOGSCALE))
        self.beta = genbeta
        self.eta = genscale
        self.size = gensize

    def generate_failures(self):
        return exponweib.rvs(
                a=1, loc=0, c=self.beta, scale=self.eta, size=self.size
                )

        def __repr__(self):
            string = f"Subsystem ~ ({self.size} Instances)"
        string += f" Weibull({self.eta:.2f}, {self.beta:.4f})"
        return string


def get_cumulative_failures(failure_times, times):
    cumulative_failures = {
            i: np.histogram(ft, times)[0].cumsum()
            for i, ft in failure_times.items()
            }
    cumulative_failures = pd.DataFrame(cumulative_failures, index=times[1:])
    return cumulative_failures


def fit_failures(cumulative_failures, subsystems):
    fitted = {}
    for i, x in cumulative_failures.items():
        size = subsystems[i].size
        popt, _ = curve_fit(
                lambda x, a, b: np.exp(a)*np.power(x, b), x.index, x.values
                )
        fitted[i] = (np.exp(-popt[0]/popt[1])*size, popt[1])
    return fitted


def kl_divergence(p1, p2):
    em_constant = 0.57721  # Euler-Mascheroni constant
    eta1, beta1 = p1
    eta2, beta2 = p2
    e11 = np.log(beta1/np.power(eta1, beta1))
    e12 = np.log(beta2/np.power(eta2, beta2))
    e2 = (beta1 - beta2)*(np.log(eta1) - em_constant/beta1)
    e3 = np.power(eta1/eta2, beta2)*gamma(beta2/beta1 + 1) - 1
    divergence = e11 - e12 + e2 + e3
    return divergence


subsystems = {i: WeibullFailure() for i in range(N_SUBSYS)}
failure_times = {i: s.generate_failures() for i, s in subsystems.items()}

cumulative_failures = get_cumulative_failures(failure_times, times)
fitted = fit_failures(cumulative_failures, subsystems)
divergences = {
        i: kl_divergence(f, [subsystems[i].eta, subsystems[i].beta])
        for i, f in fitted.items()
        }

expected_failures = {i: np.power(times[1:]/s.eta, s.beta)*s.size
        for i, s in subsystems.items()}
expected_failures = pd.DataFrame(expected_failures, index=times[1:])

modeled_failures = {i: np.power(times[1:]/f[0], f[1])*subsystems[i].size
        for i, f in fitted.items()}
modeled_failures = pd.DataFrame(modeled_failures, index=times[1:])

cols = ['eta', 'fit_eta', 'beta', 'fit_beta', 'kl_divergence', 'n_instance']
out = pd.concat([
    pd.DataFrame({i: [s.size, s.eta, s.beta] for i, s in subsystems.items()},
        index=['n_instance', 'eta', 'beta']).T,
    pd.DataFrame(fitted, index=['fit_eta', 'fit_beta']).T,
    pd.Series(divergences, name='kl_divergence')
    ], axis=1)[cols]
# out.to_csv('./output/sample_output.csv')

from io import StringIO
output = StringIO()
out.to_csv(output)
print(output.getvalue())


