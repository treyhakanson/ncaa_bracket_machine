import statsmodels.api as sm
import numpy as np


allTeams = ['Kansas', 'Austin Peay','Colorado', 'UConn', 'Maryland', 'South Dakota St', 'Cal', 'Hawaii', 'Arizona', 'Wichita State', 'Miami', 'Buffalo', 'Iowa', 'Temple', 'Villanova', 'UNC Asheville', 'Oregon', 'Southern', 'Saint Joe\'s', 'Cincinnati', 'Baylor', 'Yale', 'Duke', 'UNC Wilmington', 'Texas', 'Northern Iowa', 'Texas A&M', 'Green Bay', 'Oregon State', 'VCU', 'Oklahoma', 'CSU Bakersfield', 'UNC', 'FGCU', 'USC', 'Providence', 'Indiana', 'Chattanooga', 'Kentucky', 'Stony Brook', 'Notre Dame', 'Michigan', 'West Virginia', 'SF Austin', 'Wisconsin', 'Pitt', 'Xavier', 'Weber State', 'UVA', 'Hampton', 'Texas Tech', 'Butler', 'Purdue', 'AR-Little Rock', 'Iowa State', 'Iona', 'Seton Hall', 'Gonzaga', 'Utah', 'Fresno State', 'Dayton', 'Syracuse', 'Michigan State', 'Mid Tennessee']

allPlayers = savedAllTeamsUrls = np.load('all_players.npy')

allTeamsDict = {}

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

for team in allPlayers:
	tempHeights = [0,0,0]
	tempWeights = [0,0,0]
