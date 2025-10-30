pipeline {
    agent any

    stages {
        stage('Pull from GitHub') {
            steps {
                git branch: 'main', url: 'https://github.com/Sankeerth2005/ai-text-rewriter.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'sudo docker build -t ai-text-rewriter:latest .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'sudo docker stop $(sudo docker ps -aq) || true'
                sh 'sudo docker rm $(sudo docker ps -aq) || true'
            }
        }

        stage('Run New Container') {
            steps {
                sh 'sudo docker run -d -p 8501:8501 --env-file .env ai-text-rewriter:latest'
            }
        }
    }
}
