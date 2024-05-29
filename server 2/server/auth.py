import secrets
from typing import Optional

from fastapi import Request, HTTPException, status
from fastapi.responses import JSONResponse

sessions = {}


def create_response_with_cookie(content: dict, session_id: str) -> JSONResponse:
    response = JSONResponse(content=content)
    response.set_cookie(
        key="session_id",
        value=session_id,
        httponly=True,
        max_age=1800  # 30 minutes
    )
    return response


def remove_session(session_id: str) -> JSONResponse:
    sessions.pop(session_id)
    response = JSONResponse("logout")
    response.delete_cookie(
        key="session_id",
        path="/"
    )
    return response


# TODO - encrypt session ID - if there is enough time

def get_current_user(request: Request) -> Optional[str]:
    session_id = request.cookies.get("session_id")
    if session_id in sessions:
        return sessions[session_id]
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")


def add_session(username: str):
    # Create a session ID
    session_id = secrets.token_hex(16)
    sessions[session_id] = username
    return session_id
