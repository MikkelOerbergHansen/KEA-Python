import csv


class Database:
    def __init__(self):
        self.Users = self.ReadFromFile()        # definer user liste
       

    def getDatabase(self):
        return self.Users
    
    def addUser(self, user):
        self.Users.append(user)

    def findUser(self, inputname):
        for user in self.Users:
            if user.getUsername() == inputname:
                return user
            else:
                return None

    def ReadFromFile(self):
        with open("login_Example/static/database.csv", "r") as f:
            reader = csv.reader(f)
            rows = []
            for row in reader:
                rows.append(row)
        return rows

    def WriteToFile(self, listofInfo):
        with open("login_Example/static/database.csv", 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(listofInfo)
        return None



### funktionen checker input fra bruger
### hvis yderligere krav eller input kommer så kan det tilføres her
    def Checkinput(self, username, password, passwordrep):
        if password != passwordrep:
            return 'password does not match. Please try again.'
        elif len(password) == 0 or password.isspace() == True:
            return "password cannot be empty"
        elif len(username) == 0 or username.isspace() == True:
            return "username cannot be empty"
        else:
            return None



