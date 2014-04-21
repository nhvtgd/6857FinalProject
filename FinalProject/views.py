# Create your views here.
from django.http import HttpResponse
import urllib2
import requests
def main_page(request):
    req = urllib2.Request('http://web.mit.edu/6.033/www/schedule.shtml')
    response = urllib2.urlopen('https://www.bankofamerica.com')
    '''output = u
       <html>
         <head><title>%s</title></head>
         <body>
           <h1>%s</h1><p>%s</p>
         </body>
       </html>
        % (
       u'Django Bookmarks',
       u'Welcome to Django Bookmarks',
       u'Where you can store and share bookmarks!'
       )'''
    #req = urllib2.Request('https://online.citibank.com/')
    #response = urllib2.urlopen(req)
    the_page = response.read()
    r = requests.get('http://www.github.com/login')
    return HttpResponse(r.text)




