
# import af modulet Flask
from flask import Flask, request, render_template, redirect, session
from MenuKort import MenuKort
import itertools

# konstruerer en variabel "app" som er af klassen Flask
app = Flask(__name__)
Menu = MenuKort()
Menu.AddPizza("Margherita",["Tomat", "Ost"], 69)
Menu.AddPizza("Vesuvio",["Tomat", "Ost","skinke"], 75)
Menu.AddPizza("Capricciosa",["Tomat", "Ost","skinke", "champignon"], 80)
Menu.AddPizza("Calzone",["Tomat", "Ost","skinke", "champignon"], 80)
Menu.AddPizza("Quattro Stagioni",["Tomat", "Ost","skinke", "champignon", "rejer", "peberfrugt"], 85)
Menu.AddPizza("Marinara",["Tomat", "Ost","rejer", "muslinger", "hvidløg"], 85)
Menu.AddPizza("Vegetarian",["Tomat", "Ost","grøntsager"], 80)
Menu.AddPizza("Italiana",["Tomat", "Ost","løg", "kødsauce"], 75)
Menu.AddPizza("Gorgonzola",["Tomat", "gorgonzola","løg", "champignon"], 75)
Menu.AddPizza("Contadina",["Tomat", "Ost","Oliven", "champignon"], 75)
Menu.AddPizza("Naples",["Tomat", "Ost","ansjoser", "oliven"], 79)
Menu.AddPizza("Vichinga",["Tomat", "Ost","skinke", "champignon","peberfrugt","hvidløg", "chili (stærk)"], 80)
Menu.AddPizza("Calzone Special",["Tomat", "Ost","skinke", "rejer", "kødsauce"], 80)
Menu.AddPizza("Esotica",["Tomat", "Ost","skinke", "rejer", "annanas"], 80)
Menu.AddPizza("Tonno",["Tomat", "Ost","Tun", "rejer"], 85)
Menu.AddPizza("Sardegna",["Tomat", "Ost","cocktail pølser", "bacon", "løg", "æg"], 80)
Menu.AddPizza("Romana",["Tomat", "Ost","skinke", "bacon", "løg"], 78)
Menu.AddPizza("sole",["Tomat", "Ost","skinke", "bacon", "æg"], 78)
Menu.AddPizza("Big Mamma",["Tomat", "Gorgonzola","rejer", "Asparges", "parma skinke"], 90)

# En Decorator for en route
@app.route('/')
def startside():
    return render_template('Startside.html')



@app.route('/Bestilling', methods=['GET', 'POST'])

def Bestilling():

    ListofStrings =[]
    for pizza in Menu.PizzaCatalog:
        pizzainfo=[]
        pizzainfo.append(pizza.Id)
        pizzainfo.append(pizza.Name)

        toppingstr = " "
        for topping in pizza.toppings:
            toppingstr = toppingstr + topping + ", "
        
        pizzainfo.append(toppingstr)
        pizzainfo.append(pizza.Price)
        ListofStrings.append(pizzainfo)


    if request.method == 'POST':
        liste = request.form.getlist('Pizzas')
        navn = request.form['Navn']
        takeaway = request.form['takeaway']
        if takeaway == "on":
            takeaway = "True"
        else:
            takeaway = "False"
        
        orderlist = []
        for number in liste:
            orderlist.append(int(number))
        if sum(orderlist) == 0:
            return render_template('Bestilling.html', data = ListofStrings)
        else:
            if len(navn) == 0 or navn.isspace() == True:
                return render_template('Bestilling.html', data = ListofStrings)
            else:
                pizzalist=[]
                antallist=[]
                for i in range(1,len(orderlist)+1):
                    if orderlist[i-1] != 0:
                        pizzalist.append(i)
                        antallist.append(orderlist[i-1])
                
                PizzaOrdre = list(itertools.chain(*(itertools.repeat(elem, n) for elem, n in zip(pizzalist, antallist))))

                Menu.AddOrder(PizzaOrdre, navn, takeaway)
                ordreID = len(Menu.TakeOrderCatalog)
                Menu.TakeOrderCatalog[ordreID-1]
                return redirect('/kvittering')
        





    return render_template('Bestilling.html', data = ListofStrings)

@app.route('/kvittering')
def kvittering():
    Ordre = Menu.TakeOrderCatalog[-1]

    return render_template('kvittering.html', Ordre=Ordre)


# til at køre koden direkte
if __name__== '__main__':
    app.run()