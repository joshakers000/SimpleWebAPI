#test.py
import requests


#vars
home = "https://web-api000.herokuapp.com/"
health = home + "healthcheck?"
#Test 1, health check something that works
def healthtests():
	#Test for error message
	if "Error: No url field provided.  Please provide a url to check health." in str(requests.get(health + "urg=hiu").content):
		pass
	else:
		return 0

	#Test for 404 page not found.
	if "404" in str(requests.get(health + "url=g").content):
		pass
	else:
		return 0

	#Test for 200, status okay.
	if requests.get(health + "url=").status_code == 200:
		return 1
	else:
		return 0

def RootEndpointCheck():
	#Make sure rootendpoint is reachable and contains correct data
	if "Hello World!" in str(requests.get(home).content):
		return 1
	else:
		return 0

def shapeIdChecks():
	#ID 0
	try:
		shape = requests.get(home + "api/resources/shapes?id=0").json()[0]
	except:
		return 0

	if shape["id"] == 0:
		pass
	else:
		return 0

	#ID 2
	try:
		shape = requests.get(home + "api/resources/shapes?id=2").json()[0]
	except:
		return 0
	if shape["id"] == 2:
		pass
	else:
		return 0

	#ID -1
	try:
		shape = requests.get(home + "api/resources/shapes?id=-1").json()[0]
		return 0
	except:
		pass

	#ID 4
	try:
		shape = requests.get(home + "api/resources/shapes?id=4").json()[0]
		return 0
	except:
		return 1


print(healthtests())
print(RootEndpointCheck())
print(shapeIdChecks())

