# SimpleWebAPI
A simple web api built using flask and python for a tech challenge that can be deployed locally via Docker or on Heroku via Docker.

# Requirements to build:
- Docker

# Requirements to test locally:
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
 * Debugger PIN: ###-###-###
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

# API Endpoints
Root: / 
- Hello World!

Metadata: /info
- Returns information about the application.

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
- Procfile (Heroku CD)
- - This is a file used for deploying the application to Heroku which checks for updates on the master branch.  
- .travis.yml (Travis CI)
- - This is a file for Travis CI which checks for pushes to the repository and will test the application.
- - A sleep is included to allow the application to be deployed onto Heroku first.  
- - test.py will commence testing against the application deployed on Heroku.  


# Deployment Risks
- Travis CI is assuming that the build will be successfully pushed to Heroku and does not check if this is the case.
- - If Heroku did not rebuild and deploy the application for whatever reason, the tests from Travis CI would be deployed against the old build version on Heroku.
- - This would result in tests not being conducted on the current version of the build.  

# Application Risks
- Because the application does not use a database, there shouldn't be any need for sanitation or validation.
- Attempted directory traversal on variable endpoints and couldn't get the attack to work.
- - Using ../ only reverts the request back to the root endpoint. 
- - It doesn't appear that the application is vulnerable to directory traversal attacks, although I could definitely be wrong.  
- All data is accessible within the application - this assumes that all data *should* be accessible.

# Files 
api.py
- Used for running the Flask API.

Dockerfile
- Used for building the Docker container.

heroku.yml
- Configuration file for the Heroku app.

localTest.py
- Python script for testing the api locally against the local host.

Procfile
- Used for instructing Heroku app to deploy actions on app startup.

README.md
- A guide that will hopefully explain everything you need to know about this application.

requirements.txt
- A file used by Dockerfile to build the container.

test.py
- A testing script used to test against the Heroku app.

.travis.yml
- Used for kicking off Travis CI.

