from website import create_app
from flask import request, Response
from werkzeug.utils import secure_filename

from website.database.db import db
from website.database.models import Img

app = create_app()


@app.route('/')
def home():
    return 'Home Page'


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


if __name__ == '__main__':
    app.run(debug=True)
