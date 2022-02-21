# import af modulet Flask
from flask import Flask

# Vi laver en variabel "app" som er en instantiering af klassen Flask
app = Flask(__name__)

# Definere class
class Car:
    # Definere attributer for en bil i min bilhandler
    def __init__(self, brand, model, color, onSale, marketPrice, sellingPrice, kmPerLiter):
        self.brand = brand
        self.model = model
        self.color = color
        self.onSale = onSale
        self.marketPrice = marketPrice
        self.sellingPrice = sellingPrice
        self.kmPerLiter = kmPerLiter

    # Getter metode for at få bilens brand
    def getBrand(self):
        return self.brand

    # Getter metode for at få bilens model
    def getModel(self):
        return self.model
    
    # Getter metode for at få bilens farve
    def getColor(self):
        return self.color
    
    # Getter metode for at få bilens markedspris
    def getMarketPrice(self):
        return str(self.marketPrice)

    # Definere metode for at udregne salgsbonusen for en bil
    ## oprindelige salesbonus var hhv. 800, 2000 og 2900 for car1, car2, car3
    def calculateSalesBonus(self):
        salesbonus = int((self.marketPrice - self.sellingPrice)*0.20)
        try:
            if salesbonus >= 2500:
                ExtraBonus = salesbonus + 500
                return str(ExtraBonus)
            elif salesbonus >= 2000:
                ExtraBonus = salesbonus + 1000
                return str(ExtraBonus)
            else:
                salesbonus = 0
                return str(salesbonus)
        except:
            return "Noget gik galt"
            
       


# Instantiere objekter af vores klasse Car
car1 = Car('Volkswagen', 'Golf', 'Grøn', True, 28000, 24000, 18.1)
car2 = Car('Toyota', 'Prius', 'Blå', False, 50000, 40000, 15.8)
car3 = Car('Ford', 'Mustang', 'Rød', False, 44500, 30000, 16.5)

# Decorator for en route så den får adressen http://127.0.0.1:5000/
@app.route('/')
# Definerer en funktion for vores route som hedder hello()
def index():
    # Vi returnerer HTML kode med en knap som linker til vores andre routes
    # <br /> er linjeskift i HTML
    # <a href="">    </a> er et link
    # <button>    </button> er en knap
    return  (
            'Velkommen til systemet for bilsælgere.<br /><br />'
            '<a href="/carOne"><button>Se bil 1</button></a>' +
            '<a href="/carTwo"><button>Se bil 2</button></a>' +
            '<a href="/carThree"><button>Se bil 3</button></a>'
            )

# Decorator for en route så den får adressen http://127.0.0.1:5000/carOne
@app.route('/carOne')
def carOne():
       return  (
            'Bilen af mærket ' + car1.getBrand() +
            ' i modellen ' + car1.getModel() +
            ' og farven ' + car1.getColor() +
            ' koster ' + car1.getMarketPrice() + ' kr. <br /><br />' + 
            'Salgsbonus for salg af bilen er ' + car1.calculateSalesBonus() + ' kr.'
            '<br /><br /><a href="/"><button>Tilbage</button></a>'
            )

# Decorator for en route så den får adressen http://127.0.0.1:5000/carTwo
@app.route('/carTwo')
def carTwo():
       return  (
            'Bilen af mærket ' + car2.getBrand() +
            ' i modellen ' + car2.getModel() +
            ' og farven ' + car2.getColor() +
            ' koster ' + car2.getMarketPrice() + ' kr. <br /><br />' + 
            'Salgsbonus for salg af bilen er ' + car2.calculateSalesBonus() + ' kr.'
            '<br /><br /><a href="/"><button>Tilbage</button></a>'
            )

# Decorator for en route så den får adressen http://127.0.0.1:5000/carThree
@app.route('/carThree')
def carThree():
       return  (
            'Bilen af mærket ' + car3.getBrand() +
            ' i modellen ' + car3.getModel() +
            ' og farven ' + car3.getColor() +
            ' koster ' + car3.getMarketPrice() + ' kr. <br /><br />' + 
            'Salgsbonus for salg af bilen er ' + car3.calculateSalesBonus() + ' kr.'
            '<br /><br /><a href="/"><button>Tilbage</button></a>'
            )



# til at køre koden direkte
if __name__== '__main__':
    app.run()