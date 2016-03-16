import statsmodels.api as sm
import numpy as np
from sklearn.decomposition import PCA
import pandas as pd

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

allTeams = ['Kansas', 'Austin Peay','Colorado', 'UConn', 'Maryland', 'South Dakota St', 'Cal', 'Hawaii', 'Arizona', 'Wichita State', 'Miami', 'Buffalo', 'Iowa', 'Temple', 'Villanova', 'UNC Asheville', 'Oregon', 'Southern', 'Saint Joes', 'Cincinnati', 'Baylor', 'Yale', 'Duke', 'UNC Wilmington', 'Texas', 'Northern Iowa', 'Texas A&M', 'Green Bay', 'Oregon State', 'VCU', 'Oklahoma', 'CSU Bakersfield', 'UNC', 'FGCU', 'USC', 'Providence', 'Indiana', 'Chattanooga', 'Kentucky', 'Stony Brook', 'Notre Dame', 'Michigan', 'West Virginia', 'SF Austin', 'Wisconsin', 'Pitt', 'Xavier', 'Weber State', 'UVA', 'Hampton', 'Texas Tech', 'Butler', 'Purdue', 'AR-Little Rock', 'Iowa State', 'Iona', 'Seton Hall', 'Gonzaga', 'Utah', 'Fresno State', 'Dayton', 'Syracuse', 'Michigan State', 'Mid Tennessee']

allGames = [['Kansas', 'Austin Peay'],['Colorado', 'UConn'], ['Maryland', 'South Dakota St'], ['Cal', 'Hawaii'], ['Arizona', 'Wichita State'], ['Miami', 'Buffalo'], ['Iowa', 'Temple'], ['Villanova', 'UNC Asheville'], ['Oregon', 'Southern'], ['Saint Joe\'s', 'Cincinnati'], ['Baylor', 'Yale'], ['Duke', 'UNC Wilmington'], ['Texas', 'Northern Iowa'], ['Texas A&M', 'Green Bay'], ['Oregon State', 'VCU'], ['Oklahoma', 'CSU Bakersfield'], ['UNC', 'FGCU'], ['USC', 'Providence'], ['Indiana', 'Chattanooga'], ['Kentucky', 'Stony Brook'], ['Notre Dame', 'Michigan'], ['West Virginia', 'SF Austin'], ['Wisconsin', 'Pitt'], ['Xavier', 'Weber State'], ['UVA', 'Hampton'], ['Texas Tech', 'Butler'], ['Purdue', 'AR-Little Rock'], ['Iowa State', 'Iona'], ['Seton Hall', 'Gonzaga'], ['Utah', 'Fresno State'], ['Dayton', 'Syracuse'], ['Michigan State', 'Mid Tennessee']]

allPlayers = np.load('numpys/all_players.npy')

positions = ['C', 'F', 'G']

longTeamNames = np.load('./numpys/long_team_names.npy')


allTeamsStats = {}

for team in allPlayers:
	tempStats = {'CHeight':0, 'CWeight': 0, 'CPER': 0, 'CYear': 0, 'FHeight':0, 'FWeight': 0, 'FPER': 0, 'FYear': 0, 'GHeight':0, 'GWeight': 0, 'GPER': 0, 'GYear': 0}
	
	# tempHeight = [0,0,0]
	# tempWeight = [0,0,0]
	# tempPER = [0,0,0]
	# tempYear = [0,0,0]
	
	totalTeamMinutes = 0
	for player in team:
		totalTeamMinutes += player.tm()

	for player in team:
		if (player.pos == 'G-F'):
			forwardWeight = (float(player.ht)-float(68))/float(84)
			playtimeWeight = float(player.tm)/float(totalTeamMinutes)

			tempStats['FHeight'] += player.ht * playtimeWeight * forwardWeight
			tempStats['FWeight'] += player.wt * playtimeWeight * forwardWeight
			tempStats['FPER'] += player.per * playtimeWeight * forwardWeight
			tempStats['FYear'] += convertYrToFloat(player.yr) * playtimeWeight * forwardWeight

			tempStats['GHeight'] += player.ht * playtimeWeight * (float(1) - forwardWeight)
			tempStats['GWeight'] += player.wt * playtimeWeight * (float(1) - forwardWeight)
			tempStats['GPER'] += player.per * playtimeWeight * (float(1) - forwardWeight)
			tempStats['GYear'] += convertYrToFloat(player.yr) * playtimeWeight * (float(1) - forwardWeight)
		else:
			positionIndex = 0
			if (player.pos == 'F'):
				positionIndex = 1
			elif (player.pos == 'G'):
				positionIndex = 2
			elif (player.pos == 'C'):
				positionIndex = 0
			else:
				print 'you done fucked up hard'
				continue

			playtimeWeight = float(player.tm)/float(totalTeamMinutes)
				
			tempStats[positions[positionIndex] + 'Height'] += player.ht * playtimeWeight
			tempStats[positions[positionIndex] + 'Weight'] += player.wt * playtimeWeight
			tempStats[positions[positionIndex] + 'PER'] += player.per * playtimeWeight
			tempStats[positions[positionIndex] + 'Year'] += convertYrToFloat(player.yr) * playtimeWeight

	allTeamsStats[team[0].team] = tempStats

	# for player in team:
	# 	if (player.pos == 'G-F'):
	# 		forwardWeight = (float(player.ht)-float(68))/float(84)
	# 		playtimeWeight = float(player.tm)/float(totalTeamMinutes)

	# 		tempHeight[1] += player.ht * playtimeWeight * forwardWeight
	# 		tempWeight[1] += player.wt * playtimeWeight * forwardWeight
	# 		tempPER[1] += player.per * playtimeWeight * forwardWeight
	# 		tempYear[1] += convertYrToFloat(player.yr) * playtimeWeight * forwardWeight

	# 		tempHeight[2] += player.ht * playtimeWeight * (float(1) - forwardWeight)
	# 		tempWeight[2] += player.wt * playtimeWeight * (float(1) - forwardWeight)
	# 		tempPER[2] += player.per * playtimeWeight * (float(1) - forwardWeight)
	# 		tempYear[2] += convertYrToFloat(player.yr) * playtimeWeight * (float(1) - forwardWeight)
	# 	else:
	# 		positionIndex = 0
	# 		if (player.pos == 'F'):
	# 			positionIndex = 1
	# 		elif (player.pos == 'G'):
	# 			positionIndex = 2
	# 		elif (player.pos == 'C'):
	# 			positionIndex = 0
	# 		else:
	# 			print 'you done fucked up hard'
	# 			continue

	# 		playtimeWeight = float(player.tm)/float(totalTeamMinutes)
				
	# 		tempHeight[positionIndex] += player.ht * playtimeWeight 
	# 		tempWeight[positionIndex] += player.wt * playtimeWeight 
	# 		tempPER[positionIndex] += player.per * playtimeWeight 
	# 		tempYear[positionIndex] += convertYrToFloat(player.yr) * playtimeWeight 

	# allTeamsStats[team[0].team] = {'Height': tempHeight, 'Weight': tempWeight, 'PER': tempPer, 'Year': tempYear}

print allTeamStats

allTeamsTestGameWins = []
allTeamsTestGameStats = [{}]
for team in longTeamNames:
	if (os.path.isfile('numpys/' + team.lower().replace(' ', '_') + '_schedule.npy')):
		gamesPlayed = np.load('numpys/' + team.lower().replace(' ', '_') + '_schedule.npy')
		for game in gamesPlayed:
			tempGameStats = {}
			# for (index, position) in enumerate(positions):
			# 	tempGameStats[position + 'Height'] = allTeamsStats[game[0]]['Height'][index] - allTeamsStats[game[1]]['Height'][index]
			# 	tempGameStats[position + 'Weight'] = allTeamsStats[game[0]]['Weight'][index] - allTeamsStats[game[1]]['Weight'][index]
			# 	tempGameStats[position + 'PER'] = allTeamsStats[game[0]]['PER'][index] - allTeamsStats[game[1]]['PER'][index]
			# 	tempGameStats[position + 'Year'] = allTeamsStats[game[0]]['Year'][index] - allTeamsStats[game[1]]['Year'][index]
			# allTeamsTestGameStats.append(tempGameStats)

			for (_,statKey) in enumerate(allTeamsStats[game[0]].keys()):
				tempGameStats[statKey] = allTeamsStats[game[0]][statKey] - allTeamsStats[game[0][statKey]]
			allTeamsTestGameStats.append(tempGameStats)

			hyphenIndex = game[3].find('-', beg=0, end=len(game[3]))
			spaceIndex = game[3].find(' ', beg=0, end= len(game[3]))
			team1Score = float(game[3][0:hyphenIndex])
			team2Score = float(game[3][hyphenIndex+1:spaceIndex])
			if (game[2] == 'W'):
				allTeamsGameWins.append(abs((team1Score-team2Score)/((team1Score + team2Score)/float(2))))
			else:
				allTeamsGameWins.append(float(-1)*abs((team1Score-team2Score)/((team1Score + team2Score)/float(2))))
	else:
		pass

allTeamsTestPanda = pd.DataFrame(allTeamTestGameStats)
print allTeamsTestPanda.head()
allTeamsTestData = sm.add_constant(allTeamsTestPanda[allTeamsTestPanda.keys()])
allTeamsAnalysis = sm.OLS(allTeamsTestGameWins, allTeamsTestData).fit()
print est.summary()

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














