node {   
      checkout scm
      
      stage ('Change Output Directory') {
            dir("C:\\Users\\z0048yrk\\Desktop\\LTA") {
                 println("Directory changed")
            }
      }
      
      stage ('Build Docker Image') {
            def image = docker.build("docker-csv", '.')   
      }
      
      stage ('Run Docker Container') {
            bat 'docker run docker-csv > output.csv'    
      }
}
