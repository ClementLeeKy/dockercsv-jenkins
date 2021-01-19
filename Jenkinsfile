node {   
      checkout scm
      
      stage ('Create Docker Registry') {
            bat 'docker run -d -p 5000:5000 --restart=always --name registry registry:2'
      }
      
      stage ('Build Docker Image') {
            def image = docker.build("docker-csv", '.')   
      }
      
      stage ('Push Docker Image') { 
            bat 'docker push localhost:5000/docker-csv'
      }
      
      //stage ('Run Docker Container') {
      //      dir("C:\\Users\\z0048yrk\\Desktop\\LTA\\demo") {
      //            bat 'docker run docker-csv > output.csv'
      //      }
      //}
}
