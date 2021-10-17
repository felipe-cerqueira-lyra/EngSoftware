import os
from flask import Flask, request, jsonify, send_from_directory

# TODO (Thales): Remove local dependency
DIRECTORY = 'C:\\Users\\thale\\PycharmProjects\\EngSoftware\\output'

api = Flask(__name__)


@api.route('/files', methods=['GET'])
def list_files():
    pass


@api.route('/files/<file_name>', methods=['GET'])
def get_file(file_name):
    pass


@api.route('/files', methods=['POST'])
def post_file():
    pass


if __name__ == '__main__':
    api.run(debug=True, port=8000)
