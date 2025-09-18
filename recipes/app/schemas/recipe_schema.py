from typing import Optional

from pydantic import BaseModel

from models.recipe_model import ExperienceLevel


# Shared properties
class RecipeBase(BaseModel):
    name: str
    description: Optional[str] = None
    difficulty: ExperienceLevel
    prep_time_minutes: int

# Properties to receive on item creation
class RecipeCreate(RecipeBase):
    pass

# Properties to return to client
class Recipe(RecipeBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True