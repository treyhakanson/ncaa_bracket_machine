from bs4 import BeautifulSoup as bs
import urllib
import numpy as np
import os.path

class Player(object):

	# TODO: turn height into inches (int) and wt into int
	def __init__(self, arr):
		self.no = arr[0]
		self.name = arr[1]
		self.pos = arr[2]
		self.ht = arr[3]
		self.wt = arr[4]
		self.yr = arr[5]
		self.htwn = arr[6]

def make_player_url(playerName):
	playerRefBaseUrl = 'http://www.sports-reference.com/cbb/players/PLAYER_NAME.html'
	formattedPlayerName = playerName.replace(' ', '-', 1)
	playerUrl = playerRefBaseUrl.replace('PLAYER_NAME', formattedPlayerName, 1)
	return playerUrl

baseUrl = 'http://espn.go.com/mens-college-basketball/teams'
concatingUrl = 'http://espn.go.com'
allTeamUrls = np.empty((64,3), dtype=object)
allPlayers = np.zeros(64, dtype=object)

allGames = [['Kansas', 'Austin Peay'],['Colorado', 'UConn'], ['Maryland', 'South Dakota St'], ['Cal', 'Hawaii'], ['Arizona', 'Wichita State'], ['Miami', 'Buffalo'], ['Iowa', 'Temple'], ['Villanova', 'UNC Asheville'], ['Oregon', 'Southern'], ['Saint Joe\'s', 'Cincinnati'], ['Baylor', 'Yale'], ['Duke', 'UNC Wilmington'], ['Texas', 'Northern Iowa'], ['Texas A&M', 'Green Bay'], ['Oregon State', 'VCU'], ['Oklahoma', 'CSU Bakersfield'], ['UNC', 'FGCU'], ['USC', 'Providence'], ['Indiana', 'Chattanooga'], ['Kentucky', 'Stony Brook'], ['Notre Dame', 'Michigan'], ['West Virginia', 'SF Austin'], ['Wisconsin', 'Pitt'], ['Xavier', 'Weber State'], ['UVA', 'Hampton'], ['Texas Tech', 'Butler'], ['Purdue', 'AR-Little Rock'], ['Iowa State', 'Iona'], ['Seton Hall', 'Gonzaga'], ['Utah', 'Fresno State'], ['Dayton', 'Syracuse'], ['Michigan State', 'Mid Tennessee']]
allTeamsHTML = urllib.urlopen(baseUrl)
soup = bs(allTeamsHTML, 'lxml')

i = 0
j = 0

# check if the file exists before attempting to open it
if (os.path.isfile('all_team_urls.npy')):
	savedAllTeamsUrls = np.load('all_team_urls.npy')
else:
	savedAllTeamsUrls = np.zeros(0)

# rescrape team urls only if np array fails to load/is unavailable
if (savedAllTeamsUrls.size == 0):
	aArr = soup.select('a.bi')
	for a in aArr:
		for matchup in allGames:	
			for team in matchup:
				if (a.get_text() == team):
					for a in a.parent.parent.find('span').find_all('a'):
						allTeamUrls[i][j] = concatingUrl + a['href']
						j += 1
					i += 1
					j = 0
	np.save('all_team_urls.npy', allTeamUrls)
else:
	allTeamUrls = savedAllTeamsUrls

if (os.path.isfile('all_players.npy')):
	savedAllPlayers = np.load('all_players.npy')
	allPlayers = savedAllPlayers
else:
	savedAllPlayers = np.zeros(0)

for k, singleTeamUrls in enumerate(allTeamUrls, start=0):
	for i, url in enumerate(singleTeamUrls, start=0):
		# testHTML = urllib.urlopen(url)
		# urlSoup = bs(testHTML, 'lxml')
		if (i == 0):
			1
			# stats url
			# print 'pass'
		elif (i == 1):
			1
			# schedule url
			# print 'pass'
		else:
			#roster url
			if (savedAllPlayers.size == 0):
				testHTML = urllib.urlopen(url)
				urlSoup = bs(testHTML, 'lxml')
				trs = urlSoup.find_all('tr')[2:]
				playerArr = np.empty(len(trs), dtype=object)
				for i, tr in enumerate(trs, start=0):
					tmpArr = np.zeros(7, dtype=object)
					for j, td in enumerate(tr.find_all('td'), start=0):
						if (j == 3):
							tmpHt = td.get_text()
							if (len(tmpHt) > 1):
								if (tmpHt == '--'):
									tmpArr[j] == None
								else:
									ft = int(tmpHt[0])
									inc = int(tmpHt[2:])
									tmpArr[j] = ft*12 + inc
							else:
								ft = int(tmpHt[0])
								tmpArr[j] = ft*12
						elif (j == 4):
							tmpWt = td.get_text()
							if (tmpWt == '--'):
								tmpArr[j] = None
							else:
								tmpArr[j] = int(td.get_text())
						else:
							tmpArr[j] = td.get_text()
					playerArr[i] = Player(tmpArr)

	if (savedAllPlayers.size == 0):
		allPlayers[k] = playerArr
		np.save('all_players.npy', allPlayers)

for playerGroup in allPlayers:
	print '------------------'
	for player in playerGroup:
		playerUrl = make_player_url(player.name)
		print playerUrl













