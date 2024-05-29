from fastapi import APIRouter, Request, HTTPException, status, Depends
from fastapi.responses import JSONResponse

import db
from auth import create_response_with_cookie, add_session, remove_session, get_current_user

router = APIRouter(prefix="/users")


# TODO - return the existing session ID if already logged in

@router.post("/login")
async def login(request: Request):
    data = await request.form()
    username = data.get("username")
    hashed_password = data.get("password")

    if db.authenticate_user(username, hashed_password):
        session_id = add_session(username)

        return create_response_with_cookie(
            content={"message": "Login successful"},
            session_id=session_id
        )

    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")


# TODO - add basic encryption
# TODO - login automatically on signup

@router.post("/signup")
async def signup(request: Request):
    data = await request.form()
    username = data.get("username")
    hashed_password = data.get("password")

    db.query(f"INSERT INTO users (username, hashed_password) VALUES ('{username}', '{hashed_password}')")

    return JSONResponse(content={"message": "Signup successful"})


@router.post("/logout")
async def logout(request: Request, _=Depends(get_current_user)):
    session_id = request.cookies.get("session_id")
    if session_id:
        return remove_session(session_id)
