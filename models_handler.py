def populate_CSV_model(self, week, CSV_model):

	# I instanciate the model


	self.CSV = model.CSV()

	self.CSV.data = self.Parser.return_keywords_with_kpis(self.User.variables['path'], week)



def populate_keyword_model(self, keyword, weeks, Keyword_model, CSV_model):


	# I create the model for passing keywords
	self.Keyword = Keyword_model

	# self.Keyword.weeks = self.User.variables['weeks']
	self.Keyword.weeks = weeks

	# for each week I get the KPIs and pass them to the model
	for week in weeks:

		clicks = 0
		impressions = 0
		ranking = 0
		rankingbruto = 0
		ctr = 0

		# first populate the CSV_model
		self.populate_CSV_model(week, CSV_model)

		for key in self.CSV.data:
			if key == keyword:

				print self.CSV.data[key]['clicks']
				clicks = clicks + self.CSV.data[key]['clicks']
				impressions = impressions + self.CSV.data[key]['impressions']
				rankingbruto = float(rankingbruto + float(self.CSV.data[key]['impressions']) *
					float(self.CSV.data[key]['ranking']))

		# I calculate the ctr
		try: 
			ctr = round(float(clicks) / float(impressions), 2)

		# and the ranking
			ranking = round(float(rankingbruto) / impressions, 2)

		except:
			pass


		# then get pass the week kpis to the keyword model
		self.Keyword.insert_kpi('clicks', week, clicks)
		self.Keyword.insert_kpi('impressions', week, impressions)
		self.Keyword.insert_kpi('ranking', week, ranking)
		self.Keyword.insert_kpi('ctr', week, ctr)

		# done

	return self.Keyword.kpis

def populate_category_model(self, keywords):

	# I create an instance of Category
	self.Category = model.Category()

	# for each keyword I have to run a self.single_keyword
	# for keyword in self.User.variables['multiple_keywords']:
	for keyword in keywords:

		self.populate_keyword_model(keyword)
		self.Category.add_keyword_with_kpis(keyword, kpis)

	print self.Category.kpis
