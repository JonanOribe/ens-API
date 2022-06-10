from typing import Optional
from fastapi import FastAPI
from src.controllers.notification import notification_controller
import uvicorn

from starlette.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]

app = FastAPI(middleware=middleware)

notification_controller(app)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)