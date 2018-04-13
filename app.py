import datetime

from flask import Flask
from flask_restful import  Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import userRegister

from resources.item import Item, ItemList

from resources.store import Store, StoreList

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)

# delete as required
# add expiry date/time to /auth register
#------------------------------------------------------------------------------

app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(days=7)

from flask import jsonify
import jwt as jwtx
import time

@jwt.auth_response_handler
def customized_response_handler(access_token, identity):
    #print('token 1 : ',access_token)

    decoded = jwtx.decode(jwt=access_token,key=app.secret_key)
    exp=decoded['exp']
    t=time.gmtime(exp)              # seconds to struct_time

    expt=time.asctime(t)            # struct time to string 'ddd mmm dd hh:mm:ss yyyy'

    return jsonify({    'access_token': access_token.decode('utf-8'),
                        'expiring ': expt
                   })

#-----------------------------------------------------------------------------


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(userRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')



if __name__ == "__main__":
    import os
    if 'WINGDB_ACTIVE' in os.environ:
        app.debug = False

    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
