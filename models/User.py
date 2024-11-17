class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    @staticmethod
    def serialize(user):
        return {
            "id": str(user["_id"]),
            "name": user["name"],
            "email": user["email"],
            "password": user["password"],
        }
