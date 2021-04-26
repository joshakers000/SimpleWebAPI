# SimpleWebAPI
A simple web api built using flask and python for a tech challenge that can be deployed locally via Docker or on Heroku via Docker.

# Requirements:
- Docker
- pip3
- Python3
- chardet2
- urllib3
- requests



# Docker Deployment
```
sudo docker build -t flask-api:latest .
sudo docker run -i -p 5000:5000 flask-api
```
Anticipated output:
```
* Serving Flask app "api" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 181-356-883
```
If you see this, the api should be running!

# Local Test
Open new terminal window (DO NOT CLOSE TERMINAL WINDOW WITH API RUNNING) and navigate to cloned repository
```
python3 localTest.py
```
Anticipated output:
```
1
1
1
```
If any of the output is a zero, this means a test has failed.

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


# Heroku
App is currently deployed and running at https://web-api000.herokuapp.com/
- Query app on heroku
``` https://web-api000.herokuapp.com<endpoint> ```

# Local Queries
``` curl http://127.0.0.1:5000<endpoint> ```


# Pipleline Functionality
- Procfile
- - This is a file used for deploying the application to Heroku which checks for updates on the master branch.  
- .travis.yml
- - This is a file for Travis CI which checks for pushes to the repository and will build out the application.
- - A sleep is included to allow the application to be deployed onto Heroku first.  
- - test.py will commence testing against the application deployed on Heroku.  
