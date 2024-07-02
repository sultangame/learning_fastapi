from fastapi.middleware.cors import CORSMiddleware
from src.config import settings
from fastapi import FastAPI
from src.api import api_v1
import uvicorn


app = FastAPI(debug=settings.DEBUG)
app.include_router(api_v1)
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=[
        "Content-Type",
        "Set-Cookie",
        "Access-Control-Allow-Headers",
        "Access-Control-Allow-Origin",
        "Authorization"
    ],
)

if __name__ == '__main__':
    uvicorn.run(
        app="main:app",
        reload=settings.RELOAD,
        host=settings.HOST,
        port=settings.PORT,
    )
