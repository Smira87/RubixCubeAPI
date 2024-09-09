from pydantic import BaseModel
from typing import List

class State(BaseModel):
    top: List
    bottom: List
    left: List
    right: List
    front: List
    back: List