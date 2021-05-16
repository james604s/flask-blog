import os 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate #pip install Flask-Migrate

BASEDIR = os.path.abspath(os.path.dirname(__file__))
#/Users/sq/flask_proj/flask-blog

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(BASEDIR, "data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
#flask db migrate -m "some message"
Migrate(app, db)
#####################################
class Puppy(db.Model):
    #MANUAL TABLE NAME CHOICE
    __tablename__ = "puppies"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    """One:One To Many, Puppy to Many Toys"""
    toys = db.relationship("Toy", backref="puppy", lazy='dynamic')
    """One to One, One Puppy to One Owner"""
    owner = db.relationship("Toy", backref="puppy", uselist=False)

    def __init__(self, name, toys):
        self.name = name

    def __repr(self):
        if self.owner:
            return f"Puppy name is {self.name} and \
                    owner is {self.owner.name}"
        else:
            return f"Puppy name is {self.name} and \
                    and has no owner yet!"

    def report_toys(self):
        print("Here are my toys:")
        for toy in self.toys:
            print(toy.item_name)
class Toy(db.Model):
    __tablename__ = "toys"
    
    id = db.Column(db.Integer, primary_key = True)
    item_name = db.Column(db.Text)
    puppy_id = db.Column(db.Interger, db.Foreign("Puppies.id"))
    
    def __init__(self, item_name, puppy_id):
        self.item_name = item_name
        self.puppy_id = puppy_id

class Owner(db.Model):
    __tablename__ = "Owners"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Interger, db.Foreign("Puppies.id"))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id

    # def __init__(self, name, age, breed):
    #     self.name = name
    #     self.age = age
    #     self.breed = breed

    # def __repr__(self):
    #     return f"Puppy {self.name} is {self.age} years old"