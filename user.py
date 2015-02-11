import os
import config


class Input:

	def __init__(self):


		self.variables = {

			# 'seosem': 'seo',
			'reporttype': 'categories',
			'single_keyword': 'kontaktlinsen',
			'multiple_keywords': ['kontaktlinsen', 'brillen', 'brille', 'sonnenbrillen'],
			'category': '',
			'country_folder': 'de',
			'weeks': [41, 42],
			'path': r'/Users/andres/Documents/python/np/np2.0/de/2014',
			'filename_of_report': 'testing.csv',
		}

		###########################################
		####### FOR TESTING REASONS I JUST BLOCK THE SHOOTER AND USE THE PRE variables
		###########################################
		
		#self.shoot_console_questions()


	def console_questions(self):

		#seo/sem/both
		# while True:
		# 	self.variables['seosem'] = raw_input('insert the channel (seo / sem / both):' )
		# 	if self.variables['seosem'] == 'seo' or self.variables['seosem'] == 'sem' or self.variables['seosem'] == 'both':
		# 		break
		# 	else:
		# 		print '\n\n'
		# 		print 'the value you included is wrong, you have to select a proper channel'
				


		
		###########################################
		#######-----report type
		###########################################
		while True:
			# I print all the report types I have and then I ask for input

			for type_of_report in config.variables['reports']:
				print type_of_report

			self.variables['reporttype'] = raw_input("insert the report you want: ")

			if self.variables['reporttype'] in config.variables['reports']:
				break
			
			else:
				print '\n\n'
				print 'you didnt write a correct report name'
				
		

		#extra questions

		if self.variables['reporttype'] == 'single keyword':
			self.variables['single_keyword'] = raw_input('insert the keyword that you want to track:' )
			self.variables['single_keyword'] = self.variables['single_keyword'].strip()

		elif self.variables['reporttype'] == 'multiple keywords':
			while True:
				self.variables['multiple_keywords'] = raw_input('insert the keywords that you want to track separated by commas (brillen, sonnenbrillen, online brillen: ')

				if ',' in self.variables['multiple_keywords']:
					self.variables['multiple_keywords'] = self.variables['multiple_keywords'].split(',')

					i = 0
					for singlekeyword in self.variables['multiple_keywords']:
						self.variables['multiple_keywords'][i] == singlekeyword.strip()
						i = i + 1
					break

				else:
					print '\n\n'
					print 'you didnt separate the keywords with commas'
					

		elif self.variables['reporttype'] == 'full category':

			while True:

				print 'list of keyword categories: '
				for single_category in config.variables['path']:
					print single_category

				self.variables['category'] = raw_input('for which category you want to have all the keywords: ')

				if self.variables['category'] in config.variables['path']:
					break

				else:
					print '\n\n'
					print 'you didnt include a correct category'
					

		###########################################
		#######-----paths and folders
		###########################################

		# question for everybody:
		self.variables['country_folder'] = raw_input('insert the country folder (de / es / fr or fr\\2013):' )
		self.variables['path'] = config.variables['path'] + self.variables['country_folder']
	

		weeks = raw_input('insert the weeks that you want in the report (41, 42, 43): ')
		#convert the weeks on array with integers instead of with strings
		weeks = weeks.replace(' ', '')

		if '-' in weeks:
			weeks = weeks.split('-')
			firstweek = int(weeks[0])
			lastweek = int(weeks[1])
			
			while firstweek <= lastweek:
				self.variables['weeks'].append(firstweek)
				firstweek = firstweek + 1
		else:
			self.variables['weeks'] = weeks.split(',')

		i = 0
		for week in self.variables['weeks']:
			self.variables['weeks'][i] = int(week)
			i = i + 1

		self.variables['filename_of_report'] = raw_input('insert the name of the file where you want the report (example.csv). The file must not exist yet: ')
		# self.filepathwhere = config.variables['path'] + self.variables['filename_of_report']



		# I print all the values and ask if they are right:
		print '\n\n'
		print "------------------------------"
		print "THESE ARE THE VALUES THAT YOU PROVIDED:"
		print "------------------------------"
		# print "the channel is:----------"   + str(self.variables['seosem']) 
		print "the report is :----------"   + str(self.variables['reporttype'])
		print "the single keyword is: --"   + str(self.variables['single_keyword'])
		print "the keywords are:--------"   + ', '.join(self.variables['multiple_keywords'])
		print "the category is:---------"   + str(self.variables['category'])
		print "the country_folder is: --"   + str(self.variables['country_folder'])
		print "the weeks are:-----------"   + str(self.variables['weeks']).strip()
		print "the files are in---------"   + self.variables['path']
		print "the filename is:---------"   + self.variables['filename_of_report']
		print "the file will be save on:"   + config.variables['path'] + self.variables['filename_of_report']

		
		###########################################
		#######----- shooting
		###########################################

	## if the user decide not to go for it, then it starts again
	def shoot_console_questions(self):
		while True:
			self.console_questions()
			goforit = raw_input('do you want to create the report? (yes/no): ')
			if goforit == 'yes':
				break 
			else:
				print '\n\n'
				print 'the report wasnt created, lets start again'

	def get(self, kpi):
		return self.variables[kpi]



