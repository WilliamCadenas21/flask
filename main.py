from flask import Flask
from flask import request
import requests
import json
import time
import threading

UrlRFIDtoCompleteTheDiscount = 'http://127.0.0.1:8001/discountBalance'

app = Flask(__name__)

def processToBilling(dataOfTheTag):
	time.sleep(5)

	#TODO bank process the tag and the plate here and make the response
	

	request = requests.post(UrlRFIDtoCompleteTheDiscount, json={
		"msg":"payment accepted", 
		"plate":dataOfTheTag['plate'],
		"epc":dataOfTheTag['tag']}
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
	return {'msg':'this route is only for testing'}

@app.route('/billing', methods = ['POST'])
def billing():

	try:
		dictData = request.get_json()
		tag = dictData['tag']
		thread = threading.Thread(target=processToBilling, args=(dictData,))
		thread.start()
		print('start thread')
	except:
		return {'msg':'internal server error'}
	responseToSend = {'msg':'the proccess of billing has started in tag: '+tag}
	print('flask has sent this',responseToSend)
	return 	responseToSend

