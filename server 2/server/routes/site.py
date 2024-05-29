import os

from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from auth import get_current_user
from consts import ROOT_DIR

router = APIRouter(prefix="/site")

templates = Jinja2Templates(directory=os.path.join(ROOT_DIR, "static", "templates"))


@router.get("/smarthome")
def get_home(request: Request, _=Depends(get_current_user)):
    return templates.TemplateResponse("smarthome.html", {"request": request})


@router.get("/login")
def get_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})
