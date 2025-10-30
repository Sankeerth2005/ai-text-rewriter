pipeline {
    agent any

    environment {
        DOCKER_BUILDKIT = '1'
    }

    stages {
        stage('Pull from GitHub') {
            steps {
                git branch: 'main', url: 'https://github.com/Sankeerth2005/ai-text-rewriter.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ai-text-rewriter:latest .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker ps -q | xargs -r docker stop || true'
                sh 'docker ps -aq | xargs -r docker rm || true'
            }
        }

        stage('Run New Container') {
            steps {
                sh 'docker run -d -p 8501:8501 --env-file .env ai-text-rewriter:latest'
            }
        }
    }
}

