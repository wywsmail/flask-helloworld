from flask_restful import Resource, reqparse


user_list = []


def min_length_str(min_length):
    def validate(s):
        print(type(s))
        if s is None:
            raise Exception("password required")
        if not isinstance(s, (int, str)):
            raise Exception("password format error")
        s = str(s)
        if len(s) >= min_length:
            return s
        raise Exception("String must be at least %i characters long" % min_length)

    return validate


class User(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        "password", type=min_length_str(5), required=True, help="{error_msg}"
    )
    parser.add_argument("email", type=str, required=False, help="{error_msg}")

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
        data = User.parser.parse_args()
        user = {
            "username": username,
            "password": data["password"],
            "email": data["email"],
        }
        for u in user_list:
            if u["username"] == username:
                return {"message": "User already exists"}, 400

        user_list.append(user)
        return {"message": "User created", "data": user}, 201

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
            data = User.parser.parse_args()
            user_list.remove(user_find)
            password = data["password"]
            email = data["email"]
            user_find["password"] = password
            user_find["email"] = email
            user_list.append(user_find)
            return {"message": "User updated"}
        return {"message": "User not found"}, 404


class UserList(Resource):
    def get(self):
        """
        get all users
        """

        return user_list
