####
#### tværfaglig dag med systemudvikling
####



# import af modulet Flask
from flask import Flask, request, render_template, redirect, session


app = Flask(__name__)


@app.route('/')
def startside():
    return render_template('Startside.html')








# til at køre koden direkte
if __name__== '__main__':
    app.run()

