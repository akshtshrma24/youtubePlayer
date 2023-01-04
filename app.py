from flask import Flask, render_template, request

from mergeHandler import * 
from directoryHandler import * 
from vlcHandler import * 

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
def manage_video():
    dictionary = get_file_names()
    if('delete_button' in request.form):
        fileName = request.form['delete_button']
        delete_file(fileName)
        return render_template('manage.html', dictionary=dictionary)
    elif('play_button' in request.form):
        fileName = request.form['play_button']
        play_vlc(fileName)
        return render_template('manage.html', dictionary=dictionary)
    else:
        fileName = request.form['play_playlist_button']
        play_vlc(fileName)
        return render_template('manage.html', dictionary=dictionary)
