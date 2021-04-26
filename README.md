# SimpleWebAPI
A simple web api built using flask and python for a tech challenge.


# Docker Deployment
```
sudo docker build -t flask-api:latest .
sudo docker run -i -p 5000:5000 flask-api
```
Open new terminal window and navigate to cloned repository
```
python3 localTest.py
```
Anticipated output:
```
1
1
1
```

# Endpoints
Root: / 
- Hello World!

Shapes: /api/resources/shapes/all
- Returns all shapes.

Shape: /api/resources/shapes?id=
- Obtain a specific shape based on id#
- Example: curl http://127.0.0.1:5000/api/resources/shapes?id=2
```
  [
    {
      "id": 2, 
      "sides": "3", 
      "type": "Triangle"
    }

  ]
```
Healthy: /healthcheck?url=
- Can check any URL within the application and it will return the proper status code.
