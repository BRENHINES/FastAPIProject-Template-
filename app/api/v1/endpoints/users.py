from fastapi import APIRouter, Depends, HTTPException, status

from app.schemas.user import UserCreate, UserOut
from app.services.user_service import UserService, get_user_service

router = APIRouter()


@router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def create_user(payload: UserCreate, svc: UserService = Depends(get_user_service)) -> UserOut:
    user = await svc.create_user(payload)
    if not user:
        raise HTTPException(status_code=400, detail="User not created")
    return user
