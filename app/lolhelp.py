from urllib2 import Request, URLError, urlopen
import simplejson as json
import os
# Notice taht almost all the links are built in the same way!

DEV_KEY = "?api_key=" + os.getenv('LEAGUE_DEV_KEY', 'ARE YOU KIDDING ME?')
HEAD = "https://na.api.pvp.net/api/lol/"
REGION = "na/"
SUMMONER_VERSION = "v1.4/"
SUMMONER_API_BY_NAME = "summoner/by-name/"
MATCHHISTORY_VERSION = "v2.2/"
MATCHHISTORY = "matchhistory"

def get_summoner_data(input_name):

	URL = HEAD + REGION + SUMMONER_VERSION + SUMMONER_API_BY_NAME + input_name.replace(" ", "") + DEV_KEY
	try:
		url_request = Request(URL)
		response = urlopen(url_request)
		summoner_data = json.loads(response.read())[input_name.lower()]
	except Exception as e:
		# OMG I need to trust RIOT API at this time
		return None

	summoner_data['profileIconId'] = "http://ddragon.leagueoflegends.com/cdn/5.9.1/img/profileicon/" + str(summoner_data['profileIconId'])+ ".png"

	return summoner_data

def get_summoner_stat(summoner_data):
	# "https://na.api.pvp.net/api/lol/na/v2.5/league/by-summoner/28909887" + DEV_KEY
	URL = HEAD + REGION + "v2.5/league/by-summoner/" + str(summoner_data['id']) + "/entry" + DEV_KEY
	
	try:
		url_request = Request(URL)
		response = urlopen(url_request)
		summoner_stat = json.loads(response.read())
		user_id = str(summoner_data['id'])
		solo_queue = None
		for solo_queue in summoner_stat[user_id]:
			if solo_queue["queue"] == "RANKED_SOLO_5x5":
				return solo_queue
	except Exception as e:
		# OMG I need to trust RIOT API at this time
		solo_queue = None
	return solo_queue

def get_champs():
	HEAD = "https://global.api.pvp.net/api/lol/"
	URL = HEAD + "static-data/" + REGION + "v1.2/" + "champion" + DEV_KEY
	# "http://ddragon.leagueoflegends.com/cdn/5.9.1/img/champion/Aatrox.png" champion image
	# "http://ddragon.leagueoflegends.com/cdn/5.9.1/img/passive/Cryophoenix_Rebirth.png" passive image

	try:
		url_request = Request(URL)
		response = urlopen(url_request)
		champions = json.loads(response.read())
	except Exception as e:
		return None
	return champions['data']

def get_summoner_hisory(summoner_data):
	# https://na.api.pvp.net/api/lol/na/v2.2/matchhistory/28909887?rankedQueues=RANKED_SOLO_5x5&api_key=DEV_KEY
	URL = HEAD + REGION + 'v2.2/matchhistory/'+ str(summoner_data['id']) + "?rankedQueues=RANKED_SOLO_5x5&api_key=" + os.getenv('LEAGUE_DEV_KEY', 'ARE YOU KIDDING ME?')
	summoner_history = None
	spell_map = {	'1': "SummonerBoost", '12':"SummonerTeleport", '30': "SummonerPoroRecall",
				 	'14': "SummonerDot",  '32':"SummonerSnowball", '7':  "SummonerHeal",
				 	'11': "SummonerSmite", '3': 'SummonerExhaust', '31': 'SummonerPoroThrow',
				 	'13': "SummonerMana", '2': "SummonerClairvoyance", '21': "SummonerBarrier",
				 	'4': "SummonerFlash", '17': "SummonerOdinGarrison", '6':"SummonerHaste"}
	try:
		url_request = Request(URL)
		response = urlopen(url_request)
		summoner_history = json.loads(response.read())

	except Exception as e:
		# OMG I need to trust RIOT API at this time
		return None
	mini_summoner_history = []
	if "matches" in summoner_history:
		for match in summoner_history['matches']:
			match_info = {}
			match_info['spell1'] = spell_map[str(match["participants"][0]['spell1Id'])]
			match_info['spell2'] = spell_map[str(match["participants"][0]['spell2Id'])]
			match_info['championId'] = match["participants"][0]['championId'] 
			match_info['assists'] = match["participants"][0]['stats']['assists']
			match_info['kills'] = match["participants"][0]['stats']['kills']
			match_info['deaths'] = match["participants"][0]['stats']['deaths']
			if match["participants"][0]['stats']['winner']:
				match_info['winner'] = "Win"
			else:
				match_info['winner'] = "Lose"
			mini_summoner_history.append(match_info)
	return mini_summoner_history
