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
        stage('Startup') {
            steps {
                script {
                    dir("frontend") {
                        sh 'yarn install'
                    }
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    dir("frontend") {
                        sh 'yarn test'
                    }
                }
            }
            post {
                always {
                    step([$class: 'CoberturaPublisher', coberturaReportFile: 'output/coverage/jest/cobertura-coverage.xml'])
                }
            }
        }
        stage('Build') {
            steps {
                script {
                    dir("frontend") {
                        sh 'yarn start'
                        sh 'yarn build'
                    }
                }
            }
        }     
    }
    // post 
    // {
    //     always {
    //         emailext body: 'Build Jenkins Game Bar', 
    //         recipientProviders: [
    //             [$class: 'DevelopersRecipientProvider'], 
    //             [$class: 'RequesterRecipientProvider']],
    //             to:'gameBarApp@gmail.com',
    //             subject: 'Build Jenkins GameBar'
    //     }
    // }
}
