
from flask import Flask, request, jsonify
from flask.ext import restful
from flask.ext.restful import reqparse
import re
from requests import get, put, post, delete
from ocr import process_jpg_image

app = Flask(__name__) 
api = restful.Api(app)

class HealthCheck(restful.Resource):
    def get(self):
        return {'Health Check': 'OK'}, 200

class ocr(restful.Resource):
	def post(self): 
		parser = reqparse.RequestParser()
		parser.add_argument('url', type=inputs.url(), help='Enter a valid URL')
		args = parser.parse_args()
		return {'Test':'OK'}, 200

api.add_resource(HealthCheck, '/healthCheck')
api.add_resource(ocr, '/ocr')

"""
Input JSON: {"receipt": "[some file]"}
Return JSON: {"receiptID" : "[unique identifier for the receipt]" , 
				"userID": "[unique identifier of who posted it]", 
				"originalImage: "[original Image URL]",
				"vendor": "[vender of the transaction]",
				"date" :"[date of transaction]", 
				"totalCost" :"[cost]",
				"items": {"name": "[name]", "cost": "[$$}"}, 
					{"name": "[name]", "cost": "[$$}"}, 
					{"name": "[name]", "cost": "[$$}"}, 
					{"name": "[name]", "cost": "[$$}"}}
"""
@app.route('/ocr', methods=['POST'])
def ocr():
	if request.headers ['Content-Type'] == 'application/json': 
		url = request.json["receipt"]
		if 'jpg' in url: 
			output = process_image(url)
			items = []
			item = {'item': "",
				'cost': ""}
			items.append(item)
			return jsonify({"imageURL": url, 'vendor': "Costco", 
				"date": "01/08/2014", "totalCost" :"$200", "items": items}), 200
		else: 
		 	return 'Error: File not recognize as jpg or png', 400
	else:
		return 'Error: Content Type is not application/json', 400
