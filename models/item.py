# import sqlite3
from db import db
class ItemModel(db.Model):
    __tablename__ = 'items'

    id       = db.Column(db.Integer, primary_key=True)

    name     = db.Column(db.String(80))
    price    = db.Column(db.Float(precision=2))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id') )
    store    = db.relationship('StoreModel')

    def __init__(self,name,price,store_id):
        self.name=name
        self.price=price
        self.store_id = store_id

    def json(self):
        return{'item' : self.name,'price': self.price,'Store_id': self.store_id}


    @ classmethod
    def find_by_name(cls,name):

        return cls.query.filter_by(name=name).first()  #query = "SELECT * FROM items where name = ?"


        #connection = sqlite3.connect('data.db')
        #cursor=connection.cursor()
        #query = "SELECT * FROM items where name = ?"
        #result = cursor.execute(query, (name,) )
        #row=result.fetchone()
        ## print(row)
        #connection.close()
        #if row:
            #return cls(row[0],row[1])
        ##   return(*row)



    def save_to_db(self):
        # was insert()
        db.session.add(self)
        db.session.commit()


        #connection = sqlite3.connect('data.db')
        #cursor=connection.cursor()

        #query = "INSERT into items  VALUES ( ?, ? )"

        #cursor.execute(query,(self.name,self.price))      #

        #connection.commit()
        #connection.close()
        #return self.json(), 201

    def delete_from_db(self):
        # was update()
        #
        db.session.delete(self)
        db.session.commit()


    #def update(self):

        #connection = sqlite3.connect('data.db')
        #cursor=connection.cursor()

        #query = "UPDATE items  SET price = ? WHERE name = ? "

        #cursor.execute(query,(self.price,self.name))      #

        #connection.commit()
        #connection.close()
        #return self.json(), 201

