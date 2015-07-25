import heatmap


class plottool():
	def heatmap(self, input):
		hm = heatmap.Heatmap()

		pts = [(x.lat, x.lng) for x in input if x.lat > 0 ]
		return pts

