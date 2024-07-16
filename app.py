from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


# @app.route("/")
# def hello_world():
#     return "Hello World Heroku!"


class HelloWorld(Resource):
    def get(self):
        return {"data": "Hello World Heroku!"}


api.add_resource(HelloWorld, "/")

if __name__ == "__main__":
    app.run()
