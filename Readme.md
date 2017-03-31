# Submitter
Varun Sondhi

+1 (416) 275-1876

sondhi.varun@gmail.com

# Prerequisites
1. Python 2.7
2. virtualenv 15.1.0

# Installation
1. Navigate to desired directory and create virtual environment
```
virtualenv juice_challenge
```
2. Copy content of project's zip file into this folder
3. Install all required libraries
```
pip install -r py_requirements.txt
```
4. Start the Project. Note - will require port 8080 to be available on your machine
```
python main.py
```

# Questions
## Provide a list of decisions you have made during this challenge. Are you proud of these decisions and why?
1. How to implement the project in simpler yet effective manner: I decided to go with cherrypy as webserver and write front end code in AngularJS, becuase I believe that with this combination it will be simplest to achieve the desired goal.
2. Not to store csv file to disk: This made the application perform better
## Were you following any best practices?
I try to follow below best practices in most of the projects that I work on.
1. Create a readable code
2. Implement OOPS concepts for understanding and maintainability.
3. Run the code through tools like pylint and try bring the code to highest standards.
## What would you have done differently?
I could have
1. Implemented test cases to run the application through various scenarios to ensure that backend is rock solid.
2. I believe the UI is usable as such, but I could have added few fancy alerts and fancy animations in case it was a public facing application. 
