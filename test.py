
from flask import Flask
from flask import render_template
app = Flask(__name__)

Pokemons =["Pikachu", "Charizard", "Squirtle"]


@app.route('/')
def index():
   return render_template("htmlTable.html", len = len(Pokemons), Pokemons = Pokemons) #if you want to render a .html file,
                        # import render_template from flask and use
                        #render_template("index.html") here.

if __name__ == '__main__':
    app.debug = True
    app.run() #go to http://127.0.0.1:5000/ to view the page.