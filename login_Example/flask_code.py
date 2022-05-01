from flask import Flask, request, render_template, redirect
from user import User
from database import Database

app = Flask(__name__)

    
MyDatabase = Database()



@app.route('/', methods=['GET', 'POST'])
def startside():
    return render_template('startside.html', LoggedIn = MyDatabase.getStatus())



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




@app.route('/profil')
def Profile():
    print(MyDatabase.getStatus())
    return render_template('profil.html')




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
    app.run()