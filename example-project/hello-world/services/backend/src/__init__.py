from flask import Flask
from flask_cors import CORS
from flask_restx import Resource, Api
from flask_pymongo import PyMongo
from pymongo.collection import Collection
from .model import Attraction
from .model import Airbnb
from flask import request

# Configure Flask & Flask-PyMongo:
app = Flask(__name__)

# allow access from any frontend
cors = CORS()
cors.init_app(app, resources={r"*": {"origins": "*"}})

# add your mongodb URI
app.config["MONGO_URI"] = "mongodb://localhost:27017/companiesdatabase"
pymongo = PyMongo(app)

# Get a reference to the airbnbs and attractions collection.
attractions: Collection = pymongo.db.attractions
airbnbs: Collection = pymongo.db.airbnbs

api = Api(app)


class Attractions(Resource):
    def get(self, args=None):
        args = request.args.to_dict()
        cursor = attractions.find()
        return [Attraction(**doc).to_json() for doc in cursor]


class Airbnbs(Resource):
    def get(self, args=None):
        args = request.args.to_dict()
        cursor = airbnbs.find()
        return [Airbnb(**doc).to_json() for doc in cursor]

api.add_resource(Attractions, '/attractions')
api.add_resource(Airbnbs, '/airbnbs')
