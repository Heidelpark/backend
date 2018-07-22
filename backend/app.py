import random

from flask import Flask, jsonify, request
from flask_cors import CORS
from influxdb import InfluxDBClient

import models
from database import init_db, db_session

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
init_db()

influx_client = InfluxDBClient('localhost', 8086, 'heidelpark', 'heidelpark', 'heidelpark')
influx_client.create_database('heidelpark')


@app.route("/", methods=['GET'])
def hello():
    return ""


@app.route("/spots", methods=['GET', 'POST'])
def spot():
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
    data = request.get_json()
    res = influx_client.write_points(data)
    return res


@app.route("/parkingState", methods=['GET'])
def getCurrentSensorData():
    spots = []
    db_spots = models.Spot.query.all()
    for s in db_spots:
        spot = {
            "type": "Feature",
            "properties": {
                "id": s.name,
                "occupied": random.randint(0, 1)
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    float(s.lat),
                    float(s.lng)
                ]
            }
        }
        spots.append(spot)
    data = {
        "type": "FeatureCollection",
        "features": spots
    }
    return jsonify(data)


@app.route("/historyData", methods=['GET'])
def getHistoryData():
    pass


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')