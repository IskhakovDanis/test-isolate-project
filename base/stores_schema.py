from typing import List, Optional
from pydantic import BaseModel, RootModel


class ProductObject(BaseModel):
    product_id: int
    product_name: int | str
    is_available: bool
    store_id: int


class StoreObject(BaseModel):
    location: str
    store_name: str
    address: str
    products: List[ProductObject]


class StoreArray(RootModel):
    root: List[StoreObject]