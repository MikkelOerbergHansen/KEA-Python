from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
        error = None
        if request.method == 'POST':
            if request.form['username'] != 'admin' or request.form['password'] != 'admin':
                error = 'Invalid Credentials. Please try again.'
            else:
                return redirect('/startside')
        return render_template('my-form.html', error=error)




@app.route('/startside')
def Profile():
    return ('dette er en startside efter succesfuldt log in')

@app.route('/NyBruger')
def NyBruger():
    return ('Ny Bruger')



@app.route('/salesPage')
def salesPage():
    return ('welcome to the shopping page')




if __name__ == "__main__":
    app.run()