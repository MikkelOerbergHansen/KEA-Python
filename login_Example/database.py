


class Database:
    def __init__(self):
        self.Users = []        # definer user liste
       

    def getDatabase(self):
        return self.Users
    
    def addUser(self, user):
        self.Users.append(user)

    def Checkinput(self, username, password, passwordrep):
        if password != passwordrep:
            return 'password does not match. Please try again.'
        elif username == " ":
            return "username cannot be empty"
        else:
            return None
