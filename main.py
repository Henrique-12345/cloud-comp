from fastapi import FastAPI

app = FastAPI(
    title="Meu Projeto FastAPI",
    description="Projeto exemplo com rota /auth/me",
    version="1.0.0"
)

@app.get("/auth/me")
async def read_me():
    return {"status": "Hello World"}
