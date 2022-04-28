


class User:
    def __init__(self, username, password ):
        self.username = username                  # definer Attributter
        self.password = password
       

    def setUsername(self, username):
        self.username=username

    def getUsername(self):
        return self.username

    def setpassword(self, password):
        self.password=password

    def getpassword(self):
        return self.password