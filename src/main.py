from fastapi import FastAPI
from schemas import State
from cube import Cube
from typing import Optional
app = FastAPI()

@app.post("/show")
def show_face(state: State, side: Optional[str] = "front"):
    newCube = Cube({"top": state.top, "bottom": state.bottom, "left": state.left,
                    "right": state.right, "front": state.front, "back": state.back})
    return newCube.print_cube(side)
