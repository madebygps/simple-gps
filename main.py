from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os
import logging
import uvicorn

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Gwyneth Peña-Siguenza",
    description="Personal website of Gwyneth Peña-Siguenza",
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
    <head>
        <title>GPS</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {
                background: #fff;
                font-family: 'Times New Roman', Times, serif;
                color: #000;
                margin: 0;
                padding: 0;
                font-size: 18px;
            }

            .container {
                max-width: 700px;
                margin: 40px auto;
                padding: 40px 32px;
            }

            .nav {
                text-align: left;
                margin-bottom: 32px;
                border-bottom: 2px solid #000;
                padding-bottom: 16px;
            }

            .nav a {
                color: #00f;
                text-decoration: underline;
                margin-right: 24px;
                font-size: 16px;
            }

            .nav a:hover {
                color: #f0f;
            }

            .nav a:visited {
                color: #551a8b;
            }

            .nav a:last-child {
                margin-right: 0;
            }

            h1 {
                font-size: 2.6em;
                font-weight: bold;
                margin-bottom: 24px;
                color: #000;
            }

            h2 {
                font-size: 1.4em;
                margin-top: 32px;
                margin-bottom: 16px;
                color: #000;
                font-weight: bold;
            }

            p, ul {
                color: #000;
                font-size: 1em;
                line-height: 1.6;
            }

            ul {
                padding-left: 40px;
                margin-bottom: 24px;
            }

            li {
                margin-bottom: 8px;
            }

            a {
                color: #00f;
                text-decoration: underline;
            }

            a:hover {
                color: #f0f;
            }

            a:visited {
                color: #551a8b;
            }

            footer {
                text-align: center;
                margin-top: 40px;
                color: #666;
                font-size: 14px;
                border-top: 1px solid #000;
                padding-top: 20px;
            }

            footer a {
                color: #00f;
            }

            @media (max-width: 700px) {
                .container {
                    max-width: 100%;
                    margin: 0;
                    border-radius: 0;
                    border-left: none;
                    border-right: none;
                    padding: 24px 16px;
                }
                h1 {
                    font-size: 2em;
                }
                .nav a {
                    font-size: 15px;
                    margin-right: 16px;
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="nav">
                <a href="https://linkedin.com/in/madebygps" target="_blank">linkedin</a>
                <a href="https://github.com/madebygps" target="_blank">github</a>
                <a href="https://x.com/madebygps" target="_blank">x</a>
                <a href="https://youtube.com/@gpslearnsai" target="_blank">youtube</a>
                <a rel="me" href="http://madebygps.substack.com/">substack</a>
            </div>
            <h1>Gwyneth Peña-Siguenza.</h1>
            <div class="content">
                <p>I am a Python Advocate at Microsoft. I spend my work time helping developers build Python systems on Azure and teaching.</p>

                <p>In my free time, I maintain <a href="https://learntocloud.guide" target="_blank">learntocloud</a> the courseware built on the belief that anyone can learn foundational cloud engineering skills with the right guide and discipline.</p>


                <h2>Recent Work</h2>
                <ul>
                    <li><a href="http://aka.ms/pythonia/recursos" target="_blank">Serie introductoria de Python + AI</a> — 9-session course series covering LLMs, RAG, agents, and MCP in Spanish</li>
                    <li><a href="https://youtu.be/d_wpn8wW2sw?feature=shared" target="_blank">Getting Started with the PostgreSQL Extension for VS Code</a> — Video guide</li>
                    <li><a href="https://substack.com/inbox/post/163994416?r=fh7h7&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false&triedRedirect=true" target="_blank">A brutal guide to removing digital distractions</a> — No-BS system for protecting focus</li>
                    <li><a href="https://github.com/Azure-Samples/python-mcp-demos" target="_blank">Python MCP Demos</a> — MCP implementations using FastMCP with stdio/HTTP transports, LangChain/Agent Framework integration, and Azure Container Apps deployment</li>
                </ul>
            </div>
            <footer>
                built on azure app service —
                <a href="https://github.com/madebygps/simple-gps" target="_blank">github repo</a>
            </footer>
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


def main():
    port = int(os.environ.get("PORT", 8000))
    logger.info(f"Starting server on port {port}")
    uvicorn.run(
        app, 
        host="0.0.0.0",
        port=port,
        log_level="info"
    )

if __name__ == "__main__":
    main()
