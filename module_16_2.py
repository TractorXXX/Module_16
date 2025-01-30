from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/")
async def root() -> dict:
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def get_user_admin() -> dict:
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def get_user_id(user_id: Annotated[int, Path(gt=1, le=100, description="Enter User ID", example="1")]):
    return {"user_id": user_id, "name": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user/{username}/{age}")
async def read_user(
        username: Annotated[str, Path(min_length=5, max_length=20, regex="^[a-zA-Z0-9_-]+$",
                                      description="Enter username", example="UrbanUser")],
        age: Annotated[int, Path(gt=18, le=120, description="Enter age", example="24")]
):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
