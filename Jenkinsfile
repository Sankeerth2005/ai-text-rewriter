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
                sh '''
                echo "⚙️ Building Docker image without BuildKit..."
                export DOCKER_BUILDKIT=0
                docker build -t ai-text-rewriter:latest .
                '''
            }
        }

        stage('Stop Old Container') {
            steps {
                sh '''
                echo "🛑 Stopping old containers (if any)..."
                docker ps -q | xargs -r docker stop
                docker ps -aq | xargs -r docker rm
                '''
            }
        }

        stage('Run New Container') {
            steps {
                sh '''
                echo "🚀 Running new container..."
                docker run -d -p 8501:8501 --env-file .env ai-text-rewriter:latest
                '''
            }
        }
    }
}

