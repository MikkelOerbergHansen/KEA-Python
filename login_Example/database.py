


class Database:
    def __init__(self):
        self.Users = []        # definer user liste
       

    def getDatabase(self):
        return self.Users

    
    def addUser(self, user):
        self.Users.append(user)

    def CheckPassword(self, input1, input2):
        if input1 != input2:
            return 'Invalid input. Please try again.'
        else:
            return None
