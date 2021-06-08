import uvicorn
from fastapi import FastAPI

from src.infra.routes import accounts

app = FastAPI()

app.include_router(accounts.router)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
