class User:
    user_id = None
    name = None
    email = None

    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.urls = []

