def define_the_keywords(self):

	for element in self.elements:

		for week in self.User.get('weeks'):

			# restore & populate the CSV
			self.CSV.restore(self.User.get('path'), week)
			self.CSV.adwords_populate()

			# extract the keywords and pass them to elements
			keywords_in_CSV = self.CSV.return_all_keywords()

			for keyword in keywords_in_CSV:
				if element in keyword:
					self.elements[element].append(keyword)

	for element in elements:
		elements[element] = list(set(elements[element])
