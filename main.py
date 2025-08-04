from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI(title="Gwyneth Peña-Siguenza")

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
        <title>Gwyneth Peña-Siguenza</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
                background-color: #000;
                color: #999999;
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
            }
            
            h1 {
                font-size: 48px;
                font-weight: 700;
                color: #333333;
                margin-bottom: 30px;
                line-height: 1.1;
            }
            
            .subtitle {
                font-size: 20px;
                color: #999999;
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
            <a href="https://linkedin.com/in/gwyneth-pena-siguenza" target="_blank">linkedin</a>
            <a href="https://github.com/madebygps" target="_blank">github</a>
            <a href="https://twitter.com/madebygps" target="_blank">x</a>
            <a href="https://youtube.com/@madebygps" target="_blank">youtube</a>
        </div>
        
        <div class="container">
            <h1>hi i'm gps.</h1>
            
            <p class="subtitle">i'm just a gal that loves creating things for others.</p>
            
            <div class="content">
                <h2 style="color: #007AFF; font-size: 24px; margin-bottom: 20px; font-weight: 600;">work</h2>
                <p>i work at microsoft as a <span class="highlight">sr. cloud advocate</span> helping others build and deploy python workloads on azure.</p>
                
                <p>primarily focused on python + azure functions, azure app service and some iaas stuff. currently obsessing over how to <a href="https://aka.ms/madebygps" target="_blank">leverage agentic coding</a> to accomplish more.</p>
                
                <h2 style="color: #007AFF; font-size: 24px; margin-bottom: 20px; margin-top: 40px; font-weight: 600;">after hours</h2>
                <p>most recently, i developed <a href="#" target="_blank">learntocloud</a> — the largest free cloud learning resource in the world. we scaled to over 100,000 learners, created learning paths, grew content to millions of views, and built resources to help people find their tribe.</p>
                
                <p>worked on it for three years before closing it down to focus more on my microsoft work and spending time with family, cats, and books.</p>
                
                <h2 style="color: #007AFF; font-size: 24px; margin-bottom: 20px; margin-top: 40px; font-weight: 600;">goals</h2>
                <p>keep making things that help people. experiment with new tech. maybe write a book someday. definitely continue being curious about everything.</p>
            </div>
        </div>
    </body>
    </html>
    """
    return html_content

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
