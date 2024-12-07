class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

    def __contains__(self, item):
        if item in self.nickname:
            return True
        else:
            return False
