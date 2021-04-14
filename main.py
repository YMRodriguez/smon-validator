from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/checkInteractiveBrokers', methods=['POST'])
@cross_origin()
def checkIB():
    # Read request
    file = request.files['pdf']
    data = request.files['settings']
    file.save('/')
    return jsonify(hello = 'world')


if __name__ == '__main__':
    app.run(debug=True)
