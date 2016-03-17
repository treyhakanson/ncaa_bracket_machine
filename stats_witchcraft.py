import statsmodels.api as sm
import numpy as np
from sklearn.decomposition import PCA
import pandas as pd
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

def convertYrToFloat(yr):
	if (yr == 'FR'):
		return float(1)
	elif (yr == 'SO'):
		return float(2)
	elif (yr == 'JR'):
		return float(3)
	elif (yr == 'SR'):
		return float(4)
	else:
		print 'you done fucked up'

allTeams = ['Kansas', 'Austin Peay','Colorado', 'UConn', 'Maryland', 'South Dakota St', 'Cal', 'Hawaii', 'Arizona', 'Wichita State', 'Miami', 'Buffalo', 'Iowa', 'Temple', 'Villanova', 'UNC Asheville', 'Oregon', 'Southern', 'Saint Joe\'s', 'Cincinnati', 'Baylor', 'Yale', 'Duke', 'UNC Wilmington', 'Texas', 'Northern Iowa', 'Texas A&M', 'Green Bay', 'Oregon State', 'VCU', 'Oklahoma', 'CSU Bakersfield', 'UNC', 'FGCU', 'USC', 'Providence', 'Indiana', 'Chattanooga', 'Kentucky', 'Stony Brook', 'Notre Dame', 'Michigan', 'West Virginia', 'SF Austin', 'Wisconsin', 'Pitt', 'Xavier', 'Weber State', 'UVA', 'Hampton', 'Texas Tech', 'Butler', 'Purdue', 'AR-Little Rock', 'Iowa State', 'Iona', 'Seton Hall', 'Gonzaga', 'Utah', 'Fresno State', 'Dayton', 'Syracuse', 'Michigan State', 'Mid Tennessee']

longTeamNames = ['kansas_jayhawks', 'austin_peay_govenors', 'colorado_buffaloes', 'connecticut_huskies', 'maryland_terrapins', 'south_dakota_state_jackrabbits', 'california_golden_bears', 'hawaii_rainbow_warriors', 'arizona_wildcats', 'wichita_st_shockers', 'miami_hurricanes', 'buffalo_bulls', 'iowa_hawkeyes', 'temple_owls', 'villanova_wildcats', 'unc_asheville_bulldogs', 'oregon_ducks', 'this_should_not_load', 'saint_joeseph\'s_hawks', 'cincinnati_bearcats', 'baylor_bears', 'yale_bulldogs', 'duke_blue_devils', 'this_should_not_load', 'texas_longhorns', 'northern_iowa_panthers', 'texas_a&m_aggies', 'green_bay_phoenix', 'oregon_state_beavers', 'vcu_rams', 'oklahoma_sooners', 'csu_bakersfield_roadrunners', 'north_carolina_tar_heels', 'florida_gulf_coast_eagles', 'usc_trojans', 'providence_friars', 'indiana_hoosiers', 'chattanooga_mocs', 'kentucky_wildcats', 'stony_brook_seawolves', 'notre_dame_fighting_irish', 'michigan_wolverines', 'west_virginia_mountaineers', 'stephen_f._austin_lumberjacks', 'wisconsin_badgers', 'pittsburgh_panthers', 'xavier_musketeers', 'this_should_not_load', 'virginia_cavaliers', 'hampton_pirates', 'texas_tech_red_raiders', 'butler_bulldogs', 'purdue_boilermakers', 'arkansas-little_rock_trojans', 'iowa_state_cyclones', 'iona_gaels', 'seton_hall_pirates', 'gonzaga_bulldogs', 'utah_utes', 'fresno_state_bulldogs', 'dayton_flyers', 'syracuse_orange', 'michigan_state_spartans', 'middle_tennessee_blue_raiders']

convertTeamNames = {}
for (k,v) in enumerate(allTeams):
	print allTeams[k], ' : ', longTeamNames[k]
	convertTeamNames[allTeams[k]] = longTeamNames[k]

allGames = [['Kansas', 'Austin Peay'], ['Colorado', 'UConn'], ['Maryland', 'South Dakota St'], ['Cal', 'Hawaii'], ['Arizona', 'Wichita State'], ['Miami', 'Buffalo'], ['Iowa', 'Temple'], ['Villanova', 'UNC Asheville'], ['Oregon', 'Southern'], ['Saint Joe\'s', 'Cincinnati'], ['Baylor', 'Yale'], ['Duke', 'UNC Wilmington'], ['Texas', 'Northern Iowa'], ['Texas A&M', 'Green Bay'], ['Oregon State', 'VCU'], ['Oklahoma', 'CSU Bakersfield'], ['UNC', 'FGCU'], ['USC', 'Providence'], ['Indiana', 'Chattanooga'], ['Kentucky', 'Stony Brook'], ['Notre Dame', 'Michigan'], ['West Virginia', 'SF Austin'], ['Wisconsin', 'Pitt'], ['Xavier', 'Weber State'], ['UVA', 'Hampton'], ['Texas Tech', 'Butler'], ['Purdue', 'AR-Little Rock'], ['Iowa State', 'Iona'], ['Seton Hall', 'Gonzaga'], ['Utah', 'Fresno State'], ['Dayton', 'Syracuse'], ['Michigan State', 'Mid Tennessee']]

allPlayers = np.load('numpys/all_players.npy')

positions = ['C', 'F', 'G']

# longTeamNames = np.load('./numpys/long_team_names.npy')

allTeamsStats = {}

for team in allPlayers:
	tempStats = {'CHeight':0, 'CWeight': 0, 'CPER': 0, 'CYear': 0, 'FHeight':0, 'FWeight': 0, 'FPER': 0, 'FYear': 0, 'GHeight':0, 'GWeight': 0, 'GPER': 0, 'GYear': 0}

	totalTeamMinutes = 0
	for player in team:
		totalTeamMinutes += player.tm

	for player in team:
		if (player.pos == 'G-F'):
			forwardWeight = (float(player.ht)-float(68))/float(84)
			playtimeWeight = float(player.tm)/float(totalTeamMinutes)

			tempStats['FHeight'] += float(player.ht) * playtimeWeight * forwardWeight
			tempStats['FWeight'] += float(player.wt) * playtimeWeight * forwardWeight
			tempStats['FPER'] += float(player.per) * playtimeWeight * forwardWeight
			tempStats['FYear'] += convertYrToFloat(player.yr) * playtimeWeight * forwardWeight

			tempStats['GHeight'] += float(player.ht) * playtimeWeight * (float(1) - forwardWeight)
			tempStats['GWeight'] += float(player.wt) * playtimeWeight * (float(1) - forwardWeight)
			tempStats['GPER'] += float(player.per) * playtimeWeight * (float(1) - forwardWeight)
			tempStats['GYear'] += convertYrToFloat(player.yr) * playtimeWeight * (float(1) - forwardWeight)
		else:
			positionIndex = 3
			if (player.pos == 'F'):
				positionIndex = 1
			elif (player.pos == 'G'):
				positionIndex = 2
			elif (player.pos == 'C'):
				positionIndex = 0
			else:
				pass

			try:
				playtimeWeight = float(player.tm)/float(totalTeamMinutes)

				tempStats[positions[positionIndex] + 'Weight'] += float(player.wt) * playtimeWeight
				tempStats[positions[positionIndex] + 'Height'] += float(player.ht) * playtimeWeight
				tempStats[positions[positionIndex] + 'PER'] += float(player.per) * playtimeWeight
				tempStats[positions[positionIndex] + 'Year'] += convertYrToFloat(player.yr) * playtimeWeight
			except:
				if (player.name == 'Reginald Johnson Jr.'):
					playtimeWeight = float(player.tm)/float(totalTeamMinutes)
					tempStats['FHeight'] += float(player.ht) * playtimeWeight
					tempStats['FWeight'] += float(225) * playtimeWeight
					tempStats['FPER'] += float(player.per) * playtimeWeight
					tempStats['FYear'] += float(2) * playtimeWeight
				if (player.name == 'Kyle Ferreira'):
					playtimeWeight = float(player.tm)/float(totalTeamMinutes)
					tempStats['GHeight'] += float(player.ht) * playtimeWeight
					tempStats['GWeight'] += float(175) * playtimeWeight
					tempStats['GPER'] += float(player.per) * playtimeWeight
					tempStats['GYear'] += convertYrToFloat(player.yr) * playtimeWeight

	allTeamsStats[team[0].team.lower().replace(' ', '_')] = tempStats


for (_,team) in enumerate(allTeamsStats):
	print team, ' : ', allTeamsStats[team]['CYear']

allTeamsTestGameWins = []
allTeamsTestGameStats = [{}]

for (k,team) in enumerate(longTeamNames):
	print 'numpys/' + team.lower().replace(' ', '_') + '_schedule.npy'
	if (os.path.isfile('numpys/' + team + '_schedule.npy')):
		gamesPlayed = np.load('numpys/' + team.lower().replace(' ', '_') + '_schedule.npy')
		for game in gamesPlayed:
			tempGameStats = {}
			# for (index, position) in enumerate(positions):
			# 	tempGameStats[position + 'Height'] = allTeamsStats[game[0]]['Height'][index] - allTeamsStats[game[1]]['Height'][index]
			# 	tempGameStats[position + 'Weight'] = allTeamsStats[game[0]]['Weight'][index] - allTeamsStats[game[1]]['Weight'][index]
			# 	tempGameStats[position + 'PER'] = allTeamsStats[game[0]]['PER'][index] - allTeamsStats[game[1]]['PER'][index]
			# 	tempGameStats[position + 'Year'] = allTeamsStats[game[0]]['Year'][index] - allTeamsStats[game[1]]['Year'][index]
			# allTeamsTestGameStats.append(tempGameStats)

			# team1 = convertTeamNames[game[0]]
			# team2 = converTeamNames[game[1]]

			# team1 = game[0].lower().replace(' ', '_')
			# team2 = game[1].lower().replace(' ', '_')
			# print team1
			# print team2

			for (_,statKey) in enumerate(allTeamsStats[team1].keys()):
				# print game[0]
				# print game[1]
				# print allTeamsStats[team1][statKey]
				# print allTeamsStats[team2][statKey]
				tempGameStats[statKey] = allTeamsStats[team1][statKey] - allTeamsStats[team2][statKey]
			# print tempGameStats
			allTeamsTestGameStats.append(tempGameStats)

			hyphenIndex = game[3].find('-')
			try:
				spaceIndex = game[3].find(' ')
				team1Score = float(game[3][0:hyphenIndex])
				team2Score = float(game[3][hyphenIndex+1:spaceIndex+1])
			except: 
				continue
			if (game[2] == 'W'):
				allTeamsTestGameWins.append(abs((team1Score-team2Score)/((team1Score + team2Score)/float(2))))
			else:
				allTeamsTestGameWins.append(float(-1)*abs((team1Score-team2Score)/((team1Score + team2Score)/float(2))))
	else:
		pass

# print len(allTeamsTestGameWins)
# for (k, game) in enumerate(allTeamsTestGameWins):
# 	print game
# 	print allTeamsTestGameStats[k]
# print allTeamsTestGameWins

# allTeamsTestGameWinsArray = []
# allTeamsTestGameStatsArray = []
# for (_, game) in enumerate(allTeamsTestGameWins):


# allTeamsTestPanda = pd.DataFrame(allTeamsTestGameStats)
# print allTeamsTestPanda.head()

# allTeamsTestData = sm.add_constant(allTeamsTestPanda[allTeamsTestPanda.keys()])
# allTeamsAnalysis = sm.OLS(allTeamsTestGameWins, allTeamsTestData).fit()
# print est.summary()

# allTeamsTestDataArray = allTeamsTestPanda.as_matrix(columns = None)
# pca = PCA(n_components=4, whiten=True).fit(allTeamsTestDataArray)




# for (_,game) in enumerate(allGames):
# 	tempGameStats = {}
# 	for (_,statKey) in enumerate(allTeamsStats[game[0]].keys()):
# 		tempGameStats[statKey] = allTeamsStats[game[0]][statKey] - allTeamsStats[game[0][statKey]]
# 	allTeamsAnalysis



# testGameWins = []
# testGameHeightDiff = []
# testGameWeightDiff = []
# testGamePERDiff = []
# testGameYearDiff = []
# for game in testGames:
# 	if (game[3] == 'win'):
# 		testGameWins.append(1)
# 	else:
# 		testGameWins.append(0)
# 	for position in range(3):
# 		testGameHeightDiff.append(allTeamsStats[game[0]]['Height'][position] - allTeamsStats[game[1]]['Height'][position])
# 		testGameWeightDiff.append(allTeamsStats[game[0]]['Weight'][position] - allTeamsStats[game[1]]['Weight'][position])
# 		testGamePERDiff.append(allTeamsStats[game[0]]['PER'][position] - allTeamsStats[game[1]]['PER'][position])
# 		testGameYearDiff.append(allTeamsStats[game[0]]['Year'][position] - allTeamsStats[game[1]]['Year'][position])














