
# import af modulet Flask
from flask import Flask, request, render_template, redirect, session


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def startside():
    HeadLine = "Welcome"

    if request.method == 'POST':
        SearchWord = request.form['searchbar']
        
        return render_template('Startside.html', Headline = HeadLine, Search = SearchWord)


    
    return render_template('Startside.html', Headline = HeadLine)



@app.route('/side1', methods=['GET', 'POST'])
def Side1():
    HeadLine = "Side1"

    if request.method == 'POST':
        SearchWord = request.form['searchbar']
        
        return render_template('side1.html', Headline = HeadLine, Search = SearchWord)


    
    return render_template('side1.html', Headline = HeadLine)





@app.route('/side2', methods=['GET', 'POST'])
def Side2():
    HeadLine = "Side2"

    if request.method == 'POST':
        SearchWord = request.form['searchbar']
        
        return render_template('side2.html', Headline = HeadLine, Search = SearchWord)


    
    return render_template('side2.html', Headline = HeadLine)







# til at køre koden direkte
if __name__== '__main__':
    app.run()
































