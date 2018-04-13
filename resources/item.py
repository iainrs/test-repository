
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.item import  ItemModel

class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help='This field cannot be left blank'
    )

    parser.add_argument('store_id',
        type=int,
        required=True,
        help='Every Item needs a store id'
    )


    @jwt_required()
    def get(self,name):

        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message' : 'Item not found'} , 404




    @jwt_required()
    def post(self,name):

        if ItemModel.find_by_name(name):
            return {'message':"an item with name '{}' already\
            exists".format(name)},400

        data = Item.parser.parse_args()
        #create item to be returned / save values
        item = ItemModel(name,data['price'],data['store_id'])

        item.save_to_db()

        return item.json(), 201

    @jwt_required()
    def delete(self,name):
        item=ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {'message' : " Item Deleted"}

        #if not ItemModel.find_by_name(name):
            #return {'message':"No item with name '{}' exists".format(name)},400

        #connection = sqlite3.connect('data.db')
        #cursor=connection.cursor()

        #query = "DELETE FROM items WHERE name = ? "
        ##print(query)

        #cursor.execute(query, (name,) )
        #connection.commit()
        #connection.close()

        #return {'message' : 'Item deleted' }

        #global items

        #if next(filter(lambda x: x['name'] == name,items),None):
            #items = list(filter(lambda x: x['name'] != name,items))
            #text = "'{}' deleted ".format(name)
        #else:
            #text = "'{}' does not exist".format(name)
        #return {'message': text}

    @jwt_required()
    def put(self,name):

        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)
        #create item to be returned / save values
        updated_item = ItemModel(name, data['price'])

        if item is None:

            item = ItemModel(name,data['price'],data['store_id'])
            # or            (name, **data)
            # add new
        else:

            item.price    = data['price']
            item.store_id = data['store_id']

        item.save_to_db()

        return item.json() , 201




class ItemList(Resource):

    def get(self):


        #connection = sqlite3.connect('data.db')
        #cursor=connection.cursor()
        #query = "SELECT * FROM items "
        #result = cursor.execute(query)

        #rows = result.fetchall()

        #connection.commit()
        #connection.close()
        #rv=[]
        #for row in rows:
            #rv.append({'id' : row[0],'name':row[1],'price':row[2]})

        return {'items' : [item.json() for item in ItemModel.query.all()] }

# map/lambda easier if other languages used
# or return {'items' : list(map(lambda x: x.json(), ItemModel.query.all()))}