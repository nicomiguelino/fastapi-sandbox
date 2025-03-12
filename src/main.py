from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False


@app.get('/')
async def read_root():
    return {
        'Hello': 'Milky Way'
    }


@app.get('/items/{item_id}')
async def read_item(item_id: int, q: str | None = None):
    return {
        'item_id': item_id,
        'q': q,
    }


@app.put('/items/{item_id}')
def update_item(
    item_id: int,
    item: Item,
    q: str | None = None,
):
    return {
        'item_id': item_id,
        'item': item,
    }
