from fastapi import FastAPI , HTTPException, Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn
import db
import testPi
app = FastAPI()

# Correct the directory for templates
templates = Jinja2Templates(directory="/home/lavi/Desktop/lavi cyber test/frontend/static/templates")

# Assuming you have static files correctly placed
app.mount("/static", StaticFiles(directory="/home/lavi/Desktop/lavi cyber test/frontend/static"), name="static")

db.deleteTale()

relay_control = testPi.Relay()
relay_control.setup()

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
    return db.get_lights()

@app.get("/lights/{light_id}/toggle")
def toggle_light(light_id: int):
    #send to RPI - irl
    global relay_control
    current_lights = db.get_lights()
    if light_id in current_lights:
        new_state = not current_lights[light_id]
        db.update_light_state(light_id, new_state)


        print(new_state , light_id)
        if new_state: relay_control.relay_on(light_id)
        if not new_state: relay_control.relay_off(light_id)

        return {light_id: new_state}
    else:
        raise HTTPException(status_code=404, detail="Light not found")

@app.get("/lights/{light_id}/on")
def turn_on_light(light_id: int):
    db.update_light_state(light_id, True)
    return {light_id: True}

@app.get("/lights/{light_id}/off")
def turn_off_light(light_id: int):
    db.update_light_state(light_id, False)
    return {light_id: False}


if __name__ == "__main__":
    uvicorn.run(app , host="0.0.0.0",port = 8000)
