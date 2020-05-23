from flask_basic import db
from flask_basic import Locations

#Datenbank erstellen
db.create_all()

loc1 = Locations(markerName='first',markerLon='11.7',markerLat='49.6',markerIconImage=0,
	markerContent='the coldsleep itself was dreamless',markerShowPopupOnLoad=True)

db.session.add(loc1)

loc2 = Locations(markerName='second',markerLon='13.1',markerLat='40.2',markerIconImage=0,
	markerContent='a man from Tentucket',markerShowPopupOnLoad=True)

db.session.add(loc2)

#Änderungen speichern
db.session.commit()

