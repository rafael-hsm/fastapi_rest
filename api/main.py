from fastapi import FastAPI


app = FastAPI(
    title="FastAPI REST",
    description="FastAPI REST API",
    version="0.0.1"
)

@app.get("/")
async def root():
    return {"message": "Hello, World!"}
