from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root() -> dict:
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def get_user_admin() -> dict:
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def get_user_id(user_id: int) -> dict:
    return {"user_id": user_id, "name": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user/")
async def read_user(username: str = "Иван", age: int = 35) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
