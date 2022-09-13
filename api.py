from typing_extensions import Required
from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)

#app has 2 different endpoints
# 1. /locations
# 2. /users
users_path = './data/users.csv'

class Users(Resource):
    def get(self):
        data = pd.read_csv(users_path)
        data = data.to_dict()
        return {'data':data},200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('locationId', required=True, type=int,location='args')
        parser.add_argument('name', required=True, type=str,location='args')
        parser.add_argument('city', required=True, type=str,location='args')
        args = parser.parse_args()
        return { 
            'loc': args['locationId'],
            'name': args['name'],
            'city': args['city']
        },200

class Locations(Resource):
    pass

api.add_resource(Users,'/users')
api.add_resource(Locations,'/locations')


if __name__ == "__main__":
    app.run(debug=True)