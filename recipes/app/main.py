from fastapi import FastAPI
from api.routers import recipe_router
from db.session import engine, Base

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Recipe Microservice")

app.include_router(recipe_router.router, prefix="/api/recipe", tags=["recipe"])


@app.get("/")
def read_root():
    return {"service": "Recipe Microservice is running"}
