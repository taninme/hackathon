import sys, os
import xlrd
from geoinfo import Geoinfo
from PlotMap import *

class generator():
	def gene(self):
		result = self.parser()

		pt = plottool()
		pt.heatmap(result)
		
	def parser(self):
		
		#We need to save our requests
		memcache = {}
		print os.path.dirname(os.path.realpath(__file__))
		data = xlrd.open_workbook("data/test.xls")
		first_sheet = data.sheet_by_index(0)
		success = 0.0
		amount  = 0
		#sheet name
		name = first_sheet.name
		
		#N is the size of data
		N = first_sheet.nrows

		# COLS is the dimension of each vector
		COLS = first_sheet.ncols

		result = []
		for i in xrange(1, N):
			arg_list = []
			for j in range(COLS):
				arg_list.append(first_sheet.cell_value(i, j))
			entry = Geoinfo(memcache, *arg_list)
			if (entry.lat != 0):
				result.append(entry)
		return result

