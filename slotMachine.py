from random import random

class slotMachine():
	def __init__(self, slotID):
		self.id = slotID
		self.wins = 0
		self.losses = 0
		self.winRate = random()*.25	#range from 0 to .25
		self.upperConfidenceBound = 1	#range from 0 to 1

	def resetWL(self):	#resets wins and losses
		self.wins = 0
		self.losses = 0

	def calculateUCB(self):
		self.upperConfidenceBound = (self.wins+1)/(self.wins+self.losses+1)
