node {

      checkout scm

      stage ('Build Docker Image') {
            def image = docker.build("docker-csv", '.')   
      }
      
      stage ('Run Docker Container') {
            bat 'docker run -d docker-csv > output.csv'    
      }
}
