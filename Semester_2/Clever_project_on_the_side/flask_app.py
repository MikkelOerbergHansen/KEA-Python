



# import af modulet Flask
from flask import Flask, request, render_template, redirect, session
from models.repository import Repository







myrep = Repository()
myrep.load_database()

#print(myrep.ladestanderList)



app = Flask(__name__)


@app.route('/')
def startside():
    return render_template('index.html')



@app.route('/Ladestander')
def ladestander():
    return render_template('ladestandere.html', data=myrep.ladestanderList)




# til at køre koden direkte
if __name__== '__main__':
    app.run()

