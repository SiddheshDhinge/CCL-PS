import webapp2

class MainPage(webapp2.RequestHandler):
	def get(self):
		total = 8
		table = [None] * total
		table[0] = 0
		table[1] = 1
		for i in range(2, total):
			table[i] = table[i-1] + table[i-2]

		for i in range(total):
			self.response.out.write('%2d : %2d <hr>' % (i + 1, table[i]))

app = webapp2.WSGIApplication([('/', MainPage)], debug= True)
app.run()
