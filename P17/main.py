import webapp2
import urllib
import json
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
	def get(self):
		path = './template/page.html'
		self.response.out.write(template.render(path, {}))
	
	def post(self):
		zipCode = self.request.get('zip')
		branchName = self.request.get('branch')
		request = ''
		if(self.request.get('fetchBy') == 'ZIP'):
			request = 'https://api.postalpincode.in/pincode/' + zipCode
		else:
			request = 'https://api.postalpincode.in/postoffice/' + branchName
		
		response = urllib.urlopen(request).read()
		data = json.loads(response)[0]
		
		if(data['Status'] == 'Error'):
			self.response.out.write("Error")
		else:
			pagePath = './template/op.html'
			self.response.out.write(template.render(pagePath, {"data": data}))

		
app = webapp2.WSGIApplication([('/', MainPage)], debug= True)
app.run()



