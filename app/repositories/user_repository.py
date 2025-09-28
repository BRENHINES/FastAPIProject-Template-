from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_by_email(self, email: str) -> User | None:
        res = self.session.execute(select(User).where(User.email == email))
        return res.scalar_one_or_none()

    def create(self, email: str, hashed_password: str, full_name: str | None) -> User:
        user = User(email=email, hashed_password=hashed_password, full_name=full_name)
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user
