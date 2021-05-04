from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
from pdfScanner import processReport
import os

UPLOAD_FOLDER = './'
ALLOWED_EXTENSIONS = {'pdf'}


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/checkInteractiveBrokers', methods=['POST'])
@cross_origin()
def checkIB():
    # Read request
    file = request.files['pdf']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        processedFileJSON = processReport('./' + filename)
        return processedFileJSON
    return jsonify(error='Something went wrong')


if __name__ == '__main__':
    app.run(debug=True)
