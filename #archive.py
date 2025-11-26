import webbrowser 
import json 
from urllib.request import urlopen #we import only the function "urlopen" from the library "urllib.request"

print("lets find an old website")
site = input("type a website URL:")
era = input("type a year, month, day, like 20150613:")
url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era)
response = urlopen(url) 
contents = response.read()
text = contents.decode("utf-8")
data = json.loads(text)
try:
    old_site = data["archived_snapshots"]["closest"]["url"] 
    print("Found this copy:", old_site)
    print("It should appear in your browser now.")
    webbrowser.open(old_site)
except:
    print("Sorry, no luck finding", site)  