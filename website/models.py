from . import db


class File(db.Model):
    """
    This class represents a File
    """
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    data = db.Column(db.LargeBinary)

    def __init__(self, name, data):
        self.name = name
        self.data = data
