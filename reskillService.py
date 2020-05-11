from flask import Flask
from flask_restful import Resource, Api
import os
import requests

app = Flask(__name__)
api = Api(app)

endPoints = [
	{
		"city list" : "city",
	},
	{
		"country list" : "country",
	}
]

countryList = [
	{
		"name": "India"
	},
	{
		"name": "England"
	},
	{
		"name": "USA",
	},
	{
		"name": "France"
	},
	{
		"WHO_AM_I": os.environ["HOSTNAME"]
	}
]

cityList = [
	{
		"name": "Mumbai"
	},
	{
		"name": "London"
	},
	{
		"name": "Newyork",
	},
	{
		"WHO_AM_I": os.environ["HOSTNAME"]
	},
]

class Home(Resource):
	def get(self):
		return {"Home", home}, 200

class EndPoints(Resource):
	def get(self):
		return { "endpoints": endPoints }, 200

class CityList(Resource):
	def get(self):
		return { "citylist": cityList }, 200

class CountryList(Resource):
	def get(self):
		return { "citylist": countryList }, 200

api.add_resource(EndPoints, '/endpoints')
api.add_resource(CityList, '/city')
api.add_resource(CountryList, '/country')

if __name__ == '__main__':
    app.run(port=5000,debug=True, host='0.0.0.0')
