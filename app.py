#!flask/bin/python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

#Input JSON 
# {"receipt": "[some file]"}
# Return JSON 
# {"receiptID" : "[unique identifier for the receipt]" , 
	# "userID": "[unique identifier of who posted it]", 
	# "date" :"[date of transaction]", 
	# "totalCost" :"[cost]",
	# "items": {"name": "[name]", "cost": "[$$}"}, 
	# 		{"name": "[name]", "cost": "[$$}"}, 
	# 		{"name": "[name]", "cost": "[$$}"}, 
	# 		{"name": "[name]", "cost": "[$$}"}}
#

if __name__ == '__main__':
    app.run(debug=True)