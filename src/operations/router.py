from fastapi import APIRouter
from typing import Optional
from cube import Cube
from schemas import State

router = APIRouter(
    prefix = "/operations",
    tags = ["Operation"]
)
@router.post("/")
def show_face(state: Optional[State] = None, side: Optional[str] = "front"):
    newCube = Cube({"top": state.top, "bottom": state.bottom, "left": state.left,
                    "right": state.right, "front": state.front, "back": state.back})
    return newCube.print_cube(side)
