


class User:
    def __init__(self, username, password, age):
        self.username = username                  # definer Attributter
        self.password = password
        self.age = age
       

    def setUsername(self, username):
        self.username=username

    def getUsername(self):
        return self.username

    def setpassword(self, password):
        self.password=password

    def getpassword(self):
        return self.password