from fastapi import FastAPI
from schemas import State
from cube import Cube
app = FastAPI()

@app.get("/")
def turn_face(state: State, direction: str):
    newCube = Cube()