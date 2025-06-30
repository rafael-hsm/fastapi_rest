from fastapi import APIRouter


order_router = APIRouter(
    prefix="/orders",
    tags=["orders"],
    responses={404: {"description": "Not found"}}
)

@order_router.get("/")
async def list_orders():
    orders = [
        {"id": 1, "item": "Laptop", "quantity": 1, "price": 1200.00},
        {"id": 2, "item": "Smartphone", "quantity": 2, "price": 800.00},
        {"id": 3, "item": "Headphones", "quantity": 5, "price": 150.00},
        {"id": 4, "item": "Monitor", "quantity": 1, "price": 300.00},
        {"id": 5, "item": "Keyboard", "quantity": 3, "price": 50.00}
    ]
    return {"message": orders}
