from flask import Flask, request, render_template, redirect
from user import User
from database import Database

app = Flask(__name__)

MyDatabase = Database()
currentUser = None
loggedIN = None


@app.route('/')
def startside():
    return render_template('startside.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
        error = None
        if request.method == 'POST':
            if request.form['username'] != 'admin' or request.form['password'] != 'admin':
                error = 'Invalid Credentials. Please try again.'
            else:
                return redirect('/profil')
        return render_template('loginform.html', error=error)




@app.route('/profil')
def Profile():
    return ('dette er en profilside efter succesfuldt log in')




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
            currentUser = NewUser
            MyDatabase.addUser(currentUser)
            loggedIN = True
            MyDatabase.WriteToFile([brugernavn, password])
            return redirect('/profil')
    return render_template('nybruger.html', error = error)



@app.route('/ekstraSide')
def extraPage():
    return ('Dette er en ekstra side der ikke er i brug nu')




if __name__ == "__main__":
    app.run()