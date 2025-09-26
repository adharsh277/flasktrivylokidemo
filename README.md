# flasktrivylokidemo
# 🐍 Flask App with Trivy, Loki, Promtail & GitHub Actions CI/CD

![Docker](https://img.shields.io/badge/Docker-Containerization-blue?logo=docker)
![Trivy](https://img.shields.io/badge/Trivy-Security%20Scanner-red?logo=aqua)
![Loki](https://img.shields.io/badge/Loki-Log%20Aggregation-purple?logo=grafana)
![Promtail](https://img.shields.io/badge/Promtail-Log%20Forwarder-orange?logo=grafana)
![CI/CD](https://img.shields.io/badge/GitHub%20Actions-CI/CD-green?logo=githubactions)
![Python](https://img.shields.io/badge/Python-Flask-app-blue?logo=python)

---

## 📌 Project Overview

This project demonstrates a **DevOps pipeline** that integrates:

- ✅ **Flask app** containerized with Docker  
- ✅ **Trivy** scanning for vulnerabilities & SBOM  
- ✅ **Promtail → Loki** pipeline for log collection  
- ✅ **GitHub Actions** CI/CD to build & push images  

It provides a **mini end-to-end setup** for secure, observable, and automated deployments.

---

## 🚀 What I Learned

- ⚙️ **Dockerization** of Flask applications  
- 🔍 **Image scanning & SBOM generation** using Trivy  
- 📜 **Log aggregation pipeline** with Promtail + Loki  
- 🔁 **CI/CD automation** using GitHub Actions workflows  
- 📂 **Infrastructure as Code** with `docker-compose` & YAML  
- 🐍 Python web development with logging to files  

---

## 🧰 Tech Stack

| Layer               | Tools / Tech                         |
|----------------------|---------------------------------------|
| **Backend App**      | Python (Flask)                       |
| **Security**         | Trivy (SBOM + vulnerability scan)    |
| **Log Forwarding**   | Promtail                             |
| **Log Aggregation**  | Loki                                 |
| **Containerization** | Docker, Docker Compose               |
| **CI/CD**            | GitHub Actions                       |
| **Source Control**   | Git, GitHub                          |
| **DevOps Skills**    | CI/CD, Observability, Security, YAML |

---

## 🏗️ Project Structure

flasktrivylokidemo/
├── app.py # Flask application
├── Dockerfile # Flask app Dockerfile
├── docker-compose.yml # Multi-service setup (Flask, Loki, Promtail)
├── promtail-config.yaml # Promtail log forwarder config
├── loki-config.yml # Loki configuration
├── .github/
│ └── workflows/
│ └── gitworkflow.yml # GitHub Actions pipeline
├── requirements.txt # Flask dependencies
└── README.md

## ⚡ CI/CD Pipeline

GitHub Actions workflow automates:  

1. **Build Docker image** of Flask app  
2. **Scan image with Trivy** (optional extension)  
3. **Push to Docker Hub** automatically  

---

## ▶️ Running Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/<your-username>/flasktrivylokidemo.git
   cd flasktrivylokidemo
Start services:

bash
Copy
Edit
docker-compose up -d
Access:

Flask app → http://localhost:5000

Loki API → http://localhost:3100

📊 Future Improvements
Add Grafana dashboards for Loki logs

Extend Trivy scans with GitHub Action reports

Deploy to Kubernetes for scaling
