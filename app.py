from flask import Flask
from flask_restful import Api

# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate


# db = SQLAlchemy()

from restdemo.resource.hello import HelloWorld
from restdemo.resource.user import User, UserList


# from .restdemo.model.user import User as UserModel


# def create_app():
#     app = Flask(__name__)
#     api = Api(app)
#     # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///demo.db"

#     # db.init_app(app)
#     # migrate = Migrate(app, db)

#     api.add_resource(HelloWorld, "/")
#     api.add_resource(User, "/user/<string:username>")
#     api.add_resource(UserList, "/users")
#     return app


app = Flask(__name__)
api = Api(app)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///demo.db"

# db.init_app(app)
# migrate = Migrate(app, db)

api.add_resource(HelloWorld, "/")
api.add_resource(User, "/user/<string:username>")
api.add_resource(UserList, "/users")


if __name__ == "__main__":
    # app = create_app()
    app.run()
