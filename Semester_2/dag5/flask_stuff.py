# import af modulet Flask
from flask import Flask, request, render_template, redirect, session

import requests
import json



def elspotpriser():
    url = 'https://api.energidataservice.dk/dataset/Elspotprices?offset=0&sort=HourUTC%20DESC&timezone=dk'
    headers = {"Content-Type": "application/json"}
    response = requests.get(url, headers=headers).json()
    #print(response)
    with open('Semester_2/dag5/price_data.json', 'w') as f:
        json.dump(response, f)

    return response

def getTimedata(data):
    tidspunkter = []

    for x in range(0,len(data["records"])):
        if data["records"][x]["PriceArea"] == "DK1":
            tidspunkter.append(data["records"][x]["HourDK"])
    return tidspunkter

def getPriceData(data):
    priser = []

    for x in range(0,len(data["records"])):
        if data["records"][x]["PriceArea"] == "DK1":
            priser.append(data["records"][x]["SpotPriceDKK"])
    return priser



'''
elpriser = elspotpriser()

timeslots = getTimedata(elpriser)
priser = getPriceData(elpriser)

print(len(timeslots))

print(len(priser))

print(timeslots[0].split("T")[1].split(":", 2)[0])
print(timeslots[0].split("T")[1].split(":", 2)[0])
'''

app = Flask(__name__)


@app.route('/' , methods=['GET', 'POST'])
def startside():
    
    

    if request.method == 'POST':
        
        input1 = request.form['input1']
        input2 = request.form['input2']
        
       
        
        elpriser = elspotpriser()
               
        timeslots = getTimedata(elpriser)
        priser = getPriceData(elpriser)
        mydata = []
        
        for i in range(0,len(timeslots)):
            if int(input1.split(":")[0]) <= int(timeslots[i].split("T")[1].split(":", 2)[0]) and int(input2.split(":")[0]) >= int(timeslots[i].split("T")[1].split(":", 2)[0]): 
                tempdata = []
                tempdata.append(timeslots[i])
                tempdata.append(priser[i])
                mydata.append(tempdata)

        return render_template('index.html', myinput1=input1, myinput2=input2, data = mydata)
    
    return render_template('index.html')




# til at køre koden direkte
if __name__== '__main__':
    app.run()



