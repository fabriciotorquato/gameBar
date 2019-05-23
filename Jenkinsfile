pipeline {
    agent {
        docker {
            image 'node:6-alpine'
            args '-p 3000:3000'
        }
    }
    environment {
        CI = 'true'
    }
    stages {
        stage('Build') {
            steps {
                cd frontend
                yarn install
            }
        }
        stage('Test') {
            steps {
                cd frontend
                ./jenkins/scripts/test.sh
            }
        }
        stage('Deliver') {
            steps {
                cd frontend
                ./jenkins/scripts/deliver.sh
                input message: 'Finished using the web site? (Click "Proceed" to continue)'
                ./jenkins/scripts/kill.sh
            }
        }
    }
}