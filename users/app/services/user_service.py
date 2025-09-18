from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.session import get_db
from models.user_model import User
from repositories.user_repository import UserRepository
from schemas.user import UserCreate


class UserService:
    def __init__(self, db: Session = Depends(get_db)):
        self.repo = UserRepository(db)

    def register_user(self, user_data: UserCreate) -> User:
        existing_user = self.repo.get_user_by_email(email=user_data.email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered",
            )
        return self.repo.create_user(user=user_data)
