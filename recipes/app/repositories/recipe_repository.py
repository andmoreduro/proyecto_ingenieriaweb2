from sqlalchemy.orm import Session

from models.recipe_model import Recipe
from schemas.recipe_schema import RecipeCreate


class RecipeRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_recipe(self, *, recipe_in: RecipeCreate, owner_id: int) -> Recipe:
        db_recipe = Recipe(
            **recipe_in.model_dump(),
            owner_id=owner_id
        )
        self.db.add(db_recipe)
        self.db.commit()
        self.db.refresh(db_recipe)
        return db_recipe

    def get_recipe_by_id(self, recipe_id: int) -> Recipe | None:
        return self.db.query(Recipe).filter(Recipe.id == recipe_id).first()
