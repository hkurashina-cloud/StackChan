from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Command(BaseModel):
    type: str
    value: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/command")
def command(cmd: Command):
    print(f"指示を受信: {cmd.type} = {cmd.value}")
    return {"result": "ok", "received": cmd}
