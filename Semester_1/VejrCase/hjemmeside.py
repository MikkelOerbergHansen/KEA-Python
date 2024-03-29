# Vi importerer modulet Flask ind i vores Python fil
from flask import Flask, render_template
import csv

from matplotlib.axes import Axes
from ExcelReader import ExcelReader
from matplotlib import pyplot as plt
from Målinger import Måling
from VejrStation import VejrStation


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
            ' <a href="/Aalborg"><button>Aalborg</button></a>' + 
            ' <a href="/Grafer"><button>Se Grafer</button></a>'
            )

# Decorator for en route så den får adressen http://127.0.0.1:5000/København
@app.route('/København')

def København():
        ExcelFilData = ExcelReader()
        dataframe = ExcelFilData.prepareData("Semester_1/VejrCase/VejrDataKøbenhavn.csv")
        del dataframe[0]
      
        return( '<center><h1>København</h1></center> '
                '<br /><br /><a href="/Aalborg"><button>Se Aalborg</button></a>'
                ' <a href="/Odense"><button>Se Odense</button></a>'
                ' <a href="/Grafer"><button>Se Grafer</button></a>'
             '<br /><br /><a href="/"><button>Tilbage til forsiden</button></a>'
             '<br /><br />' + render_template('htmlTable.html', data = dataframe ))
             


# Decorator for en route så den får adressen http://127.0.0.1:5000/Odense
@app.route('/Odense')
def Odense():
        ExcelFilData = ExcelReader()
        dataframe = ExcelFilData.prepareData("Semester_1/VejrCase/VejrDataOdense.csv")
        del dataframe[0]

      
        return( '<center><h1>Odense</h1></center> '
                '<br /><br /><a href="/Aalborg"><button>Se Aalborg</button></a>'
                ' <a href="/København"><button>Se København</button></a>'
                ' <a href="/Grafer"><button>Se Grafer</button></a>'
             '<br /><br /><a href="/"><button>Tilbage til forsiden</button></a>'
             '<br /><br />' + render_template('htmlTable.html', data = dataframe ))          



# Decorator for en route så den får adressen http://127.0.0.1:5000/Aalborg
@app.route('/Aalborg')
def Aalborg():
        ExcelFilData = ExcelReader()
        dataframe = ExcelFilData.prepareData("Semester_1/VejrCase/VejrDataAalborg.csv")
        del dataframe[0]

        return( '<center><h1>Aalborg</h1></center> '
                '<br /><br /><a href="/Odense"><button>Se Odense</button></a>'
                ' <a href="/København"><button>Se København</button></a>'
                ' <a href="/Grafer"><button>Se Grafer</button></a>'
             '<br /><br /><a href="/"><button>Tilbage til forsiden</button></a>'
             '<br /><br />' + render_template('htmlTable.html', data = dataframe )) 



# Decorator for en route så den får adressen http://127.0.0.1:5000/Grafer
@app.route('/Grafer')
def Grafer():

        return( '<center><h1>Grafer</h1></center> '
                '<br /><br /><a href="/Odense"><button>Se Odense</button></a>'
                ' <a href="/København"><button>Se København</button></a>'
                ' <a href="/Aalborg"><button>Aalborg</button></a>'
                '<br /><br /><a href="/"><button>Tilbage til forsiden</button></a>'
                '<br /><br /><h2>Grafer for København</h2>'
                '<br /><br />' + render_template('plotKBH.html') +
                '<br /><br /><h2>Grafer for Odense</h2>'
                '<br /><br />' + render_template('plotOD.html') +
                '<br /><br /><h2>Grafer for Aalborg</h2>'
                '<br /><br />' + render_template('plotAA.html')) 





# til at køre koden direkte
if __name__== '__main__':
    app.run()