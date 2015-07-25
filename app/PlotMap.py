class plottool():
	def heatmap(self, input):
		
		LNG = [x.lng for x in input]
		LAT = [x.lat for x in input]
		return LNG, LAT

