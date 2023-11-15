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

## If you run into "working outside of application context" error
If you run into this error, you can skip the python shell initialization and go straight to running the app with `python app.py` or `python3 app.py` if on mac or linux. Make sure to exit your python shell before running the python commands!

## If you run into "localhost access denied" error when navigating to localhost in the browser
Change the last line in app.py from `app.run(debug=True)` to `app.run(debug=True, port=8001)` re-run the app and navigate to `http://localhost:8001/`
