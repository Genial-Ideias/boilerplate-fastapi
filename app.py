from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    return {'hello': 'world'}


@app.get('/items/{item_id}')
def read_ite(item_id: int, q: Optional[str] = None):
    return {'item_id': item_id, 'q': q}
