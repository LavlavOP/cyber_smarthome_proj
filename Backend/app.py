from fastapi import FastAPI , HTTPException
from pydantic import BaseModel
import uvicorn
import db

app = FastAPI()

# A simple model to represent the light state
class LightState(BaseModel):
    is_on: bool

# In-memory example of a light state
light_state = LightState(is_on=False)


@app.on_event("startup")
def startup_event():
    db.create_tables()

@app.get("/lights")
def get_lights():
    lights = db.get_lights()
    return lights

@app.post("/lights/{light_id}/on")
def turn_on_light(light_id: int):
    db.update_light_state(light_id, True)
    return {light_id: True}

@app.post("/lights/{light_id}/off")
def turn_off_light(light_id: int):
    db.update_light_state(light_id, False)
    return {light_id: False}

@app.post("/lights/{light_id}/toggle")
def turn_off_light(light_id: int):
    lights = db.get_lights()
    db.update_light_state(light_id, not lights[light_id])
    return {light_id: not lights[light_id]}


if __name__ == "__main__":
    uvicorn.run(app , host="0.0.0.0",port = 8000)
