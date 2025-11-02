from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agents_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Agent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code_name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    access = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'Agent: id: {self.id}, Code name: {self.code_name}, Phone: {self.phone_number}, Email: {self.email}, Access level: {self.access}'

with app.app_context():
    db.create_all()

@app.route('/')
def get_agents():
    agents = Agent.query.all()
    return render_template('agents.html', agents=agents)

@app.route('/add', methods=['GET', 'POST'])
def add_agent():
    if request.method == 'POST':
        code_name = request.form['code_name']
        phone_number = request.form['phone_number']
        email = request.form['email']
        access = request.form['access']
        if code_name.strip() and phone_number.strip() and email.strip() and access.strip():
            new_agent = Agent(code_name=code_name, phone_number=phone_number, email=email, access=access)
            db.session.add(new_agent)
            db.session.commit()
        return redirect(url_for('get_agents'))
    return render_template('add_agent.html')

@app.route('/agent/<int:id>')
def agent_info(id):
    agent = Agent.query.get_or_404(id)
    return render_template('agent_info.html', agent=agent)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_agent(id):
    agent = Agent.query.get_or_404(id)
    if request.method == 'POST':
        new_code_name = request.form['code_name']
        new_phone_number = request.form['phone_number']
        new_email = request.form['email']
        new_access = request.form['access']
        if new_code_name.strip() and new_phone_number.strip() and new_email.strip() and new_access.strip():
            agent.code_name = new_code_name
            agent.phone_number = new_phone_number
            agent.email = new_email
            agent.access = new_access
            db.session.commit()
        return redirect(url_for('get_agents'))
    return render_template('edit_agent.html', agent=agent)

@app.route('/delete/<int:id>')
def delete_agent(id):
    agent = Agent.query.get_or_404(id)
    db.session.delete(agent)
    db.session.commit()
    return redirect(url_for('get_agents'))

@app.route('/delete/all')
def delete_all_agents():
    Agent.query.delete()
    db.session.commit()
    return redirect(url_for('get_agents'))

@app.route('/<access>')
def get_filter_agents(access):
    valid_access_levels = ['unclassified', 'classified', 'top secret']

    if access.lower() not in valid_access_levels:
        return "Invalid access level", 400

    agents = Agent.query.filter_by(access=access).all()

    if not agents:
        return render_template('agents.html', agents=[], message="No agents found for this access level")

    return render_template('agents.html', agents=agents)

if __name__ == '__main__':
    app.run(debug=True)

