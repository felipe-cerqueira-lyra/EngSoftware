import os
from website import create_app
from flask import Flask, redirect, url_for, render_template, request, Response, send_from_directory
from werkzeug.utils import secure_filename

from website.database.db import db
from website.database.models import Img

DOWNLOAD_DIRECTORY = 'E:\\UFMG (ANB)\\Eng Software\\TP1\\EngSoftware\\static\\midia' # Diretorio local para os arquivos, lembrar de alterar dependendo da máquina

app = create_app()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/uploadf')
def uploadf():
    return render_template("upload.html")


@app.route('/upload', methods=['POST'])
def upload():
    pic = request.files['pic']
    if not pic:
        return 'No pic uploaded', 400

    filename = secure_filename(pic.filename)
    mimetype = pic.mimetype

    if not filename or not mimetype:
        return 'Bad upload', 400

    img = Img(img=pic.read(), mimetype=mimetype, name=filename)
    db.session.add(img)
    db.session.commit()
    return 'Img has been uploaded!', 200


@app.route('/<int:id>')
def get_img(id):
    img = Img.query.filter_by(id=id).first()
    if not img:
        return 'No img with that id', 404
    return Response(img.img, mimetype=img.mimetype)

@app.route('/files/<file_name>', methods=['GET'])
def get_file(file_name):
    # as_attachment = True (Download file)
    # as_attachment = False (Open file (browser))
    return send_from_directory(DOWNLOAD_DIRECTORY, file_name, as_attachment=True)

@app.route('/download/<file_name>')
def download(file_name):
    name, extension = os.path.splitext(file_name)
    if (extension == '.mp3'):
        type = 'audio'
    elif (extension == '.mp4'):
        type = 'video'
    else :
        type = 'img'
    
    path = 'midia/'+ file_name
    return render_template('/download.html', archive_type = type, archive = url_for('static', filename = path), file_input = file_name)

if __name__ == '__main__':
    app.run(debug=True)
