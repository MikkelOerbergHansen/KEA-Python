
# import af modulet Flask
from flask import Flask, request, render_template, redirect, session


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def startside():
    HeadLine = "Welcome"

    if request.method == 'POST':
        SearchWord = request.form['searchbar']
        print(SearchWord)
        print("test")
        
        return render_template('Startside.html', Headline = HeadLine, Search = SearchWord)


    
    return render_template('Startside.html', Headline = HeadLine)








# til at køre koden direkte
if __name__== '__main__':
    app.run()
































