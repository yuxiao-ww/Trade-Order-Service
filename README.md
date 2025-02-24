# 🚀 Trade Order Service (FastAPI + WebSocket)

This project is a simple trading order management system built with FastAPI. It supports RESTful APIs for order submission and retrieval, and real-time order updates via WebSocket.

## 📌 Features

- 📝 **REST API**: Submit & fetch trade orders (`POST /orders`, `GET /orders`)
- 🔄 **WebSocket Support**: Real-time order status updates (`ws://<server>/ws`)
- 🗃 **Database**: SQLite (for simplicity)
- 🐳 **Containerized**: Dockerfile for easy deployment
- ☁ **AWS Deployment**: Automated CI/CD pipeline using GitHub Actions

## 🚀 How to Run Locally
### ⬇ Clone and Install Dependencies
```bash
git clone https://github.com/yuxiao-ww/Trade-Order-Service.git
cd backend
pip install -r requirements.txt
```
### ▶ Run FastAPI Server
```bash
uvicorn backend.main:app --reload
```

Swagger UI: http://localhost:8000/docs

## 🐳 Docker Usage
### 🏗 Build Docker Image
```bash
docker build -t backend-service .
```
### ▶ Run Docker Container
```bash
docker run -p 8000:8000 backend-service
```

## ☁ CI/CD (Automatic Deployment)

Whenever you git push to main, GitHub Actions will:

1. Build & push a Docker image to Docker Hub

2. SSH into AWS EC2, pull the latest image & restart the container


## 📄 API Endpoints

| Method | Endpoint  | Description |
|--------|----------|-------------|
| `POST` | `/orders` | Submit a new trade order |
| `GET`  | `/orders` | Fetch all orders |
| `WS`   | `/ws`     | Real-time order updates |



## 🚀 Deployment Steps
1️⃣ Setup AWS EC2

Launch an Ubuntu 24.04 instance

Install Docker:
```bash
sudo apt update && sudo apt install -y docker.io
```

2️⃣ Configure CI/CD

Add GitHub Secrets:

- DOCKER_USERNAME: lulu0424
- DOCKER_PASSWORD: ******(Ask author)
- EC2_HOST: ******(Ask author)
- EC2_SSH_KEY: ******(Ask author)

3️⃣ Deploy with GitHub Actions

Push changes to the main branch:
```bash
git add .
git commit -m "Deploy update"
git push origin main
```

The GitHub Actions workflow will automatically deploy to AWS.
