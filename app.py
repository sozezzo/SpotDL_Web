from flask import Flask, request, redirect, url_for, send_file
import os

app = Flask(__name__)

@app.route('/')
def upload_form():
    return '''
    <form method="POST">
    <label for="url">URL:</label>
    <input type="text" name="url" id="url">
    <input type="submit" value="Téléchargement">
    </form>
    '''

@app.route('/', methods=['GET', 'POST'])
def index():
    message = None
    if request.method == 'POST':
        url = request.form['url']
        result = process_file(url)
    return ''' 
    <h1> Téléchargement terminé </h1>
    <button onclick="window.location.href = '/';">Télécharger à nouveau</button>
    '''

def process_file(url):
    path = os.path.expanduser('~/musics')
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
    

# @app.route('/download/<path:filename>')
# def download_file(filename):
#     return send_file(filename, attachment_filename=filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
