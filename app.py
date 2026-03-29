from fastapi import FastAPI
from pydantic import BaseModel
from environment import EmailEnv

app = FastAPI(title="Email OpenEnv")

env = EmailEnv()

class ActionInput(BaseModel):
    action: int

@app.get("/")
def home():
    return {"status": "running"}

@app.get("/reset")
def reset(task: str = "easy"):
    state = env.reset(task)
    return {
        "state": state,
        "task": task
    }

@app.post("/step")
def step(input: ActionInput):
    state, reward, done, info = env.step(input.action)
    return {
        "state": state,
        "reward": reward,
        "done": done,
        "info": info
    }

@app.get("/state")
def state():
    return {"state": env.state()}