pipeline {
    agent any

    environment {
        IMAGE_NAME = "game-app"
    }

    stages {
        stage('Checkout') {
            steps {
                // Pull code from GitHub
                git 'https://github.com/YOUR_USERNAME/YOUR_REPO.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image locally
                    docker.build("${IMAGE_NAME}:latest")
                }
            }
        }

        stage('Run Tests') {
            steps {
                // Run pytest to validate code
                sh 'pytest'
            }
        }

        stage('Deploy') {
            steps {
                echo "Deployment stage: Here you could push Docker image or run container"
                // Example: docker run --rm ${IMAGE_NAME}:latest
            }
        }
    }

    post {
        success {
            echo "Pipeline succeeded!"
        }
        failure {
            echo "Pipeline failed 😞"
        }
    }
}

