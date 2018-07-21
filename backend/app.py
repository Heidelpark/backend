import json
from json import JSONEncoder

from flask import Flask, jsonify, request
import models
from database import init_db, db_session

app = Flask(__name__)

init_db()


@app.route("/", methods=['GET'])
def hello():
    #spots = models.Spot.query.all()
    return ""


@app.route("/sensor", methods=['GET', 'POST'])
def sensor():
    # create new sensor
    if request.method == 'POST':
        data = request.get_json()
        features = data.get("features")
        for f in features:
            name = f.get("properties").get("id")
            point = f.get("geometry").get("coordinates")
            spot = models.Spot(name=name, lat=point[0], lng=point[1])
            db_session.add(spot)
        db_session.commit()

    return "Sensor information"


@app.route("/sensorData", methods=['POST'])
def createSensorData():
    pass


@app.route("/currentData", methods=['GET'])
def getCurrentSensorData():
    pass


@app.route("/historyData", methods=['GET'])
def getHistoryData():
    pass
