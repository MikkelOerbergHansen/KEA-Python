



# import af modulet Flask
from flask import Flask, request, render_template, redirect, session


app = Flask(__name__)


@app.route('/')
def startside():
    return render_template('index.html')



@app.route('/Ladestander')
def ladestander():
    return render_template('ladestandere.html')




# til at køre koden direkte
if __name__== '__main__':
    app.run()

