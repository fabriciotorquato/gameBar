pipeline {
    agent {
        docker {
            image 'node:8-alpine'
            args '-p 3000:3000'
        }
    }
    environment {
        CI = 'true'
    }
    stages {
        stage('Build') {
            steps {
                dir("frontend") {
                    sh 'yarn install'
                }
            }
        }
        stage('Test') { 
            steps {
                  dir("frontend") {
                      sh './jenkins/scripts/test.sh' 
                }
            }
        }        
    }
    post {
    always {
        emailext body: 'Build Jenkins Game Bar. - Luiz Roberto Silva 152563, Fabricio Torquato-153124, Marco Paiva-152945', 
        recipientProviders: [
            [$class: 'DevelopersRecipientProvider'], 
            [$class: 'RequesterRecipientProvider']],
            to:'andreia.leles@facens.br',
             subject: 'Build Jenkins GameBar'
    }
}
}
