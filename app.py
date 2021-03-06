from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_admin import Admin 
from flask_admin.contrib.sqla import ModelView 
 
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'flask' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sql12363465:9FIBXkEcCi@sql12.freemysqlhosting.net:3306/sql12363465' 

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

admin = User('admin', 'admin@example.com')

db.create_all() # In case user table doesn't exists already. Else remove it.    
db.session.add(admin)
db.session.commit() # This is needed to write the changes to database
User.query.all()
User.query.filter_by(username='admin').first()