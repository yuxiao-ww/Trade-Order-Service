# 🚀 Trade Order Service (FastAPI + WebSocket)

This project is a simple trading order management system built with FastAPI. It supports RESTful APIs for order submission and retrieval, and real-time order updates via WebSocket.

## 📌 Features

- 📝 **REST API**: Submit & fetch trade orders (`POST /orders`, `GET /orders`)
- 🔄 **WebSocket Support**: Real-time order status updates (`ws://<server>/ws`)
- 🗃 **Database**: SQLite (for simplicity)
- 🐳 **Containerized**: Dockerfile for easy deployment
- ☁ **AWS Deployment**: Automated CI/CD pipeline using GitHub Actions

## 🚀 How to Run Locally
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/backend-service.git
cd backend-service
pip install -r requirements.txt
uvicorn backend.main:app --reload

Swagger UI: http://localhost:8000/docs

🐛 Docker Usage

docker build -t backend-service .
docker run -p 8000:8000 backend-service

☁ CI/CD (Automatic Deployment)

Whenever you git push to main, GitHub Actions will:

Build & push a Docker image to Docker Hub

SSH into AWS EC2, pull the latest image & restart the container

📄 API Endpoints

Method

Endpoint

Description

POST

/orders

Submit a new trade order

GET

/orders

Fetch all orders

WS

/ws

Real-time order updates

