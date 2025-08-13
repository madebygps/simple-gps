from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Gwen Peña-Siguenza",
    description="Personal website of Gwen Peña-Siguenza",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (if any)
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Gwen Peña-Siguenza</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
                background-color: #fff;
                color: #222;
                line-height: 1.6;
                min-height: 100vh;
            }
            .nav {
                text-align: left;
                padding: 40px 0 60px 0;
                max-width: 600px;
                margin: 0 auto;
                padding-left: 20px;
                padding-right: 20px;
            }
            .nav a {
                color: #007AFF;
                text-decoration: underline;
                margin-right: 30px;
                font-size: 16px;
            }
            .nav a:hover {
                opacity: 0.7;
            }
            .container {
                max-width: 600px;
                margin: 0 auto;
                padding: 0 20px;
                background: #fff;
                border-radius: 12px;
                box-shadow: none;
            }
            h1 {
                font-size: 48px;
                font-weight: 700;
                color: #222;
                margin-bottom: 30px;
                line-height: 1.1;
            }
            .subtitle {
                font-size: 20px;
                color: #444;
                margin-bottom: 40px;
                line-height: 1.4;
            }
            .content {
                font-size: 16px;
                margin-bottom: 30px;
                line-height: 1.7;
            }
            .content p {
                margin-bottom: 30px;
            }
            a {
                color: #007AFF;
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
            .highlight {
                color: #007AFF;
            }
            @media (max-width: 768px) {
                .nav {
                    padding-left: 15px;
                    padding-right: 15px;
                }
                .nav a {
                    margin-right: 20px;
                    font-size: 14px;
                }
                .container {
                    padding: 0 15px;
                }
                h1 {
                    font-size: 36px;
                }
                .subtitle {
                    font-size: 18px;
                }
                .content {
                    font-size: 15px;
                }
            }
        </style>
    </head>
    <body>
        <div class="nav">
            <a href="https://linkedin.com/in/madebygps" target="_blank">linkedin</a>
            <a href="https://github.com/madebygps" target="_blank">github</a>
            <a href="https://twitter.com/madebygps" target="_blank">x</a>
            <a href="https://youtube.com/@gpslearnsai" target="_blank">youtube</a>
        </div>
        
        <div class="container">
            <h1>Gwen Peña-Siguenza.</h1>
            <div class="content">
                <p>I like building things and teaching. I work at Microsoft as a Cloud Advocate helping customers build and deploy Python workloads on Azure.</p>

                <p>Primarily focused on improving the developer experience for Python + Azure App Service, Azure Functions, GitHub Copilot, and Cosmos DB.</p>

                <p>I maintain <a href="https://learntocloud.guide" target="_blank">learntocloud</a> — the courseware built on the belief that anyone can learn cloud engineering with the right guide and discipline.</p>
                
                
                <h2 style="color: #007AFF; font-size: 24px; margin-bottom: 20px; margin-top: 40px; font-weight: 600;">some of my favorite recent work</h2>
                <ul>
                    <li><a href="http://aka.ms/pythonia/grabaciones" target="_blank">Python + IA </a> Serie introductoria de 6 partes sobre IA con Python </li>
                    <li><a href="https://x.com/madebygps/status/1950352345327345837" target="_blank">Python Learning Space</a> How to configure GitHub Copilot to learn tech concepts deeply through hands-on exercises.</li>
                    <li><a href="https://substack.com/inbox/post/163994416?r=fh7h7&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false&triedRedirect=true" target="_blank">A brutal guide to removing digital distractions</a> I am a big fan of leveraging tech to enhance focus and productivity.</li>
                    <li><a href="https://github.com/madebygps/azd-simple-fastapi-container-appservice" target="_blank">Containerized FastAPI on App Service</a> Deploy a FastAPI app in a container on Azure App Service quick!</li>
                </ul>
            </div>
        </div>
    </body>
    </html>
    """
    return html_content

@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring"""
    return {
        "status": "healthy",
        "service": "simple-gps",
        "version": "1.0.0"
    }

@app.get("/")
async def root():
    """Redirect to home page"""
    return {"message": "Welcome to Gwyneth's website", "docs": "/docs"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    logger.info(f"Starting server on port {port}")
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=port,
        log_level="info"
    )
