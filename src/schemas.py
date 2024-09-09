from pydantic import BaseModel
from typing import List

class State(BaseModel):
    face: str
    top: List
    bottom: List
    left: List
    right: List
    front: List
    back: List