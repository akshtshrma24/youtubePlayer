from flask import Flask, render_template, request

import vlcHandler
from mergeHandler import *
from directoryHandler import *
from logger import * 

app = Flask(__name__, template_folder="./frontend")
vlc = vlcHandler.vlcHandler()

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
    os.system("killall vlc")
    dictionary = get_file_names()
    if ('delete_button' in request.form):
        fileName = request.form['delete_button']
        delete_file(fileName)
    elif ('play_button' in request.form):
        fileName = request.form['play_button']
        vlc.play_song(fileName)
    elif ('play_playlist_button' in request.form):
        fileName = request.form['play_playlist_button']
        vlc.set_directory(fileName)
        vlc.start_playlist()
    return render_template('manage.html', dictionary=dictionary)

@app.route('/player')
def load_player():
    return render_template('player.html')

@app.route('/player', methods=['POST'])
def player_button():
    os.system("killall vlc")
    if('previous_button' in request.form): vlc.previous()
    else: vlc.next()
    return render_template('player.html')
