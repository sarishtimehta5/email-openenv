from fastapi import FastAPI
from environment import EmailEnv

app = FastAPI()

env = EmailEnv()

@app.get("/")
def home():
    return {"message": "Email OpenEnv running"}

@app.post("/reset")
def reset():
    state = env.reset()
    return {"state": state}

@app.post("/step")
def step(action: dict):
    next_state, reward, done, info = env.step(action)
    return {
        "next_state": next_state,
        "reward": reward,
        "done": done,
        "info": info
    }
