from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/gustos')
def gustos():
    return render_template('gustos.html')

@app.route('/hab')
def hab():
    return render_template('hab.html')

@app.route('/contact')
def contact():
    return render_template('contacto.html')
    
if __name__ == '__main__':
    app.run(debug = True)
