#app/api/users.py
from fastapi import APIRouter
router = APIRouter(
    prefix="/users", 
    tags=["users"],
)


@router.get("/", summary="List all users (placeholder)") 
async def list_users(): 
    """Temporary hard-coded user list. Will be replaced with DB-backed implementation later.""" 
    return [ 
            {"id": 1, "name": "Alice", "email": "alice@example.com"}, 
            {"id": 2, "name": "Bob", "email": "bob@example.com"}, 
            ]