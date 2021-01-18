node {

      checkout scm

      stage ('Build Docker Image') {
            def image = docker.build("docker-csv", '.')   
      }
      
      stage ('Change Directory for output') {
            ws('/Users/z0048yrk/Desktop/DOCKER/demo')
      }
      
      stage ('Run Docker Container') {
            bat 'docker run docker-csv > output.csv'    
      }
}
