from flask import Flask, render_template

app = Flask(__name__)

yourdb=[
     ("your data 1.1","your data 1.2"),
     ("your data 2.1","your data 2.2"),
     ("your data 3.1", "your data 3.2")
     ]
@app.route("/")
def main():
    return render_template("index.html",data=yourdb)

if __name__ == '__main__':
    app.debug = True
    app.run() #go to http://127.0.0.1:5000/ to view the page.