import unittest
import requests
import json

def testGetAllLocations():
	url = "http://127.0.0.1:5000/api/v1/locations/alldb"
	response = requests.get(url)
	print(response.json())

testGetAllLocations()
