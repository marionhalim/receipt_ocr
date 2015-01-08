#!flask/bin/python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/healthCheck', methods=['GET'])
def healthCheck():
	return "Health Check OK"

#Input JSON 
# {"receipt": "[some file]"}
# Return JSON 
# {"receiptID" : "[unique identifier for the receipt]" , 
	# "userID": "[unique identifier of who posted it]", 
	# "vendor": "[vender of the transaction]",
	# "date" :"[date of transaction]", 
	# "totalCost" :"[cost]",
	# "items": {"name": "[name]", "cost": "[$$}"}, 
	# 		{"name": "[name]", "cost": "[$$}"}, 
	# 		{"name": "[name]", "cost": "[$$}"}, 
	# 		{"name": "[name]", "cost": "[$$}"}}
#

if __name__ == '__main__':
    app.run(debug=True)