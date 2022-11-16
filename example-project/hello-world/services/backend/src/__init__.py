from flask import Flask
from flask_cors import CORS
from flask_restx import Resource, Api
from flask_pymongo import PyMongo
from pymongo.collection import Collection
from .model import Company
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
# Get a reference to the companies collection.
companies: Collection = pymongo.db.companies
attractions: Collection = pymongo.db.attractions
airbnbs: Collection = pymongo.db.airbnbs

api = Api(app)


class CompaniesList(Resource):
    def get(self, args=None):
        # retrieve the arguments and convert to a dict
        args = request.args.to_dict()
        print(args)
        # If the user specified category is "All" we retrieve all companies
        if args['category'] == 'All':
            cursor = companies.find()
        # In any other case, we only return the companies where the category applies
        else:
            cursor = companies.find(args)
        # we return all companies as json
        return [Company(**doc).to_json() for doc in cursor]


class Companies(Resource):
    def get(self, id):
        cursor = companies.find_one_or_404({"id": id})
        company = Company(**cursor)
        # do preprocessing, machine learning etc.
        return company.to_json()


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


api.add_resource(CompaniesList, '/companies')
api.add_resource(Companies, '/companies/<int:id>')
api.add_resource(Attractions, '/attractions')
api.add_resource(Airbnbs, '/airbnbs')
