from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

user_list = []


class HelloWorld(Resource):
    def get(self):
        return {"data": "Hello World Heroku!"}


class User(Resource):
    def get(self, username):
        """
        get user detail information
        """
        for user in user_list:
            if user["username"] == username:
                return user
        return {"message": "User not found"}, 404

    def post(self, username):
        """
        create a new user
        """
        password = request.json.get("password")
        print(password)
        if password:
            user = {"username": username, "password": password}
            user_list.append(user)
            return {"message": "User created"}, 201
        return {"message": "Password is required"}, 400

    def delete(self, username):
        """
        delete a user
        """
        user_find = None
        for user in user_list:
            if user["username"] == username:
                user_find = user
            if user_find:
                user_list.remove(user_find)
                return {"message": "User deleted"}
        return {"message": "User not found"}, 404

    def put(self, username):
        """
        update a user
        """
        # password = request.json.get("password")
        user_find = None
        for user in user_list:
            if user["username"] == username:
                user_find = user
        if user_find:
            user_list.remove(user_find)
            password = request.json.get("password")
            user_find["password"] = password
            user_list.append(user_find)
            return {"message": "User updated"}
        return {"message": "User not found"}, 404


api.add_resource(HelloWorld, "/")
api.add_resource(User, "/user/<string:username>")


if __name__ == "__main__":
    app.run()
