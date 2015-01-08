#!flask/bin/python
from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

#ALL ROUTES 
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
	print "HERE"
	if request.headers ['Content-Type'] == 'application/json': 
		#Run all the OCR stuff should just take an image URL 
		print "DERP"
		originalImage = request.json["receipt"]
		items = []
		item = {'item': "",
				'cost': ""}
		items.append(item)
		return jsonify({"originalImage": originalImage, 'vendor': "Costco", 
			"date": "01/08/2014", "totalCost" :"$200", "items": items}), 200


if __name__ == '__main__':
    app.run(debug=True)
