from fastapi import FastAPI
import http.client
import json

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

