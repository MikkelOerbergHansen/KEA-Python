import sqlite3
import pandas as pd

from models.Repository import Repository

from flask import Flask, request, render_template, redirect


app = Flask(__name__)

rep = Repository()


@app.route("/")
def Kundesiden():
    return render_template('Kundesiden.html')



@app.route("/Kunde/")
def Kunde():
    return render_template('Kunde.html', data=rep.KundeObjekter)









if __name__ == '__main__':
    app.run()