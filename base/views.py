from flask import render_template
from . import app

@app.errorhandler(404)
def page_not_found_handler(error):
    return "Error!! page not found"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def show_dashboard():
    return render_template('dashboard.html')
