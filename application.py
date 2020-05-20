from flask import Flask
import json
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/routepost', methods = ['POST'])
def routepost():    
	data = request.get_json()
	print(data)
	return {'msg':'respuesta'}