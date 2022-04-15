from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


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

@app.route('/NyBruger')
def NyBruger():
    return render_template('nybruger.html')



@app.route('/ekstraSide')
def salesPage():
    return ('Dette er en ekstra side der ikke er i brug nu')




if __name__ == "__main__":
    app.run()