import csv


class Database:
    def __init__(self):
        self.Users = []        # definer user liste
       

    def getDatabase(self):
        return self.Users
    
    def addUser(self, user):
        self.Users.append(user)

    def WriteToFile(self, listofInfo):
        with open("login_Example/static/database.csv", 'a') as f:
            writer = csv.writer(f)
            writer.writerow(listofInfo)
        return None

    def Checkinput(self, username, password, passwordrep):
        if password != passwordrep:
            return 'password does not match. Please try again.'
        elif username == " ":
            return "username cannot be empty"
        else:
            return None



