# Vi importerer modulet Flask ind i vores Python fil
from flask import Flask
import csv
from ExcelReader import ExcelReader
from VejrStation import VejrStation
from Målinger import Måling

# Vi laver en variabel "app" som er en instantiering af klassen Flask
app = Flask(__name__)

# Decorator for en route så den får adressen http://127.0.0.1:5000/
@app.route('/')
# Definerer en funktion for vores route som hedder forside
def index():

        ExcelFilData = ExcelReader()
        dataframe = ExcelFilData.prepareData("VejrCase/VejrDataKøbenhavn.csv")

        ###
        ### datasættet skal konverteres til en liste af målinger
        ### som kan bruges ved oprettelse af vejrstationer
        ### 

        MålingerKBH =[]
        for i in range(1, len(dataframe)):
            MålingerKBH.append(Måling(dataframe[i][0],dataframe[i][1],dataframe[i][2],dataframe[i][3],dataframe[i][4], dataframe[i][5]))

        # Vi gentager for datasættet for hhv. Aalborg og odense
        dataframe = ExcelFilData.prepareData("VejrCase/VejrDataAalborg.csv")

        MålingerAA =[]
        for i in range(1, len(dataframe)):
            MålingerAA.append(Måling(dataframe[i][0],dataframe[i][1],dataframe[i][2],dataframe[i][3],dataframe[i][4], dataframe[i][5]))

        dataframe = ExcelFilData.prepareData("VejrCase/VejrDataOdense.csv")

        MålingerOD = []
        for i in range(1, len(dataframe)):
            MålingerOD.append(Måling(dataframe[i][0],dataframe[i][1],dataframe[i][2],dataframe[i][3],dataframe[i][4], dataframe[i][5]))

        ### vi kan nu oprette tre vejrstations objekter

        vejrStation1 = VejrStation("København", "København C", "DK", MålingerKBH)
        vejrStation2 = VejrStation("Odense", "Odense C", "DK", MålingerOD)
        vejrStation3 = VejrStation("Aalborg", "Aalborg C", "DK", MålingerAA)

    # Vi returnerer HTML kode med en knap som linker til vores andre routes
    # <br /> er linjeskift i HTML
    # <a href="">    </a> er et link
    # <button>    </button> er en knap
        return(
            'Velkommen til vejrdata.<br /><br />'
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

        MålingerKBH =[]
        for i in range(1, len(dataframe)):
            MålingerKBH.append(Måling(dataframe[i][0],dataframe[i][1],dataframe[i][2],dataframe[i][3],dataframe[i][4], dataframe[i][5]))
        
        vejrStation1 = VejrStation("København", "København C", "DK", MålingerKBH)


        return( 'Vejret i København er '
                '<br /><br /><a href="/KøbenhavnSenesteDøgn"><button>Se København Seneste Døgn</button></a>'
                '<br /><br /><a href="/Aalborg"><button>Se Aalborg</button></a>'
                ' <a href="/Odense"><button>Se Odense</button></a>'
             '<br /><br /><a href="/"><button>Tilbage til forsiden</button></a>'
             '<br /><br />' + vejrStation1.PrintData2(10,1400) )
       
@app.route('/KøbenhavnSenesteDøgn')
def KøbenhavnSenesteDøgn():
        return( 'Vejret i København det seneste døgn er '
             '<br /><br /><a href="/"><button>Tilbage til forsiden</button></a>' )       


# Decorator for en route så den får adressen http://127.0.0.1:5000/Odense
@app.route('/Odense')
def Odense():
       return( 'Vejret i Odense er '
            '<br /><br /><a href="/OdenseSenesteDøgn"><button>Se Odense Seneste Døgn</button></a>'
            '<br /><br /><a href="/København"><button>Se København</button></a>'
            ' <a href="/Aalborg"><button>Se Aalborg</button></a>'
           '<br /><br /><a href="/"><button>Tilbage til forsiden</button></a>' )           

@app.route('/OdenseSenesteDøgn')
def OdenseSenesteDøgn():
        return( 'Vejret i Odense det seneste døgn er '
             '<br /><br /><a href="/"><button>Tilbage til forsiden</button></a>' )

# Decorator for en route så den får adressen http://127.0.0.1:5000/Aalborg
@app.route('/Aalborg')
def Aalborg():
       return( 'Vejret i Aalborg er '
            '<br /><br /><a href="/AalborgSenesteDøgn"><button>Se Aalborg Seneste Døgn</button></a>'
            '<br /><br /><a href="/København"><button>Se København</button></a>'
            ' <a href="/Odense"><button>Se Odense</button></a>'
           '<br /><br /><a href="/"><button>Tilbage til forsiden</button></a>' )

@app.route('/AalborgSenesteDøgn')
def AalborgSenesteDøgn():
        return( 'Vejret i Aalborg det seneste døgn er '
             '<br /><br /><a href="/"><button>Tilbage til forsiden</button></a>' )

# til at køre koden direkte
if __name__== '__main__':
    app.run()