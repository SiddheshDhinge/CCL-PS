import webapp2

class MainPage(webapp2.RequestHandler):
	def get(self):
		name = 'Siddhesh Avinash Dhinge'
		rollNo = 33310
		dept = 'IT'
		
		for i in range(5):
			self.response.out.write('Name: %s <br>Roll: %d <br>Dept: %s <hr>' % (name, rollNo, dept))
			

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
app.run()
