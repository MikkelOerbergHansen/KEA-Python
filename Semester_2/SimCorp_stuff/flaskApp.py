
# import af modulet Flask
from flask import Flask, request, render_template, redirect, session
import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt








app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def startside():
    HeadLine = "Welcome"

    if request.method == 'POST':
        SearchWord = request.form['searchbar']
        
        return render_template('Startside.html', Headline = HeadLine, Search = SearchWord)


    
    return render_template('Startside.html', Headline = HeadLine)



@app.route('/LinRegExample', methods=['GET', 'POST'])
def LinearRegEx():
    HeadLine = "Linear Regression"

    if request.method == 'POST':
        SearchWord = request.form['searchbar']
        
        return render_template('LinReg.html', Headline = HeadLine, Search = SearchWord)


    
    return render_template('LinReg.html', Headline = HeadLine)





@app.route('/DecTreeExample', methods=['GET', 'POST'])
def DecTreesEx():
    HeadLine = "Decision Tree"

    if request.method == 'POST':
        SearchWord = request.form['searchbar']
        
        return render_template('DecTree.html', Headline = HeadLine, Search = SearchWord)


    
    return render_template('DecTree.html', Headline = HeadLine)







# til at køre koden direkte
if __name__== '__main__':
    app.run()
































