from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///locs.db'

CORS(app)

db = SQLAlchemy(app)

#Datenbank
class Locations(db.Model):
	markerName = db.Column(db.String(80), primary_key=True)
	markerLon = db.Column(db.Numeric())
	markerLat = db.Column(db.Numeric())
	markerIconImage = db.Column(db.Integer())
	markerContent = db.Column(db.Text())
	markerShowPopupOnLoad = db.Column(db.Boolean())


	def __init__(self, markerName, markerLon, markerLat, markerIconImage, markerContent, markerShowPopupOnLoad):
		self.markerName = markerName
		self.markerLon = markerLon
		self.markerLat = markerLat
		self.markerIconImage = markerIconImage
		self.markerContent = markerContent
		self.markerShowPopupOnLoad = markerShowPopupOnLoad

	def __repr__(self):
		return "Locations({},{},{},{},{},{})".format(self.markerName,self.markerLon,self.markerLat,
			self.markerIconImage,self.markerContent,self.markerShowPopupOnLoad)

#mit der Datenbank - benutzt die Datenbank 'Locations'
@app.route('/api/v1/locations/alldb', methods=['GET'])
def api_alldb(db=db,Locations=Locations):

	loc_data = Locations.query.all()
	locations = [{'markerName':loc.markerName,'markerLon':float(loc.markerLon),
	'markerLat':float(loc.markerLat),'markerIconImage':loc.markerIconImage,
	'markerContent':loc.markerContent,'markerShowPopupOnLoad':loc.markerShowPopupOnLoad} for loc in loc_data]

	return jsonify(locations)


if __name__ == '__main__':
	app.run(debug=True)

