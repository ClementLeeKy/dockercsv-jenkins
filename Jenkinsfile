node {

      checkout scm

      stage ('Build & Run Docker Image') {
            def image = docker.build("docker-csv", '.')
            bat 'docker run --name csv-container image > output.csv' && echo "Container is running and produces a csv output"   
      }
}
