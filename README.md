# Cloud Application - Group 10

![Django CI Pipeline](https://github.com/assignment-cloud/cloud-computer-chapter10/actions/workflows/ci.yml/badge.svg)

A premium, modern web application built with Django for the Cloud Computing course (Level 4).

## Features
- **Premium UI**: Modern dark-mode design with glassmorphism and smooth animations.
- **Dynamic Dashboard**: Displays group information and team members dynamically from the Django backend.
- **System Monitoring**: Includes real-time server status, time, and Python environment information.
- **Health API**: A dedicated JSON endpoint for system health monitoring (`/api/health/`).
- **Cloud-Ready**: Includes `Procfile`, `Dockerfile`, and `WhiteNoise` for seamless deployment.
- **Production Optimized**: Static file compression and environment safety ready.
- **Responsive Design**: Fully optimized for mobile, tablet, and desktop views.
- **CI/CD Integrated**: Automated testing pipeline using GitHub Actions.

## Tech Stack
- **Backend**: Django 6.0
- **Frontend**: HTML5, Vanilla CSS3 (Custom Design System)
- **Environment**: Python 3.x
- **CI/CD**: GitHub Actions

## Setup & Running
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run migrations (if any):
   ```bash
   python manage.py migrate
   ```
3. Start the development server:
   ```bash
   python manage.py runserver 8080
   ```
4. Access the application at `http://127.0.0.1:8080`

## Team Members
- NDOLI Jean Damascene
- UMUTONI Belise
- MUHIRWA Joyeuse Sainte Trinite
- TUYIZERE Claude
- NTAWURENZINGABIRE Dorothee
- NSHUTI Maurice
- NGOGA NIYOMANA Pacifique

---
*Developed for the Cloud Computing course taught by Dr. Irene.*

## CI/CD Pipeline
This project uses **GitHub Actions** to automate the testing process. The workflow is triggered on every push to the `master` branch.

### Automated Tasks:
- **Environment Setup**: Configures Python 3.10.
- **Dependency Installation**: Installs all required packages from `requirements.txt`.
- **Test Execution**: Runs the Django test suite (`python manage.py test`) to ensure code stability.
