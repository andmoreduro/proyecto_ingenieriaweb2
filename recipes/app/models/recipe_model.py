import enum

from sqlalchemy import Column, Enum, Integer, String, Text

from db.session import Base


class ExperienceLevel(enum.Enum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"


class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(Text, nullable=True)
    difficulty = Column(Enum(ExperienceLevel), nullable=False)
    prep_time_minutes = Column(Integer, nullable=False)
    owner_id = Column(Integer, index=True, nullable=False)
