from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

@app.route('/people', methods = ['GET', 'POST'])
def get_person():

    if request.method == 'GET':
        return 'akosdokasdoka'

    if request.method == 'POST':
        pass

    else:
        print("You did not enter a recognised HTTP method")


if __name__ == '__main__':
    app.run(host='localhost', port=8080)