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


@app.post("/lights/toggle")
def turn_off_light():
    light_state.is_on = not light_state.is_on
    return light_state

uvicorn.run(app , host="0.0.0.0",port = 8000)