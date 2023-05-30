from flask import Flask, request, redirect, url_for, send_file, render_template, send_from_directory
from subprocess import run
from datetime import datetime
import os
import logging

app = Flask(__name__)


def process_file(urls, download_param):
    download_param_album = download_param or '{artist}/{album}/{artist} - {title}'
    download_param_playlist = download_param or '{playlist}/{artists}/{album} - {title} {artist}'
    download_param_track = download_param or '{artist}/{album}/{artist} - {title}'

    os.chdir('downloads')
    # os.system(f'rm -rf *')

    for url in urls:
        if url:
            if "album" in url:
                run(['python3', '-m', 'spotdl', url, '--output', download_param_album])
            elif "playlist" in url:
                run(['python3', '-m', 'spotdl', url, '--output', download_param_playlist])
            elif "track" in url:
                run(['python3', '-m', 'spotdl', url, '--output', download_param_track])

    # os.system(f'zip -r musics.zip ./downloads')
    # run(['zip', '-r', 'musics.zip', '.'])
    os.chdir('../')


@app.route('/', methods=['GET', 'POST'])
def upload_form():
    return render_template('index.html')

# Fonctionne
# @app.route('/download/<filename>')
# def download_file(filename):
#   PATH='file.txt'
#   return send_file(PATH, as_attachment=True)


@app.route('/download', methods=['POST'])
def download_file():
    # votre code de téléchargement ici
    #   now = datetime.now()
    #   date_time = now.strftime("%Y-%m-%d %H-%M-%S")
    #   with open(f"file.txt", "w") as file:
    #     file.write(date_time)
    if request.method == 'POST':
        url1 = request.form['url1']
        url2 = request.form['url2']
        url3 = request.form['url3']
        url4 = request.form['url4']
        url5 = request.form['url5']
        download_param = request.form['output-format']

        urls = [url1, url2, url3, url4, url5]

        # Vérifier si au moins un champ est vide
        if not url1 and not url2 and not url3 and not url4 and not url5:
            return render_template('erreur.html')

        # Créer le dossier 'downloads' s'il n'existe pas
        if not os.path.exists('downloads'):
            os.makedirs('downloads')

        process_file(urls, download_param)

    # path = "downloads/musics.zip"
    # return send_file(path, as_attachment=True)
    return render_template('finish.html')


@app.errorhandler(404)
def page_not_found(error):  # error est necessaire
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=3000)
