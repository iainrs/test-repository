import sqlite3
from db import db

# in models module

class UserModel(db.Model):
    __tablename__ = 'users'

    id       = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))


    def __init__(self,username,password):
        self.username = username
        self.password = password

    def save_to_db(self):
        # was insert()
        db.session.add(self)
        db.session.commit()


    #----------------------------------------------------------------------
    @classmethod
    def find_by_username(cls,username):

        return cls.query.filter_by(username=username).first()  #query = "SELECT * FROM items where name = ?"


        #try:
            #connection = sqlite3.connect('data.db')
            #cursor = connection.cursor()
            #query = 'SELECT * FROM users WHERE username = ?'
            #result= cursor.execute(query, (username,))
            #row = result.fetchone()
            #if row:
                ##create user object
                #user = cls(*row)
            #else:
                #user=None
            #connection.close()
        #except:
            #print('ERROR : in <find_by_username>')
        #return user

    @classmethod
    def find_by_id(cls,_id):

        return cls.query.filter_by(id=_id).first()  #query = "SELECT * FROM items where name = ?"

        #connection = sqlite3.connect('data.db')
        #cursor = connection.cursor()
        #query = 'SELECT * FROM users WHERE id = ?'
        #result= cursor.execute(query, (_id,))
        #row = result.fetchone()
        #if row:
            ##create user object
            #user = cls(*row)
        #else:
            #user=None
        #connection.commit()
        #connection.close()
        #return user
