import http.server
import threading
import os

from videoDownloading.handlers.mergeHandler import download_merge
from frontend.renderHtml import *
import videoDownloading.handlers.vlcHandler as vlcHandler

vlc = vlcHandler.VlcHandler()


class TestServerHandler(http.server.CGIHTTPRequestHandler):

    def do_GET(self):
        file = open("./frontend/index.html", "w")
        file.write(renderHtml())
        file.close()
        if self.path == '/':
            self.path = '/frontend/index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        os.system("killall vlc")
        text = str(self.rfile.read(int(self.headers['Content-Length'])).decode("utf-8")).replace(
            "%3A", ":").replace("%2F", "/").replace("%3F", "?").replace("%3D", "=")
        if ("play_playlist_button" in text):
            vlc.set_directory(text.split("=")[1])
            threading.Thread(target=vlc.start_playlist).start()
        elif ("previous_button" in text):
            threading.Thread(target=vlc.previous).start()
        elif ("next_button" in text):
            threading.Thread(target=vlc.next).start()
        elif ("stop_button" in text):
            threading.Thread(target=vlc.stop_vlc).start()
        else:
            url = text[5:]
            file = open("./playlists.txt", "a+")
            file.seek(0)
            if(url not in file.read()):
                file.write(url + "\n")
            threading.Thread(target=download_merge, args=(url, )).start()
            
        if self.path == '/':
            self.path = '/frontend/index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


test_server = http.server.HTTPServer(('0.0.0.0', 80), TestServerHandler)
test_server.serve_forever()
