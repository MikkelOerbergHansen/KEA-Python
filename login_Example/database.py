


class Database:
    def __init__(self):
        self.Users = []        # definer user liste
       

    def getDatabase(self):
        return self.Users

    
    def addUser(self, user):
        self.Users.append(user)