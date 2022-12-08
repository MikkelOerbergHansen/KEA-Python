####
#### tværfaglig dag med systemudvikling
####



# import af modulet Flask
from flask import Flask, request, render_template, redirect, session


class newUser:
    def __init__(self):
        self.pillestatus = "False"
        self.alarmtid = "Alarm ikke sat"
        self.alarmdage = []
        self.alarmvibration = " "
        self.alarmsang = " "
        self.alarmsnooze = " "
        self.byvalg=" "
        self.pollenvalg=" "

    def setalarmtid(self, tidinput):
        self.alarmtid = tidinput
        pass

    def getalarmtid(self):
        return self.alarmtid

    def setpillestatus(self, input):
        self.pillestatus=input
        pass

    def getpillestatus(self):
        return self.pillestatus


    def setbyvalg(self, input):
        self.byvalg=input
        pass

    def getbyvalg(self):
        return self.byvalg

    def setpollenvalg(self, input):
        self.pollenvalg=input
        pass

    def getpollenvalg(self):
        return self.pollenvalg

    def setalarmdage(self, input):
        self.alarmdage  = input
        pass

    def getalarmdage(self):
        return self.alarmdage

    def setalarmvibration(self, input):
        self.alarmvibration  = input
        pass

    def getalarmvibration(self):
        return self.alarmvibration

    def setalarmsang(self, input):
        self.alarmsang  = input
        pass

    def getalarmsang(self):
        return self.alarmsang

    def setalarmsnooze(self, input):
        self.alarmsnooze  = input
        pass

    def getalarmsnooze(self):
        return self.alarmsnooze













app = Flask(__name__)


user = newUser()

@app.route('/', methods=['GET', 'POST'])
def startside():
    overskrift= "Sandoz Allergi App"
    
    

    if request.method == 'POST':
        if 'form1' in request.form:
            alarmstatus = request.form['alarmstatus']
            user.setpillestatus(alarmstatus)
            print("pillestatus sat")
            return render_template('Startside.html', headline=overskrift, alarm = user.getpillestatus(), alarmtid = user.getalarmtid())

        elif 'form2' in request.form:
            forsideknap = request.form['forsideknap']
            print(forsideknap)
            return redirect('/')

        elif 'form3' in request.form:
            alarmknap = request.form['alarmknap']
            print(alarmknap)
            return redirect('/Alarm')

        elif 'form4' in request.form:
            pollenknap = request.form['pollenknap']
            print(pollenknap)
            return redirect('/Pollen')


            
    return render_template('Startside.html', headline=overskrift, alarm = user.getpillestatus(), alarmtid = user.getalarmtid() )





@app.route('/Alarm', methods=['GET', 'POST'])
def Alarm():
    overskrift = "Ændre alarm tidspunkt"
    ugedage = ["dag1", "dag2", "dag3", "dag4", "dag5", "dag6", "dag7"]
    for day in user.getalarmdage():
        if day == "Mandag":
            ugedage[0]= day
        if day == "Tirsdag":
            ugedage[1]= day
        if day == "Onsdag":
            ugedage[2]= day
        if day == "Torsdag":
            ugedage[3]= day
        if day == "Fredag":
            ugedage[4]= day
        if day == "Lørdag":
            ugedage[5]= day
        if day == "Søndag":
            ugedage[6]= day

    if request.method == 'POST':

        if 'anuller' in request.form:
            print("Anuller")
            return redirect('/')

        if 'gem' in request.form:
            alarmtid = request.form['alarmtid']
            user.setalarmtid(alarmtid)
            print("alrmtid = {}".format(alarmtid))
            ugedage = request.form.getlist('weekdays')
            user.setalarmdage(ugedage)
            print("valgte ugedage = {}".format(ugedage))
            if "vibration" in request.form:
                user.setalarmvibration(request.form['vibration'])
                print("Vibration = {}".format(request.form['vibration']))
            else:
                user.setalarmvibration("False")
                print("Vibration = False")
            if "sang" in request.form:
                alarmsang = request.form['sang']
                user.setalarmsang(alarmsang)
                print("Sang = {}".format(alarmsang))
            else:
                user.setalarmsang(" ")
                print("Sang = {}".format(" "))
            if "snooze" in request.form:
                alarmsnooze = request.form['snooze']
                user.setalarmsnooze(alarmsnooze)
                print("snooze tid = {}".format(alarmsnooze))
            else:
                user.setalarmsnooze(" ")
                print("snooze tid = {}".format(" "))
            


            return redirect('/Alarm')
        

        if 'form2' in request.form:
            forsideknap = request.form['forsideknap']
            print(forsideknap)
            return redirect('/')

        elif 'form3' in request.form:
            alarmknap = request.form['alarmknap']
            print(alarmknap)
            return redirect('/Alarm')

        elif 'form4' in request.form:
            pollenknap = request.form['pollenknap']
            print(pollenknap)
            return redirect('/Pollen')



    return render_template('Alarm.html', headline=overskrift, alarmtid=user.getalarmtid(), weekdays = ugedage, vibration = user.getalarmvibration(), sang = user.getalarmsang(), snooze = user.getalarmsnooze() )





@app.route('/Pollen', methods=['GET', 'POST'])
def Pollen():
    overskrift = "Dagens pollental"


    if request.method == 'POST':


        if 'form1' in request.form:
            byvalg = request.form['byvalg']
            user.setbyvalg(byvalg)
            print("byvalg = {}".format(byvalg))
            return redirect('/Pollen')

        if 'form5' in request.form:
            pollenvalg = request.form['pollenvalg']
            user.setpollenvalg(pollenvalg)
            print("pollenvalg = {}".format(pollenvalg))
            return redirect('/Pollen')


        if 'form2' in request.form:
            forsideknap = request.form['forsideknap']
            print(forsideknap)
            return redirect('/')

        elif 'form3' in request.form:
            alarmknap = request.form['alarmknap']
            print(alarmknap)
            return redirect('/Alarm')

        elif 'form4' in request.form:
            pollenknap = request.form['pollenknap']
            print(pollenknap)
            return redirect('/Pollen')



    return render_template('pollental.html', headline=overskrift, byvalg = user.getbyvalg(), pollenvalg = user.getpollenvalg())







# til at køre koden direkte
if __name__== '__main__':
    app.run()





























