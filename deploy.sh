#!/bin/bash
set -e

echo "🔹 Stopping existing containers (if any)..."
docker stop $(docker ps -aq) || true
docker rm $(docker ps -aq) || true

echo "🔹 Pulling latest code from GitHub..."
git pull origin main

echo "🔹 Building Docker image..."
docker build -t ai-text-rewriter .

echo "🔹 Running new container..."
docker run -d -p 8501:8501 --env-file .env ai-text-rewriter

echo "✅ Deployment complete!"
echo "🚀 App is running at: http://13.51.174.115:8501"
