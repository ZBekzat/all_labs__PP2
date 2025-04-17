class Users:
    def __init__(self, id, username, level):
        self.id = id
        self.username = username
        self.level = level

    def __repr__(self):
        return f"id={self.id}, username='{self.username}', level={self.level})"