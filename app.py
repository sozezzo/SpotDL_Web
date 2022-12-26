from flask import Flask, render_template, request
import os
import time

app = Flask(__name__)

def download_music(url):

    path = os.path.expanduser('~')
    download_param_album = '{artist}/{album}/{artist} - {title}'
    download_param_playlist = '{playlist}/{artists}/{album} - {title} {artist}'

    if "album" in url:
        #os.makedirs(f"{path}")
        os.chdir(f"{path}")
        print ("album found")
        os.system(f'python3 -m spotdl {url} --output "{download_param_album}"')
    elif "playlist" in url:
        os.chdir(f"{path}")
        print("playlist found")
        os.system(f'python3 -m spotdl {url} --output "{download_param_playlist}"')

@app.route('/', methods=['GET', 'POST'])
def index():
    message = None
    if request.method == 'POST':
        url = request.form['url']
        message = download_music(url)
    return render_template('index.html', message=message)
