# BasicFlask

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