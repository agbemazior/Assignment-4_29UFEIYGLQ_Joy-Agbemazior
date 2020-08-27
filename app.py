from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/covid-19')
def tracker():
    data = dict(
        total = 44000,
        active = 1000,
        disch = 40000,
        deaths = 200,
        ncases = 543,
    )
    return jsonify(data)