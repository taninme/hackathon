import fiona
def heatmap(input):
	shape_file = fiona.open('../cb_2014_us_county_500k.shp')
	bounds = shape_file.bounds
	shape_file.close()

	extra = 0.01
	ll = (bounds[0], bounds[1])
	ur = (bounds[2], bounds[3])
	coords = list(chain(ll, ur))
	w, h = coords[2] - coords[0], coords[3] - coords[1]
	m = Basemap(
	    projection='tmerc',
	    lon_0=-2.,
	    lat_0=49.,
	    ellps = 'WGS84',
	    llcrnrlon=coords[0] - extra * w,
	    llcrnrlat=coords[1] - extra + 0.01 * h,
	    urcrnrlon=coords[2] + extra * w,
	    urcrnrlat=coords[3] + extra + 0.01 * h,
	    lat_ts=0,
	    resolution='i',
	    suppress_ticks=True)
	m.readshapefile(
	    'data/london_wards',
	    'london',
	    color='none',
	    zorder=2)