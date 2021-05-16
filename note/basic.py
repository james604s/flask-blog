"""
basic.py
create entries into the tables
"""
from models import db, Puppy, Owner, Toy

#CREATING 2 Puppies
rufus = Puppy("Rufus")
fido = Puppy("Fido")

#ADD Puppies
db.session.add_all([rufus, fido])
db.session.commit()

#Check
print(Puppy.query.all())
rufus = Puppy.query.filter_by(name="Rufus").first()
print(rufus)

#CREATE OWNER OBJECT
jose = Owner("Jose", rufus.id)

#Give Rufus some toys
toy1 = Toy("Chew Toy", rufus.id)
toy2 = Toy("Ball", rufus.id)

db.session.add_all([jose, toy1, toy2])
db.session.commit()

#Grab Fufus After Those Additions
rufus = Puppy.query.filter_by(name="Rufus").first()
print(rufus)

print(rufus.report_toys())