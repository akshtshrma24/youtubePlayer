import time

from flask import Flask, render_template, request
from prometheus_client import generate_latest, Gauge

import videoDownloading.handlers.vlcHandler as vlcHandler
from videoDownloading.handlers.mergeHandler import *
from videoDownloading.handlers.directoryHandler import *
import metricHandling.metrics as metricHandling

app = Flask(__name__, template_folder="./frontend")
vlc = vlcHandler.VlcHandler()
metric = metricHandling.Metrics()

# Prometheus metrics and variables
download_time = Gauge('download_time', 'Time it took to download')


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def my_form_post():
    link = request.form['text']
    start = time.time()
    download_merge(link)
    download_time.set(time.time() - start)
    metric.set_sent(False)
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
    if ('previous_button' in request.form):
        vlc.previous()
    else:
        vlc.next()
    return render_template('player.html')


@app.route('/metrics')
def metrics():
    if (metric.get_sent()):
        download_time.set(0)
    metric.set_sent(True)
    return generate_latest()
