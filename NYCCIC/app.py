import folium 
import numpy
import pandas as pd
from NYCCIC.NYCCIC import Data
from NYCCIC.NYCCIC import Map

from fastapi import FastAPI
import uvicorn
from fastapi.responses import HTMLResponse

# create the app as an instance of the fastAPI class
app = FastAPI()

# load the database once when the server starts

# create a root endpoint that provide basic information about the webapp
@app.get("/")
def root():
	return {"message": "go to /map to see the map"}

# create another endpoint for displaying the trend graph
#@app.get("/trend")

# create another endpoint for displaying the map 
# Just try out 
# Codes will be more refined later 
@app.get("/map", response_class=HTMLResponse)
def map():
	m = Map()
	m = m.map("percpos")
	return m._repr_html_()
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
