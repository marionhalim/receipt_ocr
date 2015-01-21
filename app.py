from flask import Flask, request, render_template

app = Flask(__name__) 
api = restful.Api(app)

class HealthCheck(restful.Resource):
    def get(self):
        return {'Health Check': 'OK'}, 200

api.add_resource(HealthCheck, '/healthCheck')

@app.route('/')
def home():
  return render_template('home.html')
  
@app.route('/about')
def about():
  return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)

