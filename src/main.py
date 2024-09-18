from fastapi import FastAPI
from schemas import State
from cube import Cube
from typing import Optional
app = FastAPI()

app.include_router(router_operation)