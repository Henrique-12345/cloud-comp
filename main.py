from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserRequest(BaseModel):
    user: str


@app.get("/auth/me")
async def read_me():
    return {"status": "Hello World"}

@app.post("/auth/me")
async def auth_me(req: UserRequest):
    return {"user": req.user, "ping": "pong"}