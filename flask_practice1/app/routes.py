from flask import render_template, request, redirect, jsonify, url_for
from app import app
from datetime import datetime

@app.route('/')
def home():
    current_time = datetime.now()
    return render_template('index.html', current_time=current_time)

@app.route('/about')
def about():
    team_members = [
        {'name': 'Alice', 'role': 'Developer'},
        {'name': 'Bob', 'role': 'Designer'},
        {'name': 'Charlie', 'role': 'Project Manager'}
    ]
    return render_template('about.html', team_members=team_members)

@app.route('/contact')
def contact():
    customer_care = {
        'number': '3-45-89',
        'address': {
            'city': 'London',
            'street':'Carey Street',
            'building': 666
        }
    }
    return render_template('contact.html', customer_care=customer_care)

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        return jsonify({'success': True})
    else:
        return redirect(url_for('contact'))