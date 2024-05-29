from fastapi import APIRouter, Depends

import db
from auth import get_current_user
import pi_irl_lights

router = APIRouter(prefix="/lights")

relay_control = pi_irl_lights.Relay()
relay_control.setup_relays()

@router.get("")
def get_lights(_=Depends(get_current_user)):
    lights = db.get_lights()
    return lights


@router.post("/{light_id}/on")
def turn_on_light(light_id: int, _=Depends(get_current_user)):
    db.update_light_state(light_id, True)
    return {light_id: True}


@router.post("/{light_id}/off")
def turn_off_light(light_id: int, _=Depends(get_current_user)):
    db.update_light_state(light_id, False)
    return {light_id: False}


@router.post("/{light_id}/toggle")
def turn_off_light(light_id: int, _=Depends(get_current_user)):
    global relay_control

    if relay_control.toggle_relay(light_id):
        lights = db.get_lights()
        db.update_light_state(light_id, not lights[light_id])

    return {light_id: not lights[light_id]}
