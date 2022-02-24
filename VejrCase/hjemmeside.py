# Vi importerer modulet Flask ind i vores Python fil
from flask import Flask, render_template
import csv
from ExcelReader import ExcelReader


# Vi laver en variabel "app" som er en instantiering af klassen Flask
app = Flask(__name__)

# Decorator for en route så den får adressen http://127.0.0.1:5000/
@app.route('/')
# Definerer en funktion for vores route som hedder forside
def index():


    # Vi returnerer HTML kode med en knap som linker til vores andre routes
    # <br /> er linjeskift i HTML
    # <a href="">    </a> er et link
    # <button>    </button> er en knap
        return(
            '<h2>Velkommen til vejrdata</h2><br /><br />'
            'Tryk på en af byerne for at se vejret i byen.<br /><br />'
            '<a href="/København"><button>København</button></a>' +
            ' <a href="/Odense"><button>Odense</button></a>' +
            ' <a href="/Aalborg"><button>Aalborg</button></a>'
            )

# Decorator for en route så den får adressen http://127.0.0.1:5000/København
@app.route('/København')

def København():
        ExcelFilData = ExcelReader()
        dataframe = ExcelFilData.prepareData("VejrCase/VejrDataKøbenhavn.csv")
        del dataframe[0]
      
        return( '<center><h2>København</h2></center> '
                '<br /><br /><a href="/Aalborg"><button>Se Aalborg</button></a>'
                ' <a href="/Odense"><button>Se Odense</button></a>'
             '<br /><br /><a href="/"><button>Tilbage til forsiden</button></a>'
             '<br /><br />' + render_template('htmlTable.html', data = dataframe ))
             


# Decorator for en route så den får adressen http://127.0.0.1:5000/Odense
@app.route('/Odense')
def Odense():
        ExcelFilData = ExcelReader()
        dataframe = ExcelFilData.prepareData("VejrCase/VejrDataOdense.csv")
        del dataframe[0]

      
        return( '<center><h2>Odense</h2></center> '
                '<br /><br /><a href="/Aalborg"><button>Se Aalborg</button></a>'
                ' <a href="/København"><button>Se København</button></a>'
             '<br /><br /><a href="/"><button>Tilbage til forsiden</button></a>'
             '<br /><br />' + render_template('htmlTable.html', data = dataframe ))          



# Decorator for en route så den får adressen http://127.0.0.1:5000/Aalborg
@app.route('/Aalborg')
def Aalborg():
        ExcelFilData = ExcelReader()
        dataframe = ExcelFilData.prepareData("VejrCase/VejrDataAalborg.csv")
        del dataframe[0]

        return( '<center><h2>Aalborg</h2></center> '
                '<br /><br /><a href="/Odense"><button>Se Odense</button></a>'
                ' <a href="/København"><button>Se København</button></a>'
             '<br /><br /><a href="/"><button>Tilbage til forsiden</button></a>'
             '<br /><br />' + render_template('htmlTable.html', data = dataframe )) 

# til at køre koden direkte
if __name__== '__main__':
    app.run()