from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.session import get_db
from models.recipe_model import Recipe
from repositories.recipe_repository import RecipeRepository
from schemas.recipe_schema import RecipeCreate


class RecipeService:
    def __init__(self, db: Session = Depends(get_db)):
        self.repo = RecipeRepository(db)

    def create_new_recipe(self, *, recipe_in: RecipeCreate, owner_id: int) -> Recipe:
        return self.repo.create_recipe(recipe_in=recipe_in, owner_id=owner_id)
