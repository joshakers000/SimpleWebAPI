import flask
import requests
from flask import request, jsonify
import os
port = int(os.environ.get("PORT", 5000))


app = flask.Flask(__name__)
app.config["DEBUG"] = True


#Add json object
shapes = [
	{'id': 0,
     'type': 'Rectangle',
     'sides': '4'},
    {'id': 1,
     'type': 'Square',
     'sides': '4'},
    {'id': 2,
     'type': 'Triangle',
     'sides': '3'}

		]


@app.route('/', methods=['GET'])
def home():
	return "<h1> Hello World! <h1>"


@app.route('/api/resources/shapes/all', methods=['GET'])
def api_all():
	return jsonify(shapes)

@app.route('/api/resources/shapes', methods=['GET'])
def api_id():
	if 'id' in request.args:
		id = int(request.args['id'])
	else:
		return "Error: No id field provided.  Please specify an id."

	results = []

	for shape in shapes:
		if shape['id'] == id:
			results.append(shape)


	return jsonify(results)


@app.route('/healthcheck', methods=['GET'])
def api_healthcheck():
	#Check healthy

	#This is not how this would normally be done.
	if 'url' in request.args:
		url = request.args['url']
	else:
		return "Error: No url field provided.  Please provide a url to check health."
	return str(requests.get('http://127.0.0.1:' + port + '/' + url).status_code)
	

app.run(threaded=True, host="0.0.0.0", port=port)
