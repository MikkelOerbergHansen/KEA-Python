from pathlib import Path
import os
from flask import Flask, render_template, request, redirect, url_for, abort, jsonify
from werkzeug.utils import secure_filename
import csv

UPLOADS_PATH = Path.cwd() / "Semester_2" / "recap" / "stuff" / "flask-file-upload-2" / "static" / "uploads"
print(UPLOADS_PATH)
app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif', '.csv']
app.config['UPLOAD_PATH'] = UPLOADS_PATH


# Index GET route


@app.route('/')
def index():
    with open('Semester_2/recap/stuff/flask-file-upload-2/static/temp.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        list1 = []
        for row in csv_reader:
            list1.append(row)
    return render_template('index.html', list1=list1, header=header)


# GET route for JSON in REST API

@app.route('/api/data')
def get_data():
    with open('Semester_2/recap/stuff/flask-file-upload-2/static/temp.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        print(header)
        list1 = []
        for row in csv_reader:
            list1.append(row)
            print(list1)
        dict1 = dict(zip(header, list1))
    return jsonify(dict1)


# File upload POST route


@app.route('/upload/', methods=['POST'])
def upload_files():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    print(filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        print(os.path.join(app.config['UPLOAD_PATH'], filename))
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    return redirect(url_for('index'))


# Add data to csv file POST route


@app.route('/add/', methods=['POST'])
def add_data():
    print("test")
    print(request.form.to_dict().keys())
    data = []
    for key in request.form.to_dict().keys():
        data.append(request.form[key])
        

    '''
    title = request.form['title']
    category = request.form['category']
    data = request.form['data']
    print(title)
    print(category)
    print(data)
    '''
    with open('Semester_2/recap/stuff/flask-file-upload-2/static/temp.csv', 'a', encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(data)
    return redirect(url_for('index'))


# Variable Rules for a View route
# @app.route('files/<converter: variable_name>')


files = ['hej', 'goddag', 'farvel', 'jotak', 'nej']


@app.route("/files/<int:index_id>/")
def csv_page(index_id):
    print(files)
    for i, item in enumerate(files):
        if index_id == i:
            return render_template("file.html", item=item)
    for i, item in enumerate(files):
        if index_id != i:
            return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()