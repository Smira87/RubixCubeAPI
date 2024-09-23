from pydantic import BaseModel
from typing import List

class State(BaseModel):
    top: List[List[List[int]]]
    bottom: List[List]
    left: List[List]
    right: List[List]
    front: List[List]
    back: List[List]