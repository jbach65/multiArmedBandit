from slotMachine import slotMachine
from random import random

def main():
	print("Win-Stay Solution")
	#initialize slot machines
	slotList = []
	for i in range(2):
		slotList.append(slotMachine(i))
	slotList[0].winRate = .2
	slotList[1].winRate = .4

	print("generated {} slotMachines:".format(len(slotList)))
	for obj in slotList:
		print("{}: {}".format(obj.id, obj.winRate))

	inp = input("Press enter to continue, i + enter for current slot info, or q + enter to quit: ")
	leverPulls = 0
	totalWins = 0
	currentBandit = 0
	while inp != "q" and inp != "Q":
		if inp == "i" or inp == "I":
			for obj in slotList:
				print("slotMachine {} (wins: {}, losses: {})\n\tactual win rate:\t{}".format(obj.id, obj.wins, obj.losses, obj.winRate))
			if(leverPulls !=0):
				print("Total Wins: {}, Total Pulls: {}, Total Win Rate: {}".format(totalWins, leverPulls,totalWins/leverPulls))
		elif inp == "":
			win = "no"
			print("slotMachine {} was selected (wins: {}, losses: {})\tactual win rate:\t{}".format(slotList[currentBandit].id, slotList[currentBandit].wins, slotList[currentBandit].losses, slotList[currentBandit].winRate))
			if random() < slotList[currentBandit].winRate:
				slotList[currentBandit].wins += 1
				totalWins += 1
				win = "yes"
			else:
				slotList[currentBandit].losses += 1
				currentBandit += 1
				if currentBandit == len(slotList):
					currentBandit = 0
			leverPulls+=1
			print("\tWin: {}\n\tTotal Wins: {}, Total Pulls: {}, Total Win Rate: {}".format(win, totalWins, leverPulls,totalWins/leverPulls))
		else:
			print("Does not compute")
		inp = input("\nPress enter to continue, i + enter for current slot info, or q + enter to quit: ")

if __name__ == "__main__":
	main()
