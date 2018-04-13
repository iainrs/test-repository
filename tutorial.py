from flask_sqlalchemy import sqlalchemy
print(sqlalchemy.__version__)
from sqlalchemy import create_engine
engine = create_engine('sqlite:///memory:', echo=True)
