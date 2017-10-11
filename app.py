from flask import Flask , render_template, flash, request, redirect, url_for
app  = Flask(__name__)
@app.route('/')
def index():
    return render_template('main.html')
@app.route('/innova')
def innova():
    return render_template('innova.html')
@app.route('/bolero')
def bolero():
    return render_template('bolero.html')
@app.route('/scorpio')
def scorpio():
    return render_template('scorpio.html')
@app.route('/qualis')
def qualis():
    return render_template('qualis.html')
if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)