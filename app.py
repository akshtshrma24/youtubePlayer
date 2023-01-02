from flask import Flask, render_template, request

from mergeHandler import * 
from directoryHandler import * 

app = Flask(__name__, template_folder="./frontend")

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def my_form_post():
    link = request.form['text']
    download_merge(link)
    link = ""
    return hello_world()

@app.route('/manage')
def manage():
    dictionary = get_file_names()
    return render_template('manage.html', dictionary=dictionary)

@app.route('/manage', methods=['POST'])
def delete_video():
    fileName = request.form['submit_button']
    delete_file(fileName)
    dictionary = get_file_names()
    return render_template('manage.html', dictionary=dictionary)