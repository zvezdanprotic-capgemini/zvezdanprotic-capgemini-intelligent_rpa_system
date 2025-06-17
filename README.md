# Intelligent RPA System

## Getting Started on macOS

### 1. Install Google Cloud SDK

```sh
curl https://sdk.cloud.google.com | bash
exec -l $SHELL
gcloud init
```

### 2. Set Up Virtual Environment

```sh
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Authenticate with Google Cloud

```sh
gcloud auth application-default login
```

### 5. Configure Environment Variables

Create a `.env` file in the `orchestrator_agent` folder with the following content:

```env
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=<our-team-project-id>
GOOGLE_CLOUD_LOCATION=us-central1
MODEL=gemini-2.0-flash-001
```

### 6. Run the ADK Web Application

```sh
adk web
```

### 7. Access the Application

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.