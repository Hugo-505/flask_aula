from flask import Flask, render_template
app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('index.html')
@app.route('/teste')
def teste():
    return 'AAAAAAA'
@app.route('/')
def index():
    return 'Olá Mundo'

if __name__ == '__main__':
    app.run(debug=True)

