from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.core.security import hash_password
from app.db.session import get_session
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserOut


class UserService:
    def __init__(self, session: AsyncSession = Depends(get_session)):
        self.repo = UserRepository(session)

    async def create_user(self, payload: UserCreate) -> UserOut:
        exists = await self.repo.get_by_email(payload.email)
        if exists:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already used")
        user = await self.repo.create(
            email=payload.email,
            hashed_password=hash_password(payload.password),
            full_name=payload.full_name,
        )
        return UserOut.model_validate(user)
