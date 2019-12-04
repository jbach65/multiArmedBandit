from slotMachine import slotMachine
from random import random

def main():
	#initialize slot machines
	slotList = []
	for i in range(10):
		slotList.append(slotMachine(i))
	#slotList[0].winRate = .1
	#slotList[1].winRate = .09

	print("generated:")
	for obj in slotList:
		print("{}: {}".format(obj.id, obj.winRate))

	inp = input("Press enter to continue, i + enter for current slot info, or q + enter to quit: ")
	leverPulls = 0
	totalWins = 0
	while inp != "q" and inp != "Q":
		if inp == "i" or inp == "I":
			for obj in slotList:
				print("slotMachine {} (wins: {}, losses: {}, UCB: {})\n\tactual win rate:\t{}".format(obj.id, obj.wins, obj.losses, obj.upperConfidenceBound, obj.winRate))
			if(leverPulls !=0):
				print("Total Wins: {}, Total Pulls: {}, Total Win Rate: {}".format(totalWins, leverPulls,totalWins/leverPulls))
		else:
			win = "no"
			slotList.sort(key=lambda x: x.upperConfidenceBound, reverse=True)	#sort by upper confidence bound
			print("slotMachine {} was selected (wins: {}, losses: {}, UCB: {})\n\tactual win rate:\t{}".format(slotList[0].id, slotList[0].wins, slotList[0].losses, slotList[0].upperConfidenceBound, slotList[0].winRate))
			if random() < slotList[0].winRate:
				slotList[0].wins += 1
				totalWins += 1
				win = "yes"
			else:
				slotList[0].losses += 1
			leverPulls+=1
			slotList[0].calculateUCB()
			print("\tWin: {}\n\tTotal Wins: {}, Total Pulls: {}, Total Win Rate: {}".format(win, totalWins, leverPulls,totalWins/leverPulls))
		inp = input("Press enter to continue, i + enter for current slot info, or q + enter to quit: ")

if __name__ == "__main__":
	main()
