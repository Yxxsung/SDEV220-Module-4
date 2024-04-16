python -m venv myvenv
myvenv/Scripts/activate
pip install flask
pip install flask-sqlalchemy
pip freeze > requirements.txt
New-Item application.py


from flask import Flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy



app.conmfig['SQLAlchemy_DATABASE_URI'] = 'sqllite:///data.db'
db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))
    
    
def __repr__(self):
    return f"{self.name} - {self.dscription}"

@app.route('/')
def index():
    return 'hello!'

set FLASK_APP=application.py
set FLASK_ENV=development
$env:FLASK_APP="application.py"
flask run 


app.route('/books')
def get_books():
    
    return {'dooks':'book data'}