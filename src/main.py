from fastapi import FastAPI
from schemas import State
app = FastAPI()

@app.get("/")
def turn_face(state: State, direction: str):
    pass