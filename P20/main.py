import webapp2

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.out.write("<h1>Hello World</h1>")

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
app.run()
