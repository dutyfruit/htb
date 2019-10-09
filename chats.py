import json
import requests
from parse import parse
import warnings

headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'}

warnings.filterwarnings("ignore")
apikey = ""
def get_message():
	r = requests.post("https://www.hackthebox.eu/api/shouts/get/initial/html/100?api_token="+apikey)
	js = json.loads(r.content)
	html = js['html']
	lastmsg = html[99]
	for x in html:
		if 'https://www.hackthebox.eu/storage/avatars/' in x:
			parse(x)

quite = True

def get_last_message(quite):
	while True:
		r = requests.post("https://www.hackthebox.eu/api/shouts/get/initial/html/1?api_token="+apikey)
		js = json.loads(r.content)
		html = js['html'][0]
		if quite == True:
			if 'https://www.hackthebox.eu/storage/avatars/' in html:
				if html != lastmsg:
					parse(html)
					lastmsg = html
		else:
			if html != lastmsg:
				parse(html)
				lastmsg = html
