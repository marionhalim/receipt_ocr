from flask import Flask, request, jsonify, render_template
from flask.ext import restful
import re
from ocr import process_jpg_image

app = Flask(__name__) 
api = restful.Api(app)

class HealthCheck(restful.Resource):
    def get(self):
        return {'Health Check': 'OK'}

api.add_resource(HealthCheck, '/healthCheck')

@app.route('/')
def home():
  return render_template('home.html')
  
@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/healthCheck', methods=['GET'])
def healthCheck():
	return "Health Check OK"

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


if __name__ == '__main__':
    app.run(debug=True)

