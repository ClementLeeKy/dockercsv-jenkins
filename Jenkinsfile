node {

      checkout scm

      stage ('Build & Run Docker Image') {
            def image = docker.build("docker-csv", '.')
            def container = image.run('--name ' + "dockercsv-container")
            println('Container is running!')
            println('Container outputs csv file!')
}
}
