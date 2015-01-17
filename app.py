from flask import Flask, request, jsonify
import re
from ocr import process_image

app = Flask(__name__) 

@app.route('/index') 
def index(): 
	return 'OK'

@app.route('/healthCheck', methods=['GET'])
def healthCheck():
	return "Health Check OK"

#Input JSON 
# {"receipt": "[some file]"}
# Return JSON 
# {"receiptID" : "[unique identifier for the receipt]" , 
	# "userID": "[unique identifier of who posted it]", 
	# "originalImage: "[original Image URL]",
	# "vendor": "[vender of the transaction]",
	# "date" :"[date of transaction]", 
	# "totalCost" :"[cost]",
	# "items": {"name": "[name]", "cost": "[$$}"}, 
	# 		{"name": "[name]", "cost": "[$$}"}, 
	# 		{"name": "[name]", "cost": "[$$}"}, 
	# 		{"name": "[name]", "cost": "[$$}"}}
#
@app.route('/ocr', methods=['POST'])
def ocr():
	if request.headers ['Content-Type'] == 'application/json': 
		url = request.json["receipt"]
		
		if 'jpg' | 'png' in url: 
			output = process_image(url)
			items = []
			item = {'item': "",
				'cost': ""}
			items.append(item)
			return jsonify({"originalImage": originalImage, 'vendor': "Costco", 
				"date": "01/08/2014", "totalCost" :"$200", "items": items}), 200
		else: 
		 	return 'Error: File not recognize as jpg or png', 400
	else:
		return 'Error: Content Type is not application/json', 400



if __name__ == '__main__':
    app.run(debug=True)

