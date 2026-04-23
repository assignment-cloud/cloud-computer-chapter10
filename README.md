<<<<<<< HEAD
# Chapter 10: Cloud Application Assignment
## Group 10 - Cloud Computing (Level 4)

![Django CI Pipeline](https://github.com/assignment-cloud/cloud-computer-chapter10/actions/workflows/ci.yml/badge.svg)

---

## 📋 Assignment Overview
**Objective:** Create a cloud application repository that demonstrates a full DevOps lifecycle, including build, test, packaging, deployment, and monitoring.

### 🎯 Core Requirements:
1. **Repository & App**: Create a Git repository and commit a web application.
2. **Build & Test**: Define automated build and test stages.
3. **Packaging**: Package the application as a container image.
4. **Deployment**: Simulate deployment to a test environment.
5. **Monitoring**: Record a metric and configure an alerting rule (CPU > 80%).

---

## 🚀 Implementation & Solutions

### 1. Git Repository & Web Application
- **Repository**: [assignment-cloud/cloud-computer-chapter10](https://github.com/assignment-cloud/cloud-computer-chapter10)
- **Application**: A modern Django-based web application with a premium UI, system dashboard, and health monitoring APIs.

### 2. Build and Test Stages
Integrated via **GitHub Actions** (`.github/workflows/ci.yml`):
- **Test Stage**: Runs `python manage.py test` to verify code integrity on every push.
- **Build Stage**: Sets up the Python environment and installs dependencies from `requirements.txt`.

### 3. Packaging (Containerization)
- The application is containerized using **Docker**.
- **Artifact**: A Docker image is created using the `Dockerfile` in the root directory.
- `docker build -t cloud-app:latest .`

### 4. Deployment to Test Environment
- **Live Deployment**: The application is successfully deployed to **Render**.
- **URL**: [https://cloud-computer-chapter10.onrender.com](https://cloud-computer-chapter10.onrender.com)
- The pipeline verifies the deployment readiness of the containerized app.

### 5. Metrics & Alerting Configuration
- **Defined Metric**: System CPU Utilization.
- **Alerting Rule**: An alert is configured to trigger if **CPU usage > 80%** for more than 5 minutes.
- **Configuration File**: `monitoring/alert_rules.yml`

---

## 🛠️ Tech Stack
- **Backend**: Django 6.0
- **Frontend**: HTML5, Vanilla CSS3 (Glassmorphism UI)
- **DevOps**: GitHub Actions, Docker
- **Monitoring**: Prometheus-style Alert Rules

## 👥 Team Members
- **NDOLI Jean Damascene**
- **UMUTONI Belise**
- **MUHIRWA Joyeuse Sainte Trinite**
- **TUYIZERE Claude**
- **NTAWURENZINGABIRE Dorothee**
- **NSHUTI Maurice**
- **NGOGA NIYOMANA Pacifique**

---
*Developed for the Cloud Computing course taught by Dr. Irene.*
=======
# cloud-computer-chapter10
>>>>>>> 93d6e5d66e41351d1a216fd8b6bddaed3ee5c42c
