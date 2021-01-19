node('/Users/z0048yrk/Desktop/LTA/demo') {   
      checkout scm
      
      stage ('Build Docker Image') {
            def image = docker.build("docker-csv", '.')   
      }
      
      stage ('Run Docker Container') {
            bat 'docker run docker-csv > output.csv'    
      }
}
