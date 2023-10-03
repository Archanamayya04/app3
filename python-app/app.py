from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@database:5432/database_name'
db = SQLAlchemy(app)

# Define a model (example)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

# Route to query the database and render the HTML template
@app.route('/')
def index():
    # Retrieve data from the database
    users = User.query.all()
    # Render the 'index.html' template and pass the 'users' data to it
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

