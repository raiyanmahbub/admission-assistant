from flask import Flask, request, render_template
app = Flask(__name__)

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from backend.data import clean_data



@app.route('/', methods = ['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/data', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = clean_data(request.form.to_dict())


        return render_template('data.html', data = form_data)


@app.route('/test')
def test():
    return render_template('home.html')
    pass




if __name__ == '__main__':
    app.run(debug=True)