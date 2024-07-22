from flask import Flask, request
from flask_restful import Api, Resource

from rest_demo.resource.hello import HelloWorld
from rest_demo.resource.user import User, UserList


# class HelloWorld(Resource):
#     def get(self):
#         return {"data": "Hello World First Refactor123456!"}


app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, "/")
api.add_resource(User, "/user/<string:username>")
api.add_resource(UserList, "/users")


if __name__ == "__main__":
    app.run()
