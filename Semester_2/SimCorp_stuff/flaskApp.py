
# import af modulet Flask
from flask import Flask, request, render_template, redirect, session


app = Flask(__name__)


@app.route('/')
def startside():
    HeadLine = "SimCorp"
    return render_template('SimCorp.html', Headline = HeadLine)








# til at køre koden direkte
if __name__== '__main__':
    app.run()































