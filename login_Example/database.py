import csv

from user import User
import os

class Database:
    def __init__(self):
        self.Users = self.ReadFromFile()        # definer user liste
        self.status = "False"
        self.user = None
       

    def getDatabase(self):
        return self.Users

    def getUser(self):
        return self.user

    def setUser(self, user):
        self.user = user

    def setStatus(self, status):
        self.status = status
    
    def getStatus(self):
        return self.status
    
    def addUser(self, user):
        self.Users.append(user)

    def findUser(self, inputname):
        for user in self.Users:
            if user.getUsername() == inputname:
                myuser = user
                return myuser
            else:
                myuser = None
        return myuser

    def ReadFromFile(self):
        with open("login_Example/static/database.csv", "r") as f:
            reader = csv.reader(f)
            rows = []
            for row in reader:
                rows.append(row)
            users= []
            for row in rows:
                user= User(row[0], row[1])
                users.append(user)
        return users

    def WriteToFile(self, listofInfo):
        with open("login_Example/static/database.csv", 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(listofInfo)
        return None

    def DeleteFile(self):
        file = "login_Example/static/database.csv"
        if(os.path.exists(file) and os.path.isfile(file)):
            os.remove(file)
        return None

    def saveFile(self, userlist):
        with open("login_Example/static/database.csv", 'w', newline='') as f:
            writer = csv.writer(f)
            for user in userlist:
                writer.writerow([user.getUsername(), user.getpassword()])
        return None

    def credentialCheck(self, inputname, inputpassword):
        for user in self.Users:
            if user.username == inputname and user.password == inputpassword:
                error = None
                return error
            else:
                error = 'Invalid Credentials. Please try again.'
        return error


### funktionen checker input fra bruger
### hvis yderligere krav eller input kommer så kan det tilføres her
    def Checkinput(self, username, password, passwordrep):
        if password != passwordrep:
            return 'password does not match. Please try again.'
        elif len(password) == 0 or password.isspace() == True:
            return "password cannot be empty"
        elif len(username) == 0 or username.isspace() == True:
            return "username cannot be empty"
        elif self.findUser(username) != None:
            return "User already exist"
        else:
            return None



