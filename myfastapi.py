import logging
from fastapi import FastAPI
import uvicorn

APP = FastAPI()
logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)

@APP.get("/")
async def root():
    LOGGER.info("This function is called")
    return {"message": "My webhook for the PD POC"}

if __name__ == "__main__":
    uvicorn.run("main:APP", host="127.0.0.1", port=8000)
