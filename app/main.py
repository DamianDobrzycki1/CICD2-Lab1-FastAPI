from fastapi import FastAPI, HTTPException, status
from app.schemas import UserCreate

app = FastAPI(title= "lab1 - FastAPI User Api")

users: list[UserCreate] = []
@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/hello")
def hello():
    return {"message": "Hello World"}

@app.post("/api/users", status_code=status.HTTP_201_CREATED)
def add_user(new_user: UserCreate):
    for existing_user in users:
        if existing_user.userid == new_user.userid:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail="A user with this id already exists")
    users.append(new_user)
    return new_user

@app.delete("/api/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    for index, existing_user in enumerate(users):
        if existing_user.user_id == user_id:
            users.pop(index)
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User no found",
    )
