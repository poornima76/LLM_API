from pydantic import BaseModel

class ProductInfo(BaseModel):
    product_name: str
    product_description: str
    product_price: float
    rating: int