import urllib
import simplejson as json
import os
from urllib2 import Request, URLError, urlopen
target_url = "http://ddragon.leagueoflegends.com/cdn/5.2.1/img/champion/"
DEV_KEY = "?api_key=" + os.getenv('LEAGUE_DEV_KEY', 'ARE YOU KIDDING ME?')
HEAD = "https://na.api.pvp.net/api/lol/"
REGION = "na/"
SUMMONER_VERSION = "v1.4/"
SUMMONER_API_BY_NAME = "summoner/by-name/"
MATCHHISTORY_VERSION = "v2.2/"
MATCHHISTORY = "matchhistory"

HEAD = "https://global.api.pvp.net/api/lol/"
URL = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion?champData=image&api_key="+os.getenv('LEAGUE_DEV_KEY', 'ARE YOU KIDDING ME?')
try:
	url_request = Request(URL)
	response = urlopen(url_request)
	champions = json.loads(response.read())
except Exception as e:
	print e
	# OMG I need to trust RIOT API at this time
	champions = None

print champions

testfile = urllib.URLopener()

# get champions image
target = "http://ddragon.leagueoflegends.com/cdn/5.9.1/img/champion/"

# if not os.path.exists("champions"):
#     os.makedirs("champions")
# for champ in champions['data']:
# 	name = champions['data'][champ]['image']['full']
# 	testfile.retrieve(target + name, "champions/" + str(champions['data'][champ]['id']) + ".png")
# 	testfile.retrieve(target + name, "champions/" +name)

# get tiers image

target = "http://www.leagueofgraphs.com/img/league-icons/160/"
if not os.path.exists("tiers"):
    os.makedirs("tiers")
for i in range(7):
	current_index = i + 1
	# for diamonds and below
	if current_index < 6:
		for j in range(5):
			name = str(current_index) + '-' + str(j + 1)+'.png'
			testfile.retrieve(target + name, "tiers/" + name)
	else:
		 name = str(current_index) + '-' +'1.png'
		 testfile.retrieve(target + name, "tiers/" + name)
testfile.retrieve(target + "0-0.png", "tiers/" + "0-0.png")
