
# import af modulet Flask
from flask import Flask, render_template

# konstruerer en variabel "app" som er af klassen Flask
app = Flask(__name__)

# En Decorator for en route
@app.route('/')
def startside():
    return render_template('Startside.html')



@app.route('/Bestilling')
# Definer en funktion for vores route der hedder hello_world()
def hello_world():
    return 'Hello, From Flask!' # funktionen returnerer en string med beskeden "Hello, from flask"


# til at køre koden direkte
if __name__== '__main__':
    app.run()