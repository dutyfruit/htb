#!/usr/bin/python
from os import system, getcwd
from getpass import getpass
import requests
import json
try:
	from bs4 import BeautifulSoup
except:
	system("pip install bs4")
	from bs4 import BeautifulSoup

print "\033[96m[+] \033[92mDutyfruit"
print "\033[96m[+] \033[92mhtb: https://www.hackthebox.eu/home/users/profile/12057"
print "\033[96m[+] \033[92mSiteWeb : rootinjail.com"

headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'}

session = requests.Session()
response = session.get('https://www.hackthebox.eu/login', headers=headers)


cookie = session.cookies.get_dict()
html = BeautifulSoup(response.content, 'lxml')
token = html.body.find('input', attrs={'type':'hidden'})['value']
email = 'dutyfruit1@outlook.com'#raw_input("Email: ")
password = getpass("password: ")
session2 = requests.Session()
response2 = session2.post('https://www.hackthebox.eu/login', data={"_token":token, "email":email, "password":password, "remember":"on"}, cookies=cookie, headers=headers)
cookie2 = session2.cookies.get_dict()
if 'hackthebox.eu/home' not in response2.content:
	exit("[+] Enter a valid email and password!")
file = open("cookies.txt","w")
file.write(json.dumps(cookie2))
file.close()
file = open("cookies.txt","r")
cont = file.read()
f = json.loads(cont)
r = requests.get("https://hackthebox.eu/home/hof", cookies=f,headers=headers)
content = r.content
num = content.find("api_token=")
api_key = content[num+10:num+70]
print "\033[96m[+] \033[92mDownloading HTB vpn"
vpd = requests.get('https://www.hackthebox.eu/home/htb/access/ovpnfile', cookies=f,headers=headers)
ovpn = open('/root/Desktop/pentest/htb/htb.ovpn', 'w')
ovpn.write(vpd.content)
ovpn.close()
print "\033[96m[+] \033[92mDownloaded"
textsearch = "MYAPIKEY"
with open('chats.py', 'r') as file :
  filedata = file.read()

filedata = filedata.replace(textsearch, api_key)
with open('chats.py', 'w') as file:
  file.write(filedata)
pwd = getcwd()
textsearch = "MYVPNFILE"
with open('htb.py', 'r') as file :
  filedata = file.read()

filedata = filedata.replace(textsearch, pwd+"/htb.ovpn")
with open('htb.py', 'w') as file:
  file.write(filedata)
system('pip install netifaces')
system('chmod +x htb.py')
system("sudo apt -y install openvpn")
system('sudo ln -s `pwd`/htb.py /usr/bin/htb')
print "\033[96m[+] \033[92mSetup Successful"
print "\033[96m[+] \033[92mType htb on your terminal"
