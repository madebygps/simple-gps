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
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {
                background: #f6f7fa;
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
                color: #222;
                margin: 0;
                padding: 0;
                font-size: 18px;
            }
            .container {
                max-width: 700px;
                margin: 40px auto;
                background: #fff;
                border-radius: 12px;
                box-shadow: 0 2px 12px rgba(0,0,0,0.06);
                padding: 40px 32px;
            }
            .nav {
                text-align: left;
                margin-bottom: 32px;
            }
            .nav a {
                color: #2970ff;
                text-decoration: underline;
                margin-right: 24px;
                font-size: 16px;
            }
            .nav a:last-child {
                margin-right: 0;
            }
            h1 {
                font-size: 2.6em;
                font-weight: 700;
                margin-bottom: 24px;
                color: #222;
            }
            h2 {
                font-size: 1.2em;
                margin-top: 32px;
                margin-bottom: 16px;
                color: #2970ff;
                font-weight: 600;
            }
            p, ul {
                color: #444;
                font-size: 1em;
                line-height: 1.7;
            }
            ul {
                padding-left: 20px;
                margin-bottom: 24px;
            }
            li {
                margin-bottom: 10px;
            }
            a {
                color: #2970ff;
            }
            @media (max-width: 700px) {
                .container {
                    max-width: 100%;
                    margin: 0;
                    border-radius: 0;
                    box-shadow: none;
                    padding: 24px 8px;
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
                <a href="https://twitter.com/madebygps" target="_blank">x</a>
                <a href="https://youtube.com/@gpslearnsai" target="_blank">youtube</a>
                <a rel="me" href="https://hachyderm.io/@gps">mastodon</a>
                <a rel="me" href="https://bsky.app/profile/madebygps.com">bsky</a>
                <a rel="me" href="http://madebygps.substack.com/">substack</a>
            </div>
            <h1>Gwen Peña-Siguenza.</h1>
            <div class="content">
                <p>I like building and teaching. I work at Microsoft as a Cloud Advocate helping customers build and deploy Python workloads on Azure.</p>
                        
                <p>I maintain <a href="https://learntocloud.guide" target="_blank">learntocloud</a> — the courseware built on the belief that anyone can learn cloud engineering with the right guide and discipline.</p>
                
                
                <h2 style="color: #007AFF; font-size: 24px; margin-bottom: 20px; margin-top: 40px; font-weight: 600;">some of my favorite recent work</h2>
                <ul>
                    <li><a href="http://aka.ms/pythonia/grabaciones" target="_blank">Serie introductoria de 6 partes sobre IA con Python</a></li>
                    <li><a href="https://youtu.be/d_wpn8wW2sw?feature=shared" target="_blank">Getting Started with the PostgreSQL Extension for VS Code</a></li>
                    <li><a href="https://substack.com/inbox/post/163994416?r=fh7h7&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false&triedRedirect=true" target="_blank">Guide to removing digital distractions</a></li>
                    <li><a href="https://github.com/madebygps/llm-spanish-lexicon-eval" target="_blank">Evaluation suite for testing Spanish language comprehension and lexical knowledge in LLMs</a></li>
                </ul>
            </div>
            <footer style="text-align:center; margin-top:40px; color:#888; font-size:15px;">
                built on azure app service —
                <a href="https://github.com/madebygps/simple-gps" target="_blank" style="color:#2970ff;">github repo</a>
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
