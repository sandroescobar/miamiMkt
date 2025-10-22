import os
from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-key-change-in-production')
app.config['ENV'] = os.getenv('FLASK_ENV', 'development')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/locations')
def locations():
    return render_template('locations.html')

@app.route('/support')              # <-- add this
def support():
    return render_template('support.html')

    
if __name__ == '__main__':
    debug_mode = app.config['ENV'] == 'development'
    app.run(debug=debug_mode)