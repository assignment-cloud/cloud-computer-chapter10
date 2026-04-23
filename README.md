# Cloud Computing Coursework
## Group 10 - Level 4

![Django CI Pipeline](https://github.com/assignment-cloud/cloud-computer-chapter10/actions/workflows/ci.yml/badge.svg)

---

## 📋 Chapter 10: DevOps & CI/CD Lifecycle
**Objective:** Demonstrate a full DevOps lifecycle for a cloud application.

### 🚀 Solutions:
1. **Git Repository & App**: Hosted at [GitHub](https://github.com/assignment-cloud/cloud-computer-chapter10). Modern Django web app.
2. **Build & Test**: Automated via GitHub Actions. Runs tests on every push.
3. **Packaging**: Application is containerized using **Docker** (`Dockerfile`).
4. **Deployment**: Live deployment on **Render**: [https://cloud-computer-chapter10.onrender.com](https://cloud-computer-chapter10.onrender.com)
5. **Monitoring**: Alerting rule defined in `monitoring/alert_rules.yml` (CPU > 80%).

---

## ⚡ Chapter 11: Event-Driven Architecture
**Objective:** Build an event-driven workflow using a storage trigger and a cloud function.

### 🛠️ Implementation:
- **Storage Bucket (Simulated)**: The `events/uploads/` directory.
- **Event Trigger**: `events/trigger.py` monitors for new file uploads.
- **Cloud Function**: `events/function.py` processes the file and saves metadata to `events/logs/`.

### 📝 How to run the simulation:
1. Open a terminal and run: `python events/trigger.py`
2. In another window, add any file to the `events/uploads/` folder.
3. Observe the terminal logs and the generated metadata in `events/logs/`.

### 🌐 Live Frontend Testing (Production):
1. Navigate to the **[Live Dashboard](https://cloud-computer-chapter10.onrender.com)**.
2. Scroll to the **"Event-Driven Testing"** section.
3. Upload any file (Image, Text, etc.).
4. The dashboard will communicate with the backend API (`/api/upload/`), save the file to cloud storage, and trigger the background processing function.
5. Verification can be seen in the real-time server logs on Render.

### 💡 Design Analysis:
- **Advantages**:
    - **Scalability**: Logic only executes when an event occurs, handling bursts easily.
    - **Cost-Efficiency**: Resources are only consumed during active processing (Serverless model).
    - **Asynchronous**: The main application isn't blocked while the file is being processed.
- **Limitations**:
    - **Cold Starts**: Initial invocation can be slow.
    - **Timeout Limits**: Not suitable for extremely long-running tasks.
    - **Observability**: Tracking a single request across multiple event-driven components can be difficult.

---

## 🛠️ Tech Stack
- **Backend**: Django 6.0
- **DevOps**: GitHub Actions, Docker
- **Serverless Simulator**: Python Event-Driven logic
- **Monitoring**: Prometheus Alert Rules

## 👥 Team Members
- **NDOLI Jean Damascene**
- **Belise UMUTONI**
- **MUHIRWA Joyeuse Sainte Trinite**
- **TUYIZERE Claude**
- **NTAWURENZINGABIRE Dorothee**
- **NSHUTI Maurice**
- **NIYOMANA NGOGA Pacifique**

---
*Developed for the Cloud Computing course taught by Dr. Irene.*
