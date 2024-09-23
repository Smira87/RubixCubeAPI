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
    newCube = Cube(state)
    return newCube.print_cube(side)

@router.post("/turn")
def turn_cube(direction: Optional[str] = "right", times: Optional[int] = 1, state: Optional[State] = None):
    newCube = Cube(state)
    newCube.turn_cube(direction, times)
    return newCube