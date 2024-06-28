
import uvicorn

from typing import List, Optional
from fastapi import Depends, FastAPI, Header, Query, Response, UploadFile, APIRouter, Depends
from fastapi.params import File
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import requests
from asyncio import Lock, Semaphore
import os


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow access from all sources
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all request headers
)
output_dir = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'outputs', 'files'))
app.mount("/files", StaticFiles(directory=output_dir), name="files")
                            
def start_file_serve():
    uvicorn.run("btgenapi.file_serve:app", host="0.0.0.0",port=9999, 
                log_level="info")
