install requirements
```bash
poetry install
```

create ".env" file with db connection data
```
APP_SWAGGER_URL = "..."
APP_REDOC_URL = "..."
APP_HOST = "..."
APP_PORT = "..."
```

run app
```bash
poetry run start_uvicorn
```
or
```bash
gunicorn deepra.src.main:app --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
```