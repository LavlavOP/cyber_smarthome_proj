import os
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

import db
from consts import ROOT_DIR
from routes import lights, users, site


@asynccontextmanager
async def lifespan(_):
    db.run_schema()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(lights.router)
app.include_router(users.router)
app.include_router(site.router)
app.mount("/static", StaticFiles(directory=os.path.join(ROOT_DIR, "static")), name="static")


@app.get("/")
async def root():
    return RedirectResponse(url="/site/login")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
