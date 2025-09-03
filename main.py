from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserRequest(BaseModel):
    user: str

@app.post("/auth/me")
async def auth_me(req: UserRequest):
    return {"user": req.user, "ping": "pong"}