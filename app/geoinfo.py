import urllib2, urllib
import simplejson as json
import fiona

KEY = "&key=AIzaSyDU4m-ITLDPObZrzwvHXDGm-91pFBxu05w"

url = "https://maps.googleapis.com/maps/api/geocode/json?address=" 

class Geoinfo:
	def __init__(self, memcache, CL_ID, ESDA_ALTERNATE_PRODUCT_CD, CMR_CONTRACT_ID, \
				FIRST_NAME, LAST_NAME, STR_ONE_AD, CTY_AD, STATE_CD, ZIP, \
				EXTND_ZIP_CD, CNTRY_CD, US_CNTY_CD, GENDER_CD):
		self.CL_ID = CL_ID
		self.ESDA_ALTERNATE_PRODUCT_CD = ESDA_ALTERNATE_PRODUCT_CD
		self.CMR_CONTRACT_ID = CMR_CONTRACT_ID
		self.FIRST_NAME = FIRST_NAME
		self.LAST_NAME = LAST_NAME
		self.STR_ONE_AD = STR_ONE_AD
		self.CTY_AD = CTY_AD
		self.STATE_CD = STATE_CD
		self.ZIP = ZIP
		self.EXTND_ZIP_CD = EXTND_ZIP_CD
		self.CNTRY_CD = CNTRY_CD
		self.US_CNTY_CD = US_CNTY_CD
		self.GENDER_CD = GENDER_CD
		self.calc_location(memcache)

	def calc_location(self, memcache):
		address = (self.STR_ONE_AD + "," + self.CTY_AD + "," + self.STATE_CD).replace(" ", "+")
		if address in memcache:
			self.lat, self.lng = memcache[address]

		req_url = url + address + KEY
		response = urllib2.urlopen(req_url)
		data = json.load(response)   


		if len(data['results']) > 0:
			self.lat = data['results'][0]['geometry']['location']['lat']
			self.lng = data['results'][0]['geometry']['location']['lng']
			data[address] = (self.lat, self.lng)
		else:
			self.lat = 0
			self.lng = 0



	def __str__(self):
		return self.LAST_NAME + " " + self.FIRST_NAME




