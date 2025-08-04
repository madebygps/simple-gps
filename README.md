# Simple GPS Landing Page

A minimal, fast-loading landing page built with FastAPI for deployment on Azure App Service.

## Features

- 🚀 Ultra-fast loading with inline CSS
- 📱 Responsive design
- ☁️ Optimized for Azure App Service
- 🔧 GitHub Actions CI/CD ready

## Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python main.py
   ```

3. Visit `http://localhost:8000`

## Azure Deployment

### Prerequisites

1. Create an Azure App Service (Python 3.11)
2. Get the publish profile from Azure Portal

### GitHub Secrets

Add these secrets to your GitHub repository:

- `AZURE_WEBAPP_NAME`: Your Azure App Service name
- `AZURE_WEBAPP_PUBLISH_PROFILE`: Download from Azure Portal → App Service → Get publish profile

### Deployment

The app automatically deploys to Azure when you push to the `main` branch.

## Project Structure

```
simple-gps/
├── main.py              # FastAPI application
├── requirements.txt     # Python dependencies
├── web.config          # Azure App Service configuration
├── startup.sh          # Startup script
└── .github/
    └── workflows/
        └── deploy.yml   # GitHub Actions workflow
```

## Performance Optimizations

- Inline CSS (no external stylesheets)
- Minimal dependencies
- Optimized for Azure App Service
- Gzip compression enabled via web.config
