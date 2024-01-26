# app.py
from flask import Flask, request, abort
import os

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    n = request.args.get('n')
    m = request.args.get('m')

    if not n:
        abort(400, 'Parameter "n" is required.')

    file_path = f'/tmp/data/{n}.txt'

    if not os.path.exists(file_path):
        abort(404, f'File {n}.txt not found.')

    if m:
        try:
            m = int(m)
            with open(file_path, 'r') as file:
                lines = file.readlines()
                if 1 <= m <= len(lines):
                    return lines[m - 1]
                else:
                    abort(400, f'Line number "m" is out of bounds for file {n}.txt.')
        except ValueError:
            abort(400, 'Invalid value for parameter "m".')

    else:
        with open(file_path, 'r') as file:
            return file.read()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
