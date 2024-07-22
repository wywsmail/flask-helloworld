from flask import Flask, request
from flask_restful import Api

from .resource.hello import HelloWorld
from .resource.user import User, UserList

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, "/")
api.add_resource(User, "/user/<string:username>")
api.add_resource(UserList, "/users")


if __name__ == "__main__":
    app.run()
