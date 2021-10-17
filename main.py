import os
from flask import Flask, request, jsonify, send_from_directory

# TODO (Thales): Remove local dependency
DIRECTORY = 'C:\\Users\\thale\\PycharmProjects\\EngSoftware\\output'

api = Flask(__name__)


@api.route('/files', methods=['GET'])
def list_files():
    files = list()
    for file in os.listdir(DIRECTORY):
        file_path = os.path.join(DIRECTORY, file)
        if os.path.isfile(file_path):
            files.append(file)
    return jsonify(files)


@api.route('/files/<file_name>', methods=['GET'])
def get_file(file_name):
    # as_attachment = True (Download file)
    # as_attachment = False (Open file (browser))
    return send_from_directory(DIRECTORY, file_name, as_attachment=True)


@api.route('/files', methods=['POST'])
def post_file():
    pass


if __name__ == '__main__':
    api.run(debug=True, port=8000)
