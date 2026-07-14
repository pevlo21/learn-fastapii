from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Worlds"}

@app.post("/api/v1/login")
async def login(username: str, password: str):
    print(f"Username: {username}, Password: {password}")
    return {"message": "Login endpoint"}