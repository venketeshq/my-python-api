#!/bin/bash

set -e

APP_NAME="python-api"
PORT=5000

echo "Stopping old container..."
docker stop $APP_NAME 2>/dev/null || true
docker rm $APP_NAME 2>/dev/null || true

echo "Building latest Docker image..."
docker build -t $APP_NAME .

echo "Starting new container..."
docker run -d \
  --name $APP_NAME \
  -p $PORT:5000 \
  $APP_NAME

echo "✅ Deployment complete. App running on http://localhost:$PORT"
