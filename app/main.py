from fastapi import FastAPI
from app.routes.user_routes import user_app
app = FastAPI()
app.include_router(user_app)

@app.get("/")
async def hello():
    return {"message": "Hello, World!"}


