pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/unaidabdullah-ui/GAME.git'
            }
        }

        stage('Build') {
            steps {
                // Add your build commands here
                echo 'Building the application...'
            }
        }

        stage('Test') {
            steps {
                // Add your test commands here
                echo 'Running tests...'
            }
        }

        stage('Deploy') {
            steps {
                // Add your deployment commands here
                echo 'Deploying the application...'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
        }
        success {
            echo 'Build and deployment successful!'
        }
        failure {
            echo 'Build or deployment failed.'
        }
    }
}
