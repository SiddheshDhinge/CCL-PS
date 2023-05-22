import webapp2
import json
import urllib
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
	def get(self):
		path = './template/index.html'
		self.response.out.write(template.render(path, {}))
	
	def post(self):
		search = self.request.get('search')
		api = 'http://universities.hipolabs.com/search?name=' + search
		response = urllib.urlopen(api).read()
		data = json.loads(response)
		opPath = './template/op.html'
		self.response.out.write(template.render(opPath, {'data': data}))



app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
app.run()
