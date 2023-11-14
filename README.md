# BasicFlask

## What is this project?
This project is a simple todo application, built in python using Flask for the api code, and Jinja for the web page. This project was made for me to take a quick dive into the Flask framework!

[Read more about Flask here!](https://github.com/pallets/flask)


## Using venv for environment management

steps to setup!

*use pip3 on mac and linux*
```
pip install virtualenv
virtualenv env

source env/bin/activate

or on windows:
source \env\Scripts\activate.bat

pip install flask flask-sqlalchemy
```

## to initialize database, start python shell and run
```
from app import db
db.create_all()
exit()
```

## To run the app after all is set up run 
`python app.py`
then in a web browser navigate to http://localhost:5000/