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
        // stage('Test') { 
        //     steps {
        //           dir("frontend") {
        //               sh './jenkins/scripts/test.sh' 
        //         }
        //     }
        // }        
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
