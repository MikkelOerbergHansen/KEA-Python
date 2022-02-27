from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    text2 = request.form['text2']
    return ('welcome ' + processed_text + '<br /><br />' +
            'your password is ' + text2 + '<br /><br />' + 
            '<a href="/salesPage"><button>start shopping</button></a>')


@app.route('/salesPage')
def salesPage():
    return ('welcome to the shooping page')




if __name__ == "__main__":
    app.run()