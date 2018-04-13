import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class userRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help='This field cannot be left blank'
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help='This field cannot be left blank'
    )


    def post(self):

        data = userRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message" : "User already registered"} , 400

        user = UserModel(data['username'], data['password'])

        user.save_to_db()

        #connection = sqlite3.connect('data.db')
        #cursor = connection.cursor()
        #connection.commit()

        #query = "INSERT INTO users Values (NULL, ? , ?)"
        #cursor.execute(query, (data['username'], data['password']))
        #connection.commit()
        #connection.close()
        #return user.json() , 200

        return {"message": "User created successfully"}, 201

