from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from starlette.applications import Starlette


@asynccontextmanager
async def lifespan(app: Starlette):
    print("START")
    yield {"greeting": "Hello world!"}
    print("SHUTDOWN")


app = FastAPI(lifespan=lifespan)


@app.get("/")
def index(request: Request):
    state = request.state._state
    greeting = state["greeting"]
    return {"greeting": greeting}
