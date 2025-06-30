from fastapi import FastAPI


app = FastAPI(
    title="FastAPI REST",
    description="FastAPI REST API",
    version="0.0.1"
)


from views.routes.auth_routes import auth_router
from views.routes.order_routes import order_router


app.include_router(auth_router)
app.include_router(order_router)


@app.get("/")
async def root():
    return {"message": "Hello, World!"}
