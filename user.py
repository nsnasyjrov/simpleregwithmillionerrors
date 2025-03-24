import uuid

class User:
    def __init__(self):
        self.id = uuid.uuid4().__str__()
        self.username = None
        self.password = None
        self.location = None
        self.birthday = None

    def __repr__(self):
        return (f"User(id={self.id},"
                f"username={self.username},"
                f"location={self.location},"
                f"birthday={self.birthday})")