import requests
import json

response = requests.get('https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow')

for data in response.json()['items']:
    print(data['title'])
    print(data['link'])


#code for the 29 min mark
python -m venv myvenv
myvenv/Scripts/activate
pip install flask
pip install flask-sqlalchemy
pip freeze > requirements.txt
New-Item application.py


#code for the 30:34 mark
set FLASK_APP=application.py
set FLASK_ENV=development
$env:FLASK_APP="application.py"
flask run 


#code for the 36:14 mark
python
from application import app, db
app.app_context().push()