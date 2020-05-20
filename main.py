from flask import Flask
from flask import request
import requests
import json
import time
import threading

UrlRFIDtoCompleteTheDiscount = 'http://127.0.0.1:8001/discountBalance'

app = Flask(__name__)

def processToBilling(dataOfTheTag):
	time.sleep(7)

	#TODO bank process the tag and the plate here and make the response
	

	request = requests.post(UrlRFIDtoCompleteTheDiscount, json={
		"msg":"payment accepted", 
		"plate":dataOfTheTag['tag'],
		"epc":dataOfTheTag['plate']}
	)
	objResponseJson = request.json()
	print(objResponseJson)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/routepost', methods = ['POST'])
def routepost():    
	data = request.get_json()
	print(data)
	return {'msg':'esta ruta está funcionando correctamente'}



	

@app.route('/billing', methods = ['POST'])
def billing():

	#try:
	dictResponse = request.get_json()
	plate = dictResponse['plate']
	thread = threading.Thread(target=processToBilling, args=(dictResponse,))
	thread.start()
	print('start thread')
	#except:.
	#	return {'msg':'hubo un problema manejando la repuesta del lado del servidor'}

	return {'msg':'El procesos de cobro se ha inicializado para la placa vehicular #'+plate}	

