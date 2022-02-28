import os
from flask import Flask, request, send_from_directory, render_template
from werkzeug.utils import secure_filename
import csv_parser

HOST = '127.0.0.1'
PORT = '8080'

app = Flask(__name__)
UPLOAD_FOLDER = 'file'
ALLOWED_EXTENSIONS = ['csv']
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            csv_parser.parse_file(UPLOAD_FOLDER + '/' + filename)
            return send_from_directory(app.config['UPLOAD_FOLDER'],
                                       filename)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
