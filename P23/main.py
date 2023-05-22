import webapp2

class MainPage(webapp2.RequestHandler):
	def get(self):
		for i in range(1, 11):
			self.response.out.write("5 * %2d = %2d <hr>" % (i, 5*i))

app = webapp2.WSGIApplication([('/', MainPage)], debug= True)
app.run()
