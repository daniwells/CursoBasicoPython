import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except:
#except urllib.request.URLError:
    print("The site is don't available")
else:
    print('The site is open')
    print(site.read())
