from fastapi import APIRouter

auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={
        200: {"description": "Successful authentication"},
        400: {"description": "Bad request"},
        401: {"description": "Unauthorized"},
        403: {"description": "Forbidden"},
        404: {"description": "Not found"},
        405: {"description": "Method not allowed"},
        408: {"description": "Request timeout"},
        422: {"description": "Unprocessable entity"},
        429: {"description": "Too many requests"},
        500: {"description": "Internal server error"},
        }
)

@auth_router.get("/")
async def auth():
    return {"message": "Authentication endpoint", "authenticated": False}
