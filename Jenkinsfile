pipeline {
    agent any

    environment {
        IMAGE_NAME = 'guess-game'
        IMAGE_TAG  = "${env.BUILD_NUMBER}"
    }

    options {
        timestamps()
        disableConcurrentBuilds()
        buildDiscarder(logRotator(numToKeepStr: '20'))
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements-dev.txt
                '''
            }
        }

        stage('Lint') {
            steps {
                sh '''
                    . .venv/bin/activate
                    flake8 .
                    black --check .
                    isort --check-only .
                '''
            }
        }

        stage('Type Check') {
            steps {
                sh '''
                    . .venv/bin/activate
                    mypy game.py
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    . .venv/bin/activate
                    pytest --junitxml=test-results.xml
                '''
            }
            post {
                always {
                    junit 'test-results.xml'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} -t ${IMAGE_NAME}:latest ."
            }
        }

        stage('Push Docker Image') {
            when { branch 'main' }
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push ${IMAGE_NAME}:${IMAGE_TAG}
                        docker push ${IMAGE_NAME}:latest
                    '''
                }
            }
        }

        stage('Deploy') {
            when { branch 'main' }
            steps {
                sh 'docker compose up -d --build'
            }
        }
    }

    post {
        always {
            sh 'rm -rf .venv'
            cleanWs()
        }
        success {
            echo "Build #${env.BUILD_NUMBER} succeeded."
        }
        failure {
            echo "Build #${env.BUILD_NUMBER} failed."
        }
    }
}
