pipeline {
    agent any

    triggers {
        pollSCM '*/1 * * * *'
    }

    stages {
        stage('Build') {
            steps {
                echo "Building.."                    
                sh '''
                python3 building.py
                '''
            }
        }
        stage('Testing') {
            steps {
                echo "Testing.."                    
                sh '''
                pipx install numpy
                python3 test_phase.py
                '''
            }
        }
        stage('Approve') {
            steps {
                input 'Do you want to deploy to production?'
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
                timeout(time: 2, unit: 'MINUTES') {
                     sh '''
                     echo "doing delivery stuff.."
                     '''
                }
            }
        }
    }
    post{
        failure{
            echo "Build failed"
            mail to: 'ujjwalardu@mail.com',
            subject: "Build failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
            body: "The build failed"
        }
    }
}
