from urllib.request import*
import json
import requests
import random
from twilio.rest import Client

def part1():
	targetSite = "https://jluo117.github.io/workshop.json"
	myRequest = requests.get(targetSite, headers = {'User-agent': 'Chrome'})
	myJson = json.loads(myRequest.text)
	print("Today is: " + myJson['date'])
	print("Check in at " + myJson['Check in'])
#part 2
def sendMsg(msg):
	account_sid = "ACe704104c6f665965aeb765eea2a1502a"
	auth_token = "2aa7630860a97a3fb9de4ab53a94abc4"
	client = Client(account_sid, auth_token)
	client.api.account.messages.create(
        to="+14158109857",
        from_="+15108228362",
        body=msg,
        )
myIndex = random.randint(0, 25)
targetSite = "https://www.reddit.com/r/kpop.json"
myRequest = requests.get(targetSite ,headers = {'User-agent': 'Chrome'})
myJson = json.loads(myRequest.text)
#print(myJson)
children = myJson["data"]["children"]
Myoutput = (children[myIndex]["data"]["title"])
sendMsg(Myoutput)
part1()