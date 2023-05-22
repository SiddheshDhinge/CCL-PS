import webapp2
import json
import urllib
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
	def get(self):
		path = './template/index.html'
		self.response.out.write(template.render(path, {}))
	
	def post(self):
		latitude = self.request.get("latitude")
		longitude = self.request.get("longitude")

		request = 'https://api.open-meteo.com/v1/forecast?latitude=%s&longitude=%s&current_weather=true' % (latitude, longitude)
		response = urllib.urlopen(request).read()
		data = json.loads(response)

		opPath = './template/op.html'
		self.response.out.write(template.render(opPath, {'data': data}))
		


app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
app.run()
