import sys
import csv

class Crawler:


	def __init__(self):
		pass

		self.kpis = {}


	def crawl(self, path, weeks, positives, negatives, how, group_name):

		for week in weeks:

			filepath = path + '/' + 'kw' + str(week) + '.csv'
			
			with open(filepath, 'rb') as csvfile:
				
				csvfiletoread = csv.reader(csvfile, delimiter = ',')
				for row in csvfiletoread:

					# the first row it is just bullshit from adwords, I have to jump it
					if len(row) > 1 and row[0] != 'Search Result Type':

####################################################################################

						# KEYWORD MAGIC
							# 4 dif reports, init, consolidated_init, just, consolidated_just

####################################################################################


						if how == 'init' and (any(element in row[1] for element in positives)) and (any(element not in row[1] for element in negatives)):
							print str(week) + ' ' + row[1]

							self.magic_crawl(row, week, how, group_name)

		

						
						elif how == 'consolidated_init' and (any(element in row[1] for element in positives)) and (any(element not in row[1] for element in negatives)):
							print str(week) + ' ' + row[1]

							self.magic_crawl(row, week, how, group_name)



						elif how == 'just' and (any(element == row[1] for element in positives)):	
							print str(week) + ' ' + row[1]

							self.magic_crawl(row, week, how, group_name)



						elif how == 'consolidated_just' and (any(element == row[1] for element in positives)):
							print str(week) + ' ' + row[1]

							self.magic_crawl(row, week, how, group_name)


		print self.kpis


	def magic_crawl(self, row, week, how, group_name):


		# define keyword vs group_name
		if (how == 'init') or (how == 'just'):

			keyword = row[1]

		elif (how == 'consolidated_init') or (how == 'consolidated_just'):

			keyword = group_name


	# check if keyword exists & update if not
		if keyword not in self.kpis:

	# the ctr is always tricky to set becaused x / 0
			try: 	
				ctr = round(float(row[7]) / float(row[8]), 2)

			except:
				ctr = 0.0

	# update the self.kpis
			self.kpis.update({keyword: {
				'clicks': {week: float(row[7])},
				'impressions': {week: float(row[8])},
				'rankingbruto': {week: (float(row[8]) * float(row[11]))},
				'ranking': {week: float(row[11])},
				'ctr': {week: ctr}}})

	# check if week exists & pass values
		elif week in self.kpis[keyword]['clicks']:

			self.kpis[keyword]['clicks'][week] = self.kpis[keyword]['clicks'][week] + float(row[7])
			self.kpis[keyword]['impressions'][week] = self.kpis[keyword]['impressions'][week] + float(row[8])
			self.kpis[keyword]['rankingbruto'][week] = self.kpis[keyword]['rankingbruto'][week] + (float(row[8]) * float(row[11]))
			
			try:
				self.kpis[keyword]['ranking'][week] = float(self.kpis[keyword]['rankingbruto'][week] / self.kpis[keyword]['impressions'][week])
			except:
				self.kpis[keyword]['ranking'][week] = 0.0
			try:
				self.kpis[keyword]['ctr'][week] = float(self.kpis[keyword]['clicks'][week] / self.kpis[keyword]['impressions'][week])
			except:
				self.kpis[keyword]['ctr'][week] = 0.0


		# if not then I update
		else:

			try: 
				ctr = float(row[7]) / float(row[8])
			except:
				ctr = 0.0

			self.kpis[keyword]['clicks'].update({week: float(row[7])})
			self.kpis[keyword]['impressions'].update({week: float(row[8])})
			self.kpis[keyword]['rankingbruto'].update({week: float(row[8]) * float(row[11])})
			self.kpis[keyword]['ranking'].update({week: float(row[11])})
			self.kpis[keyword]['ctr'].update({week: ctr})













