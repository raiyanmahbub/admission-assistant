from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/', methods = ['POST', 'GET'])
def index():
    return render_template('home.html')


@app.route('/data', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        return render_template('data.html', data = form_data)




if __name__ == '__main__':
    app.run(debug=True)