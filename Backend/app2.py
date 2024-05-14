from fastapi import FastAPI , HTTPException, Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn
import db

app = FastAPI()

# Correct the directory for templates
templates = Jinja2Templates(directory="/Users/lavirubinstein/Desktop/lavi Cyber Prog/frontend/static/templates")

# Assuming you have static files correctly placed
app.mount("/static", StaticFiles(directory="/Users/lavirubinstein/Desktop/lavi Cyber Prog/frontend/static"), name="static")

@app.get("/")
async def get_home(request: Request):
    return templates.TemplateResponse("smarthome.html", {"request": request})


# A simple model to represent the light state
class LightState(BaseModel):
    is_on: bool

# Model to represent checkbox state
class CheckboxState(BaseModel):
    checkboxId: str
    state: str

# In-memory example of a light state
light_state = LightState(is_on=False)


# Dictionary to simulate database for checkbox states
checkbox_states = {
    "a": "off", "b": "off", "c": "off", "d": "off",
    "oven": "off", "microwave": "off", "dishwasher": "off",
    "diningLight": "off", "p": "off"
}

@app.get("/get-checkbox-state/{checkbox_id}")
def get_checkbox_state(checkbox_id: str):
    # Return the state of the checkbox
    if checkbox_id in checkbox_states:
        return {"state": checkbox_states[checkbox_id]}
    else:
        raise HTTPException(status_code=404, detail="Checkbox not found")

@app.post("/update-checkbox-state")
def update_checkbox_state(state: CheckboxState):
    # Update the state of the checkbox
    if state.checkboxId in checkbox_states:
        checkbox_states[state.checkboxId] = state.state
        return {"state": state.state}
    else:
        raise HTTPException(status_code=404, detail="Checkbox not found")

@app.on_event("startup")
def startup_event():
    db.create_tables()

@app.get("/lights")
def get_lights():
    lights = db.get_lights()
    return lights

@app.get("/lights/{light_id}/on")
def turn_on_light(light_id :int):
    db.update_light_state(light_id, True)
    return {light_id: True}

@app.get("/lights/{light_id}/off")
def turn_off_light(light_id: int):
    db.update_light_state(light_id, False)
    return {light_id: False}

@app.get("/lights/{light_id}/toggle")
def turn_off_light(light_id: int):
    lights = db.get_lights()
    db.update_light_state(light_id, not lights[light_id])
    return {light_id: not lights[light_id]}


if __name__ == "__main__":
    uvicorn.run(app , host="0.0.0.0",port = 8000)
