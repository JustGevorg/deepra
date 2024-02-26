import uvicorn
import gunicorn
from fastapi import FastAPI, Query
from typing import Annotated
from fastapi.routing import APIRouter
import deepra.src.config as config

app = FastAPI(docs_url=config.APP_SWAGGER_URL, redoc_url=config.APP_REDOC_URL)
router = APIRouter()


@router.get("/")
async def say_hello(name: Annotated[str, Query()] = "Recruto",
                    message: Annotated[str, Query()] = "Давай дружить"):

    return f"Hello {name}! {message}!"


app.include_router(router)


def start_uvicorn():
    uvicorn.run(app, host=config.APP_HOST, port=config.APP_PORT)
