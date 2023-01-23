from videoDownloading.handlers.directoryHandler import get_file_names

def renderHtml():
    injected = ""
    file_names = get_file_names()
    for t in file_names:
        injected += """<h2>{}<input class="play" type="submit" name="play_playlist_button" value="{}"> </h2> """.format(t,t)
        for p in file_names[t]:
            injected += "<h3>{}</h3>".format(p)
        
    html = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" href="../static/styles/index.css">
                <title>Past Link</title>
            </head>
            <body>
                <div>
                    <div>
                        <h2>Enter url</h2>
                    </div>
                </div>
                <div>
                    <form method="POST">
                        <input class="inputBox" name="text">
                        <input class="submitButton" type="submit">
                    </form>
                </div>
                <div class="shift">
                    <form method="POST">
                    {}
                    </form>
                </div>
                <div>
                    <form method="POST">
                        <input class="previous round" type="submit" name="previous_button" value="←">
                        <input class="next round" type="submit" name="stop_button" value="◼">
                        <input class="next round" type="submit" name="next_button" value="→">
                    </form>
                </div>
            </body>
            </html>
        """.format(injected)
    return html