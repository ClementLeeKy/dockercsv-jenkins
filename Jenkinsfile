node {   
      checkout scm
      
      stage ('Build Docker Image') {
            def image = docker.build("docker-csv", '.')   
      }
      
      stage ('Run Docker Container') {
            dir("C:\\Users\\z0048yrk\\Desktop\\LTA\\demo") {
                  bat 'docker run docker-csv > output.csv'
            }
      }
}
