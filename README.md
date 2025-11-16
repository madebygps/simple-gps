# simple-gps

My personal landing page.

## Run locally

``` bash
uv sync
```

```bash
uv run main.py
```

Visit `http://localhost:8000`

## Deploy

Deployed via Azure App Service using `azd`:

```bash
azd up
```

Infrastructure defined in `infra/` using Bicep.
