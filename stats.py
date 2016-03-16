import numpy as np
import scipy
import statsmodels.api as sm
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


# sortedPlayerPanda = pd.read_clipboard(sep = ',')
# print sortedPlayerPanda.head()
# for (_,player) in sortedPlayerPanda.iterrows():
# 	player['Height'] = int(player['Height'][2:])+72
# sortedPlayerPanda['Height'][0] = 85
# print sortedPlayerPanda.head()
# sortedPlayerPanda.to_csv('playerPandaSetonHall.csv', sep = ';')

homeTeamPlayerPanda = pd.read_csv('playerPandaSetonHall.csv', sep = ';')
homeTeamAdvancedPanda = pd.read_csv('advancedPandaSetonHall.csv', sep = ';')
awayTeamPlayerPanda = pd.read_csv('playerPandaMarquette.csv', sep = ';')
awayTeamAdvancedPanda = pd.read_csv('advancedPandaMarquette.csv', sep = ';')

homeTeamStats = []
homeTeamStats.append({'Height': 0, 'Weight': 0, 'PER': 0, 'Year':0})
homeTeamStats.append({'Height': 0, 'Weight': 0, 'PER': 0, 'Year':0})
homeTeamStats.append({'Height': 0, 'Weight': 0, 'PER': 0, 'Year':0})

percentFDict = {}
playerPositionDict = {}
homeTeamPercentPlayed = {}
homeTeamTotalMinutesPlayed = 0
for (_, player) in homeTeamAdvancedPanda.iterrows():
	homeTeamPercentPlayed[player['Player']] = player['MP']
	homeTeamTotalMinutesPlayed += player['MP']
for player in homeTeamPercentPlayed:
	homeTeamPercentPlayed[player] = float(homeTeamPercentPlayed[player])/float(homeTeamTotalMinutesPlayed)

for (_, player) in homeTeamPlayerPanda.iterrows():
	if player['Pos'] == 'C':
		homeTeamStats[0]['Height'] += (float(player['Height'])*homeTeamPercentPlayed[player['Player']])
		# homeTeamStats[0]['Weight'] += (float(player['Weight'])*homeTeamPercentPlayed[player['Player']])
		if (player['Class'] == 'FR'):
			homeTeamStats[0]['Year'] += (float(1)*homeTeamPercentPlayed[player['Player']])
		if (player['Class'] == 'SO'):
			homeTeamStats[0]['Year'] += (float(2)*homeTeamPercentPlayed[player['Player']])
		if (player['Class'] == 'JR'):
			homeTeamStats[0]['Year'] += (float(3)*homeTeamPercentPlayed[player['Player']])
		if (player['Class'] == 'SR'):
			homeTeamStats[0]['Year'] += (float(4)*homeTeamPercentPlayed[player['Player']])
	elif player['Pos'] == 'F':
		homeTeamStats[1]['Height'] += (float(player['Height'])*homeTeamPercentPlayed[player['Player']])
		# homeTeamStats[1]['Weight'] += (float(player['Weight'])*homeTeamPercentPlayed[player['Player']])
		if (player['Class'] == 'FR'):
			homeTeamStats[1]['Year'] += (float(1)*homeTeamPercentPlayed[player['Player']])
		if (player['Class'] == 'SO'):
			homeTeamStats[1]['Year'] += (float(2)*homeTeamPercentPlayed[player['Player']])
		if (player['Class'] == 'JR'):
			homeTeamStats[1]['Year'] += (float(3)*homeTeamPercentPlayed[player['Player']])
		if (player['Class'] == 'SR'):
			homeTeamStats[1]['Year'] += (float(4)*homeTeamPercentPlayed[player['Player']])
	elif player['Pos'] == 'G':
		homeTeamStats[2]['Height'] += (float(player['Height'])*homeTeamPercentPlayed[player['Player']])
		# homeTeamStats[2]['Weight'] += (float(player['Weight'])*homeTeamPercentPlayed[player['Player']])
		if (player['Class'] == 'FR'):
			homeTeamStats[2]['Year'] += (float(1)*homeTeamPercentPlayed[player['Player']])
		if (player['Class'] == 'SO'):
			homeTeamStats[2]['Year'] += (float(2)*homeTeamPercentPlayed[player['Player']])
		if (player['Class'] == 'JR'):
			homeTeamStats[2]['Year'] += (float(3)*homeTeamPercentPlayed[player['Player']])
		if (player['Class'] == 'SR'):
			homeTeamStats[2]['Year'] += (float(4)*homeTeamPercentPlayed[player['Player']])
	elif player['Pos'] == 'G-F':
		percentF = (float(player['Height'])-float(68))/float(84)
		percentG = float(1) - percentF
		percentFDict[player['Player']] = percentF

		homeTeamStats[1]['Height'] += percentF*(float(player['Height'])*homeTeamPercentPlayed[player['Player']])
		# homeTeamStats[1]['Weight'] += percentF*(float(player['Weight'])*homeTeamPercentPlayed[player['Player']])
		if (player['Class'] == 'FR'):
			homeTeamStats[1]['Year'] += percentF*(float(1)*homeTeamPercentPlayed[player['Player']])
		if (player['Class'] == 'SO'):
			homeTeamStats[1]['Year'] += percentF*(float(2)*homeTeamPercentPlayed[player['Player']])
		if (player['Class'] == 'JR'):
			homeTeamStats[1]['Year'] += percentF*(float(3)*homeTeamPercentPlayed[player['Player']])
		if (player['Class'] == 'SR'):
			homeTeamStats[1]['Year'] += percentF*(float(4)*homeTeamPercentPlayed[player['Player']])

		homeTeamStats[2]['Height'] += percentG*(float(player['Height'])*homeTeamPercentPlayed[player['Player']])
		# homeTeamStats[2]['Weight'] += percentG*(float(player['Weight'])*homeTeamPercentPlayed[player['Player']])
		if (player['Class'] == 'FR'):
			homeTeamStats[2]['Year'] += percentG*(float(1)*homeTeamPercentPlayed[player['Player']])
		if (player['Class'] == 'SO'):
			homeTeamStats[2]['Year'] += percentG*(float(2)*homeTeamPercentPlayed[player['Player']])
		if (player['Class'] == 'JR'):
			homeTeamStats[2]['Year'] += percentG*(float(3)*homeTeamPercentPlayed[player['Player']])
		if (player['Class'] == 'SR'):
			homeTeamStats[2]['Year'] += percentG*(float(4)*homeTeamPercentPlayed[player['Player']])
	else:
		print 'done fucked up'
	playerPositionDict[player['Player']] = player['Pos']
	print player['Player']

awayTeamPercentPlayed = {}
awayTeamTotalMinutesPlayed = 0
for (_, player) in awayTeamAdvancedPanda.iterrows():
	awayTeamPercentPlayed[player['Player']] = player['MP']
	awayTeamTotalMinutesPlayed += player['MP']
for player in awayTeamPercentPlayed:
	awayTeamPercentPlayed[player] = float(awayTeamPercentPlayed[player])/float(awayTeamTotalMinutesPlayed)

for (_, player) in awayTeamPlayerPanda.iterrows():
	if player['Pos'] == 'C':
		homeTeamStats[0]['Height'] -= (float(player['Height'])*awayTeamPercentPlayed[player['Player']])
		# homeTeamStats[0]['Weight'] -= (float(player['Weight'])*awayTeamPercentPlayed[player['Player']])
		if (player['Class'] == 'FR'):
			homeTeamStats[0]['Year'] -= (float(1)*awayTeamPercentPlayed[player['Player']])
		if (player['Class'] == 'SO'):
			homeTeamStats[0]['Year'] -= (float(2)*awayTeamPercentPlayed[player['Player']])
		if (player['Class'] == 'JR'):
			homeTeamStats[0]['Year'] -= (float(3)*awayTeamPercentPlayed[player['Player']])
		if (player['Class'] == 'SR'):
			homeTeamStats[0]['Year'] -= (float(4)*awayTeamPercentPlayed[player['Player']])
	elif player['Pos'] == 'F':
		homeTeamStats[1]['Height'] -= (float(player['Height'])*awayTeamPercentPlayed[player['Player']])
		# homeTeamStats[1]['Weight'] -= (float(player['Weight'])*awayTeamPercentPlayed[player['Player']])
		if (player['Class'] == 'FR'):
			homeTeamStats[1]['Year'] -= (float(1)*awayTeamPercentPlayed[player['Player']])
		if (player['Class'] == 'SO'):
			homeTeamStats[1]['Year'] -= (float(2)*awayTeamPercentPlayed[player['Player']])
		if (player['Class'] == 'JR'):
			homeTeamStats[1]['Year'] -= (float(3)*awayTeamPercentPlayed[player['Player']])
		if (player['Class'] == 'SR'):
			homeTeamStats[1]['Year'] -= (float(4)*awayTeamPercentPlayed[player['Player']])
	elif player['Pos'] == 'G':
		homeTeamStats[2]['Height'] -= (float(player['Height'])*awayTeamPercentPlayed[player['Player']])
		# homeTeamStats[2]['Weight'] -= (float(player['Weight'])*awayTeamPercentPlayed[player['Player']])
		if (player['Class'] == 'FR'):
			homeTeamStats[2]['Year'] -= (float(1)*awayTeamPercentPlayed[player['Player']])
		if (player['Class'] == 'SO'):
			homeTeamStats[2]['Year'] -= (float(2)*awayTeamPercentPlayed[player['Player']])
		if (player['Class'] == 'JR'):
			homeTeamStats[2]['Year'] -= (float(3)*awayTeamPercentPlayed[player['Player']])
		if (player['Class'] == 'SR'):
			homeTeamStats[2]['Year'] -= (float(4)*awayTeamPercentPlayed[player['Player']])
	elif player['Pos'] == 'G-F':
		percentF = (float(player['Height'])-float(68))/float(84)
		percentG = float(1) - percentF
		percentFDict[player['Player']] = percentF

		homeTeamStats[1]['Height'] -= percentF*(float(player['Height'])*awayTeamPercentPlayed[player['Player']])
		# homeTeamStats[1]['Weight'] -= percentF*(float(player['Weight'])*awayTeamPercentPlayed[player['Player']])
		if (player['Class'] == 'FR'):
			homeTeamStats[1]['Year'] -= percentF*(float(1)*awayTeamPercentPlayed[player['Player']])
		if (player['Class'] == 'SO'):
			homeTeamStats[1]['Year'] -= percentF*(float(2)*awayTeamPercentPlayed[player['Player']])
		if (player['Class'] == 'JR'):
			homeTeamStats[1]['Year'] -= percentF*(float(3)*awayTeamPercentPlayed[player['Player']])
		if (player['Class'] == 'SR'):
			homeTeamStats[1]['Year'] -= percentF*(float(4)*awayTeamPercentPlayed[player['Player']])

		homeTeamStats[2]['Height'] -= percentG*(float(player['Height'])*awayTeamPercentPlayed[player['Player']])
		# homeTeamStats[2]['Weight'] -= percentG*(float(player['Weight'])*awayTeamPercentPlayed[player['Player']])
		if (player['Class'] == 'FR'):
			homeTeamStats[2]['Year'] -= percentG*(float(1)*awayTeamPercentPlayed[player['Player']])
		if (player['Class'] == 'SO'):
			homeTeamStats[2]['Year'] -= percentG*(float(2)*awayTeamPercentPlayed[player['Player']])
		if (player['Class'] == 'JR'):
			homeTeamStats[2]['Year'] -= percentG*(float(3)*awayTeamPercentPlayed[player['Player']])
		if (player['Class'] == 'SR'):
			homeTeamStats[2]['Year'] -= percentG*(float(4)*awayTeamPercentPlayed[player['Player']])
	else:
		print 'done fucked up'
	playerPositionDict[player['Player']] = player['Pos']
	print player['Player']

for (_,player) in homeTeamAdvancedPanda.iterrows():
	if playerPositionDict[player['Player']] == 'C':
		homeTeamStats[0]['PER'] += float(player['PER'])*homeTeamPercentPlayed[player['Player']]
	elif playerPositionDict[player['Player']] == 'F':
		homeTeamStats[1]['PER'] += float(player['PER'])*homeTeamPercentPlayed[player['Player']]
	elif playerPositionDict[player['Player']] == 'G':
		homeTeamStats[2]['PER'] += float(player['PER'])*homeTeamPercentPlayed[player['Player']]
	elif playerPositionDict[player['Player']] == 'G-F':
		percentF = percentFDict[player['Player']]
		percentG = float(1) - percentF

		homeTeamStats[1]['PER'] += percentF*float(player['PER'])*homeTeamPercentPlayed[player['Player']]
		homeTeamStats[2]['PER'] += percentF*float(player['PER'])*homeTeamPercentPlayed[player['Player']]		
	else:
		print 'done fucked up'


for (_,player) in awayTeamAdvancedPanda.iterrows():
	if playerPositionDict[player['Player']] == 'C':
		homeTeamStats[0]['PER'] -= float(player['PER'])*awayTeamPercentPlayed[player['Player']]
	elif playerPositionDict[player['Player']] == 'F':
		homeTeamStats[1]['PER'] -= float(player['PER'])*awayTeamPercentPlayed[player['Player']]
	elif playerPositionDict[player['Player']] == 'G':
		homeTeamStats[2]['PER'] -= float(player['PER'])*awayTeamPercentPlayed[player['Player']]
	elif playerPositionDict[player['Player']] == 'G-F':
		percentF = percentFDict[player['Player']]
		percentG = float(1) - percentF

		homeTeamStats[1]['PER'] -= percentF*float(player['PER'])*awayTeamPercentPlayed[player['Player']]
		homeTeamStats[2]['PER'] -= percentF*float(player['PER'])*awayTeamPercentPlayed[player['Player']]		
	else:
		print 'done fucked up'



for (k, position) in enumerate(homeTeamStats):
	print position

