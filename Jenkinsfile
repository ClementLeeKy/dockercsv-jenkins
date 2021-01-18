node {

      checkout scm

      stage ('Build & Run Docker Image') {
            def image = docker.build("docker-csv", '.')
            def container = image.run('--name ' + "dockercsv-container" + " > output.csv")
            println('Container outputs csv file!')
      }
}
