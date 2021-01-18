node {

      checkout scm  
      
      stage ('Build Docker Image') {
            def image = docker.build("docker-csv", '.')   
      }
      
      stage ('Run Docker Container') {
            customWorkspace "c:\\Users\z0048yrk\Desktop"
            bat 'docker run -d docker-csv > output.csv'    
      }
}
