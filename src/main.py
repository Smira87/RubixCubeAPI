from fastapi import FastAPI
from schemas import State
from cube import Cube
from typing import Optional
app = FastAPI()

@app.get("/show")
def show_face(state: State, side: Optional[str] = "Front"):
    newCube = Cube({"Top": state.top, "Bottom": state.bottom, "Left": state.left,
                    "Right": state.right, "Front": state.front, "Back": state.back})
    return newCube.print_cube(side)
