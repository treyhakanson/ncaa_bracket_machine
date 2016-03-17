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
		self.team = arr[7]
		self.per = 0.0
		self.tm = 0
		self.advurl = ''
		self.made3s = 0.0
		self.per3s = 0.0

	def make_player_url(self):
		playerRefBaseUrl = 'http://www.sports-reference.com/cbb/players/PLAYER_NAME.html'

		addon = ''
		# addon = '-1'

		# for a specific cases 
		# (Temple player Levan Shawn Alston)
		if 'levan' in self.name.lower():
			formattedPlayerName = self.name.lower().replace('levan ', '')
		# (Temple player Ayan Nunez de Carvalho)
		elif 'nunez de carvalho' in self.name.lower():
			formattedPlayerName = self.name.lower().replace('nunez de carvalho', 'nunezdecarvalho')
		elif 'xeyrius' in self.name.lower():
			formattedPlayerName = self.name.lower().replace('xeyrius', 'xeryius')
		elif 'hamdy-mohamed' in self.name.lower():
			formattedPlayerName = self.name.lower().replace('hamdy-mohamed', 'hamdymohamed')
		elif 'jonathan nwankwo' in self.name.lower():
			formattedPlayerName = self.name.lower().replace('jonathan', 'johnathan')
		elif 'anthony lawrence' in self.name.lower():
			formattedPlayerName = self.name.lower().replace('anthony lawrence', 'anthony-lawrencejr')
		elif 'pflueger' in self.name.lower():
			formattedPlayerName = self.name.lower().replace('pflueger', 'pfleuger')
		elif 'mike sutton' in self.name.lower():
			formattedPlayerName = self.name.lower()
			addon = '-2'
		elif 'ishmail' in self.name.lower():
			formattedPlayerName = self.name.lower().replace('ishmail', 'ish')
		elif 'al freeman' in self.name.lower():
			formattedPlayerName = self.name.lower().replace('al', 'allerik')
		elif 'terry maston' in self.name.lower():
			formattedPlayerName = self.name.lower().replace('terry', 'tj')
		elif 'carlton bragg' in self.name.lower():
			formattedPlayerName = self.name.lower().replace('bragg', 'braggjr')
		elif 'eric davis' in self.name.lower():
			formattedPlayerName = self.name.lower().replace('davis', 'davisjr')
		elif 'kerwin roach' in self.name.lower():
			formattedPlayerName = self.name.lower().replace('roach', 'roachjr')
		elif 'ricky council' in self.name.lower():
			formattedPlayerName = self.name.lower().replace('council', 'councilii')
		elif 'yogi ferrell' in self.name.lower():
			formattedPlayerName = self.name.lower().replace('yogi', 'kevin')
		elif 'varun ram' in self.name.lower():
			formattedPlayerName = self.name.lower().replace('varun', 'varum')
		elif 'lourawls nairn' in self.name.lower():
			formattedPlayerName = self.name.lower().replace('lourawls', 'lourawls tum tum')
		elif 'conner george' in self.name.lower():
			formattedPlayerName = self.name.lower().replace('conner', 'connor')
		elif 'matt van dyk' in self.name.lower():
			formattedPlayerName = self.name.lower().replace('van dyk', 'vandyk')
		elif 'jon mckeeman' in self.name.lower():
			formattedPlayerName = self.name.lower().replace('jon', 'john')
		elif 'andy van vliet' in self.name.lower():
			formattedPlayerName = self.name.lower().replace('van vliet', 'vanvliet')
		elif 'chase miller' in self.name.lower():
			formattedPlayerName = self.name.lower()
			print 'CHASE MILLER DOESNT EXIST ON SPORTS REFERENCE'
		elif 'stephen strachan' in self.name.lower():
			formattedPlayerName = self.name.lower()
			print 'STEPHEN STRACHAN DOESNT EXIST ON SPORTS REFERENCE'
		elif 'aaron rountree' in self.name.lower():
			formattedPlayerName = self.name.lower().replace('rountree', 'roundtree')
		elif 'stefan duric' in self.name.lower():
			formattedPlayerName = self.name.lower()
			print 'STEFAN DURIC DOESNT EXIST ON SPORTS REFERENCE'
		elif 'david runcie' in self.name.lower():
			formattedPlayerName = self.name.lower()
			print 'DAVID RUNCIE DOESNT EXIST ON SPORTS REFERENCE'
		elif 'charles wilson' in self.name.lower():
			formattedPlayerName = self.name.lower().replace('charles', 'charle')
		elif 'tre houston' in self.name.lower():
			formattedPlayerName = self.name.lower()
			print 'TRE HOUSTON DOESNT EXIST ON SPORTS REFERENCE'
		elif 'eugene marshall' in self.name.lower():
			formattedPlayerName = self.name.lower()
			print 'EUGENE MARSHALL DOESNT EXIST ON SPORTS REFERENCE'
		elif 'anton grady' in self.name.lower():
			formattedPlayerName = self.name.lower()
			print 'ANTON GRADY DOESNT EXIST ON SPORTS REFERENCE'
		elif 'lionel ellison' in self.name.lower():
			formattedPlayerName = self.name.lower().replace('ellison', 'ellisoniii')
		elif 'jared savage' in self.name.lower():
			formattedPlayerName = self.name.lower().replace('savage', 'savag')
		elif 'okoroh' in self.name.lower():
			formattedPlayerName = self.name.lower().replace('okoroh', 'okorah')
		elif 'guzonjic' in self.name.lower():
			formattedPlayerName = self.name.lower().replace('kenan', 'kevin')
		elif 'malik martin' in self.name.lower():
			formattedPlayerName = self.name.lower().replace('malik', 'malik price')
		elif 'tai wynyard' in self.name.lower():
			formattedPlayerName = self.name.lower()
			print 'TAI WYNYARD DOESNT EXIST ON SPORTS REFERENCE'
		elif 'adrian rodgers' in self.name.lower():
			formattedPlayerName = self.name.lower().replace('rodgers', 'rogers')
			addon = '-2'
		elif 'd\'adrian allen' in self.name.lower():
			formattedPlayerName = self.name.lower().replace('d\'adrian', 'darian')
		elif 'pj posey' in self.name.lower():
			formattedPlayerName = self.name.lower().replace('pj', 'ravonn')
		else:
			formattedPlayerName = self.name.lower()
		formattedPlayerName = formattedPlayerName.replace(' jr.', '').replace(' sr.', '').replace(' iii', '').replace(' ii', '').replace('\'', '').replace('.', '').replace(' ', '-') + addon
		playerUrl = playerRefBaseUrl.replace('PLAYER_NAME', formattedPlayerName)
		return playerUrl

	def add_extra_metrics(self, soup, url):			
		per100trs = soup.select('#players_per_poss > tbody > tr')
		advancedTrs = soup.select('#players_advanced > tbody > tr')
		if (len(advancedTrs) == 0):
			self.per = 0.0
			self.tm = 0
			self.advurl = url
		else:
			lastTr = advancedTrs[len(advancedTrs) - 1]
			self.advurl = url
			if (lastTr.select('td')[5].get_text() != '' and lastTr.select('td')[4].get_text() != ''):
				self.per = float(lastTr.select('td')[5].get_text())
				self.tm = int(lastTr.select('td')[4].get_text())
			elif (lastTr.select('td')[5].get_text() == '' and lastTr.select('td')[4].get_text() != ''):
				self.per = 0.0
				self.tm = int(lastTr.select('td')[4].get_text())
			elif (lastTr.select('td')[5].get_text() != '' and lastTr.select('td')[4].get_text() == ''):
				self.per = float(lastTr.select('td')[5].get_text())
				self.mp = 0
			else:
				self.per = 0.0
				self.tm = 0
				self.advurl = url
			print self.per, self.tm,
		if (len(per100trs) == 0):
			self.made3s = 0.0
			self.per3s = 0.0
		else:
			lastTr = per100trs[len(per100trs) - 1]
			self.advurl = url
			if (lastTr.select('td')[11].get_text() != '' and lastTr.select('td')[13].get_text() != ''):
				self.made3s = float(lastTr.select('td')[11].get_text())
				self.per3s = float(lastTr.select('td')[13].get_text())
			elif (lastTr.select('td')[13].get_text() == '' and lastTr.select('td')[11].get_text() != ''):
				self.per3s = 0.0
				self.made3s = float(lastTr.select('td')[11].get_text())
			elif (lastTr.select('td')[13].get_text() != '' and lastTr.select('td')[11].get_text() == ''):
				self.per3s = float(lastTr.select('td')[13].get_text())
				self.made3s = 0.0
			else:
				self.made3s = 0.0
				self.per3s = 0.0
				self.advurl = url
			if (lastTr.select('td')[5].get_text() != ''):
				self.madefgs = float(lastTr.select('td')[5].get_text())
			else:
				self.madefgs = 0.0
			if (lastTr.select('td')[7].get_text() != ''):
				self.perfgs = float(lastTr.select('td')[7].get_text())
			else:
				self.perfgs = 0.0
			if (lastTr.select('td')[14].get_text() != ''):
				self.madefts = float(lastTr.select('td')[14].get_text())
			else:
				self.madefts = 0.0
			print self.made3s, self.per3s

	def set_per(self, num):
		self.per = num

	def set_tm(self, num):
		self.tm = num

baseUrl = 'http://espn.go.com/mens-college-basketball/teams'
concatingUrl = 'http://espn.go.com'
allTeamUrls = np.empty((64,3), dtype=object)
allPlayers = np.zeros(64, dtype=object)

allGames = [['Kansas', 'Austin Peay'],['Colorado', 'UConn'], ['Maryland', 'South Dakota St'], ['Cal', 'Hawaii'], ['Arizona', 'Wichita State'], ['Miami', 'Buffalo'], ['Iowa', 'Temple'], ['Villanova', 'UNC Asheville'], ['Oregon', 'Southern'], ['Saint Joe\'s', 'Cincinnati'], ['Baylor', 'Yale'], ['Duke', 'UNC Wilmington'], ['Texas', 'Northern Iowa'], ['Texas A&M', 'Green Bay'], ['Oregon State', 'VCU'], ['Oklahoma', 'CSU Bakersfield'], ['UNC', 'FGCU'], ['USC', 'Providence'], ['Indiana', 'Chattanooga'], ['Kentucky', 'Stony Brook'], ['Notre Dame', 'Michigan'], ['West Virginia', 'SF Austin'], ['Wisconsin', 'Pitt'], ['Xavier', 'Weber State'], ['UVA', 'Hampton'], ['Texas Tech', 'Butler'], ['Purdue', 'AR-Little Rock'], ['Iowa State', 'Iona'], ['Seton Hall', 'Gonzaga'], ['Utah', 'Fresno State'], ['Dayton', 'Syracuse'], ['Michigan State', 'Mid Tennessee']]

if (os.path.isfile('numpys/long_team_names.npy')):
	longTeamNames = np.load('numpys/long_team_names.npy')
	needsSave = False
else:
	longTeamNames = np.empty(0)

allTeamsHTML = urllib.urlopen(baseUrl)
soup = bs(allTeamsHTML, 'lxml')

i = 0
j = 0

# check if the file exists before attempting to open it
if (os.path.isfile('numpys/all_team_urls.npy')):
	savedAllTeamsUrls = np.load('numpys/all_team_urls.npy')
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
	np.save('numpys/all_team_urls.npy', allTeamUrls)
else:
	allTeamUrls = savedAllTeamsUrls

if (os.path.isfile('numpys/all_players.npy')):
	savedAllPlayers = np.load('numpys/all_players.npy')
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
			# schedule url
			if (longTeamNames.size == 0 or longTeamNames[63] == ''):
				needsSave = True
				longTeamNames = np.empty(64, dtype=str)
				print '********************'
				teamsPlayedInTourney = ''
				indexOfTeam = ''
				testHTML = urllib.urlopen(url)
				urlSoup = bs(testHTML, 'lxml')
				currTeamName = urlSoup.find('b').get_text()
				longTeamNames[k] = currTeamName
				print currTeamName.upper()
				trs = urlSoup.select('tr')
				lis = urlSoup.select('li.team-name')
				for j, li in enumerate(lis[:-1]):
					if (li.find('a') != None):
						vsTeamName = li.find('a').get_text()
					else:
						vsTeamName = li.get_text()
					for game in allGames:
						for team in game:
							if (team == vsTeamName):
								teamsPlayedInTourney += (vsTeamName + ',')
								indexOfTeam += (str(j) + ',')
				numTeamsPlayed = teamsPlayedInTourney.count(',')
				if (numTeamsPlayed != 0):
					teamsPlayedNumpy = np.empty((numTeamsPlayed, 4), dtype=object)
					indexOfTeamArr = indexOfTeam.split(',')
					for i, teamPlayed in enumerate(teamsPlayedInTourney.split(',')):
						if (teamPlayed != ''):
							teamsPlayedNumpy[i][0] = currTeamName
							teamsPlayedNumpy[i][1] = teamPlayed
							if (len(trs[int(indexOfTeamArr[i]) + 2].select('li.game-status')) > 1):
								teamsPlayedNumpy[i][2] = trs[int(indexOfTeamArr[i]) + 2].select('li.game-status')[1].get_text()
							else:
								teamsPlayedNumpy[i][2] = trs[int(indexOfTeamArr[i]) + 2].select('li.game-status')[0].get_text()
							teamsPlayedNumpy[i][3] = trs[int(indexOfTeamArr[i]) + 2].select('li.score')[0].get_text()
					saveName = 'numpys/' + currTeamName.lower().replace(' ', '_') + '_schedule.npy'
					np.save(saveName, teamsPlayedNumpy)
					print saveName
					print teamsPlayedNumpy
				else:
					print currTeamName + ' played no teams in the tournament.'
				print '********************'
		else:
			#roster url
			if (savedAllPlayers.size == 0):
				testHTML = urllib.urlopen(url)
				urlSoup = bs(testHTML, 'lxml')
				trs = urlSoup.find_all('tr')[2:]
				playerArr = np.empty(len(trs), dtype=object)
				for i, tr in enumerate(trs, start=0):
					tmpArr = np.zeros(8, dtype=object)
					tmpArr[7] = urlSoup.find('b').get_text()
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
		np.save('numpys/all_players.npy', allPlayers)
if (needsSave):
	np.save('numpys/long_team_names.npy', longTeamNames)

if (savedAllPlayers.size == 0):
	if (allPlayers[63][0].advurl == None or allPlayers[63][0].advurl == ''):
		for i, playerGroup in enumerate(allPlayers):
			print '------------------'
			for j, player in enumerate(playerGroup):
				playerUrl = player.make_player_url()
				url = urllib.urlopen(playerUrl)
				playerSoup = bs(url, 'lxml')
				print playerUrl,
				if (playerSoup.find('h1') != None):
					# ON THE CORRECT PAGE
					player.add_extra_metrics(playerSoup, playerUrl)
					print playerSoup.find('h1').get_text()
				else:
					if (playerSoup.select('#search_results > tbody > tr') == None):
						print '********CHECK URL**********'
					else:
						trs = playerSoup.select('#search_results > tbody > tr')
						if (len(trs) != 0):
							desiredPlayerTr = trs[len(trs) - 1]
							playerHref = desiredPlayerTr.select('a')[0]['href']
							playerUrl = 'http://www.sports-reference.com' + playerHref
							print playerUrl,
							newPlayerUrl = urllib.urlopen(playerUrl)
							newPlayerSoup = bs(newPlayerUrl, 'lxml')
							if (newPlayerSoup.find('h1') != None):
								# ON THE CORRECT PAGE
								player.add_extra_metrics(newPlayerSoup, playerUrl)
								print newPlayerSoup.find('h1').get_text()
							else:
								print '********CHECK URL**********'
						else:
							playerUrl = playerUrl.replace('.html', '-1.html')
							newPlayerUrl = urllib.urlopen(playerUrl)
							newPlayerSoup = bs(newPlayerUrl, 'lxml')
							print playerUrl,
							if (newPlayerSoup.find('h1') != None):
								# ON THE CORRECT PAGE
								player.add_extra_metrics(newPlayerSoup, playerUrl)
								print newPlayerSoup.find('h1').get_text()
							else:
								print '********CHECK URL**********'
				allPlayers[i][j] = player
		if (savedAllPlayers.size == 0):
			np.save('numpys/all_players.npy', allPlayers)

# PRINT STATEMENT FOR PLAYERS
for i, team in enumerate(allPlayers):
	print '\n************************'
	print team[0].team.upper()
	print '************************'
	for j, player in enumerate(team):
		print player.name
		print str(player.ht) + '\t',
		print str(player.wt) + '\t',
		print str(player.pos) + '\t',
		print str(player.per) + '\t',
		print str(player.made3s) + '\t',
		print str(player.per3s) + '\t',
		print str(player.tm) + '\n'
	print '************************\n'
	print '************************\n'

# IF STATEMENT FOR PLAYERS WHO HAD NO ADVANCED STATISTICS
# if (player.name.lower() == 'chase miller' 
# 			or player.name.lower() == 'stephen strachan' 
# 			or player.name.lower() == 'stefan duric' 
# 			or player.name.lower() == 'david runcie'
# 			or player.name.lower() == 'tre houston'
# 			or player.name.lower() == 'eugene marshall iii'
# 			or player.name.lower() == 'anton grady'
# 			or player.name.lower() == 'tai wynyard'):

# for team in longTeamNames:
# 	print team.lower()











