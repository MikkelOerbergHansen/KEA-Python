import sqlite3
import json
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)


def _connect_fetch():
    with sqlite3.connect('Semester_2/recap/stuff/flask-rest-api-sqlite/database.db') as connector:
        connector.row_factory = sqlite3.Row
        cursor = connector.cursor()
        countries = cursor.execute('SELECT * FROM countries').fetchall()
        return countries


@app.route('/')
def index():
    countries = _connect_fetch()
    return render_template('index.html', countries=countries)


@app.route("/countries", methods=["GET"])
def get_countries():
    countries = _connect_fetch()
    print(type(countries))
    print(countries)

    countries_as_dict = []
    for c in countries:
        country_as_dict = {
            'id': c[0],
            'created_at': c[1],
            'name': c[2],
            'capital': c[3],
            'area': c[4]
        }
        countries_as_dict.append(country_as_dict)

    countriesToJSON = json.dumps(countries_as_dict)
    # countriesToJSON = json.loads(countries_as_dict)
    # countriesToJSON = json.dumps(json.JSONDecoder().decode(countries_as_dict))

    print(type(countries_as_dict))
    print(countries_as_dict)

    print(type(countriesToJSON))
    print(countriesToJSON)

    print(type(jsonify(countries_as_dict)))
    print(jsonify(countries_as_dict))

    # return jsonify(countries)
    # return jsonify(countriesToJSON)
    # return countriesToJSON
    return jsonify(countries_as_dict)


''' json.dumps(countries_as_dict)
"[{\"id\": 1, \"created_at\": \"2022-05-30 09:20:43\", \"name\": \"Thailand\", \"capital\": \"Bangkok\", \"area\": 513120}, {\"id\": 2, \"created_at\": \"2022-05-30 09:20:43\", \"name\": \"Australia\", \"capital\": \"Canberra\", \"area\": 7617930}, {\"id\": 3, \"created_at\": \"2022-05-30 09:20:43\", \"name\": \"Egypt\", \"capital\": \"Cairo\", \"area\": 1010408}, {\"id\": 4, \"created_at\": \"2022-05-30 09:24:32\", \"name\": \"Denmark\", \"capital\": \"Copenhagen\", \"area\": 43094}]"
'''

''' jsonify(countries)
[{"area":513120,"capital":"Bangkok","id":1,"name":"Thailand"},{"area":7617930,"capital":"Canberra","id":2,"name":"Australia"},{"area":1010408,"capital":"Cairo","id":3,"name":"Egypt"}]
'''


@app.route('/countries', methods=['POST'])
def add_country():
    if request.is_json:
        country = request.get_json()
        name1 = country["name"]
        capital1 = country["capital"]
        area1 = country["area"]

        with sqlite3.connect('Semester_2/recap/stuff/flask-rest-api-sqlite/database.db') as connector:
            cursor = connector.cursor()
            cursor.execute('INSERT INTO countries (name, capital, area) VALUES(?, ?, ?);', (name1, capital1, area1))

        return country, 201

    if request.method == 'POST':
        name1 = request.form['name']
        capital1 = request.form['capital']
        area1 = request.form['area']

        with sqlite3.connect('Semester_2/recap/stuff/flask-rest-api-sqlite/database.db') as connector:
            cursor = connector.cursor()
            cursor.execute('INSERT INTO countries (name, capital, area) VALUES(?, ?, ?);', (name1, capital1, area1))

        return redirect(url_for('index'))


# Hvad nu hvis jeg vil lave POST kald med JSON i stedet for request.form?


''' 
Public APIs list
https://github.com/public-apis/public-apis
'''


if __name__ == '__main__':
    app.run()
