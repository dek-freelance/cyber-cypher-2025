from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from src.config.constants import RolesNum, Roles
from src.backend.groq_chat import req_groq_langchain

app = FastAPI()

class ChatMsg(BaseModel):
    role: str
    msg: str

@app.post("/api/v1/chatgroq")
async def root(data: ChatMsg):
    ans = req_groq_langchain(RolesNum[data.role], data.msg)
    return {ans}

def main():
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8001,
        reload=True
    )
if __name__ == "__main__":
    main()