import os
from dotenv import load_dotenv

load_dotenv(f"{os.getcwd()}/.env")

import uvicorn

from fastapi import FastAPI
from src.infra.routes import accounts


app = FastAPI()
app.include_router(accounts.router)

if __name__ == '__main__':

    reload = True if os.environ.get('ENVIRONMENT', 'production') == 'development' else False
    debug = os.environ.get('DEBUG', False)
    host  = os.environ.get('HOST', "0.0.0.0")
    port  = os.environ.get('PORT', 8000)
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=reload, debug=debug)
