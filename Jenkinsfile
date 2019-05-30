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
        stage('Build') {
            steps {
                script {
                    dir("frontend") {
                        sh './jenkins/scripts/deliver.sh' 
                        input message: 'Finished using the web site? (Click "Proceed" to continue)' 
                        sh './jenkins/scripts/kill.sh' 
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
                    junit 'output/coverage/junit/junit.xml'
                }
            }
        }
        stage('Deliver') {
            steps {
                script {
                    dir("frontend") {
                        input message: 'Finished using the web site? (Click "Proceed" to continue)' 
                        sh './jenkins/scripts/kill.sh' 
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
