from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.gzip import GZipMiddleware
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

# Enable gzip compression for large HTML responses
app.add_middleware(GZipMiddleware, minimum_size=500)

# Serve static files (if any)
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home():
    html_content = """
    <html lang="en">
    <head>
        <title>GPS</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="icon" href="/static/favicon.svg" type="image/svg+xml">
        <style>
            :root {
                --s: 8px;
            }

            body {
                background: #fff;
                font-family: 'Times New Roman', Times, serif;
                color: #000;
                margin: 0;
                padding: 0;
                font-size: clamp(16px, 1.2vw, 19px);
                line-height: 1.6;
            }

            .container {
                max-width: 980px;
                margin: 0 auto;
                padding: clamp(16px, 3vh, 24px) clamp(16px, 4vw, 32px);
            }

            .mast {
                margin-bottom: clamp(12px, 2vh, 18px);
            }

            .poster {
                display: grid;
                grid-template-columns: 1fr 1.15fr;
                gap: clamp(20px, 4vw, 44px);
                align-content: start;
            }

            .nav {
                text-align: left;
                display: flex;
                flex-wrap: wrap;
                gap: 18px;
                align-items: center;
                margin-bottom: 0;
                border-bottom: 1px solid #000;
                padding-bottom: calc(var(--s) * 2);
            }

            .nav a {
                color: #00f;
                text-decoration: underline;
                font-size: 16px;
            }

            .nav a:hover {
                color: #000;
                text-decoration-thickness: 2px;
            }

            .nav a:visited {
                color: #551a8b;
            }

            h1 {
                font-size: clamp(2.0em, 4vw, 2.8em);
                font-weight: 700;
                margin-bottom: clamp(12px, 2vh, 18px);
                color: #000;
            }

            h2 {
                font-size: clamp(1.2em, 2.2vw, 1.45em);
                margin-top: 32px;
                margin-bottom: clamp(10px, 1.6vh, 16px);
                color: #000;
                font-weight: 600;
            }

            .work h2 {
                margin-top: 0;
            }

            p, ul {
                color: #000;
                font-size: 1em;
            }

            ul {
                padding-left: 28px;
                margin-bottom: 0;
            }

            li {
                margin-bottom: clamp(8px, 1.4vh, 12px);
            }

            a {
                color: #00f;
                text-decoration: underline;
            }

            a:hover {
                color: #000;
                text-decoration-thickness: 2px;
            }

            a:visited {
                color: #551a8b;
            }

            a:focus-visible {
                outline: 2px solid #000;
                outline-offset: 2px;
            }

            footer {
                text-align: center;
                margin-top: clamp(18px, 4vh, 40px);
                color: #666;
                font-size: 14px;
                border-top: 1px solid #000;
                padding-top: calc(var(--s) * 2);
            }

            footer a {
                color: #00f;
            }

            @media (max-width: 900px) {
                .container {
                    padding: calc(var(--s) * 3) calc(var(--s) * 3);
                }
                .poster {
                    grid-template-columns: 1fr;
                    gap: calc(var(--s) * 4);
                    align-content: start;
                }
            }

            @media (max-width: 700px) {
                .container {
                    max-width: 100%;
                    padding: 24px 16px;
                }
                h1 {
                    font-size: 2em;
                }
                .nav a {
                    font-size: 15px;
                }
            }

            @media (max-height: 800px) {
                h2 {
                    margin-top: 28px;
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <header class="mast">
                <nav class="nav" aria-label="Links">
                    <a href="https://linkedin.com/in/madebygps" target="_blank" rel="noopener noreferrer">linkedin</a>
                    <a href="https://github.com/madebygps" target="_blank" rel="noopener noreferrer">github</a>
                    <a href="https://x.com/madebygps" target="_blank" rel="noopener noreferrer">x</a>
                    <a href="https://youtube.com/@gpslearnsai" target="_blank" rel="noopener noreferrer">youtube</a>
                    <a rel="me" href="http://madebygps.substack.com/">substack</a>
                </nav>
            </header>

            <main class="poster">
                <section class="intro">
                    <h1>Gwyneth Peña-Siguenza.</h1>
                    <p>I am a Python Advocate at Microsoft. I spend my work time helping developers build Python systems on Azure and teaching.</p>
                    <p>In my free time, I maintain <a href="https://learntocloud.guide" target="_blank" rel="noopener noreferrer">learntocloud</a> the courseware built on the belief that anyone can learn foundational cloud engineering skills with the right guide and discipline.</p>
                </section>

                <section class="work">
                    <h2>Recent Work</h2>
                    <ul>
                        <li><a href="http://aka.ms/pythonia/recursos" target="_blank" rel="noopener noreferrer">Serie introductoria de Python + AI</a> — 9-session course series covering LLMs, RAG, agents, and MCP in Spanish</li>
                        <li><a href="https://youtu.be/d_wpn8wW2sw?feature=shared" target="_blank" rel="noopener noreferrer">Getting Started with the PostgreSQL Extension for VS Code</a> — Video guide</li>
                        <li><a href="https://substack.com/inbox/post/163994416?r=fh7h7&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false&triedRedirect=true" target="_blank" rel="noopener noreferrer">A brutal guide to removing digital distractions</a> — No-BS system for protecting focus</li>
                        <li><a href="https://github.com/Azure-Samples/python-mcp-demos" target="_blank" rel="noopener noreferrer">Python MCP Demos</a> — End-to-end MCP server development with FastMCP, from local debugging to production deployment on Azure Container Apps with OAuth authentication</li>
                    </ul>
                </section>
            </main>
            <footer>
                built on azure app service —
                <a href="https://github.com/madebygps/simple-gps" target="_blank" rel="noopener noreferrer">github repo</a>
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


def main():
    port = int(os.environ.get("PORT") or os.environ.get("WEBSITES_PORT", 8000))
    logger.info(f"Starting server on port {port}")
    uvicorn.run(
        app, 
        host="0.0.0.0",
        port=port,
        log_level="info",
        proxy_headers=True,
        forwarded_allow_ips="*",
    )

if __name__ == "__main__":
    main()
