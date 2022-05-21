from flask import Flask, request, render_template, redirect
from user import User
from database import Database
import os

app = Flask(__name__)

    
MyDatabase = Database()



@app.route('/', methods=['GET', 'POST'])
def startside():
    return render_template('startside.html', LoggedIn = MyDatabase.getStatus())

@app.route('/logout')
def logout():
    MyDatabase.setStatus("False")
    MyDatabase.setUser(None)
    return render_template('logout.html', LoggedIn = MyDatabase.getStatus())



@app.route('/login', methods=['GET', 'POST'])
def login():
        error = None
        if request.method == 'POST':
            inputUsername = request.form['username']
            inputPassword = request.form['password']
            
            error = MyDatabase.credentialCheck(inputUsername, inputPassword)

            if error == None:
                MyDatabase.setUser(MyDatabase.findUser(inputUsername))
                MyDatabase.setStatus("True")
                return redirect('/profil')
            else:
                return render_template('loginform.html', error=error)

        return render_template('loginform.html', error=error)



@app.route('/profil', methods=['GET', 'POST'])
def Profile():
    error = None
    currentUser = MyDatabase.user
    navn = currentUser.getUsername()
    password = currentUser.getpassword()
    passwordlength = len(password)
    cryptpassword = "*"*int(passwordlength)
    
    if request.method == 'POST':
        if request.form['action'] == 'rediger':
            return render_template('profil.html', error = error, navn = navn, password = password, edit = True)
        if request.form['action'] == 'fortryd':
            return render_template('profil.html', error = error, navn = navn, password = cryptpassword, edit = False)
        if request.form['action'] == 'gem':
            nytnavn = request.form['username']
            nytpassword = request.form['password']
            nytpasswordrep = request.form['passwordrep']
            error = MyDatabase.Checkinput(nytnavn, nytpassword, nytpasswordrep)
            if error != None:
                return render_template('profil.html', error = error, navn = nytnavn, password = nytpassword, edit = True)
            else:
                MyDatabase.user.setUsername(nytnavn)
                MyDatabase.user.setpassword(nytpassword)
                MyDatabase.DeleteFile()
                userlist = MyDatabase.getDatabase()
                MyDatabase.saveFile(userlist)
                #MyDatabase.Users = MyDatabase.ReadFromFile()
                return render_template('profil.html', error = error, navn = MyDatabase.user.getUsername(), password = "*"*int(len(MyDatabase.user.getpassword())), edit=False)

    
    return render_template('profil.html', error = error, navn = navn, password = cryptpassword, edit = False)




@app.route('/NyBruger', methods=['GET', 'POST'])
def NyBruger():
    error = None
    if request.method == 'POST':
        brugernavn = request.form['username']
        password = request.form['password']
        passwordrep = request.form['passwordrep']

        error = MyDatabase.Checkinput(brugernavn, password, passwordrep)
        if error != None:
            return render_template('nybruger.html', error = error)
        else:
            NewUser= User(brugernavn, password)
            MyDatabase.setUser(NewUser)
            MyDatabase.addUser(NewUser)
            MyDatabase.setStatus("True")
            MyDatabase.WriteToFile([brugernavn, password])
            return redirect('/profil')
    return render_template('nybruger.html', error = error)



@app.route('/ekstraSide')
def extraPage():
    return ('Dette er en ekstra side der ikke er i brug nu')




if __name__ == "__main__":
    app.run() ## insert host='0.0.0.0', port=8000 in parentesen for at gøre den tilgængelig