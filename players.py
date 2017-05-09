from glicko2 import Player
from matches02 import getParticipants


#use ben's getParticipants and compares its dictionary values to the input list's values 
#getParticipants uses lower cases so i'll probably remove those later
#returns a list of players
def updatePlayerList(inputPlayerList, inputDictionary):
    #read matches.txt file and create dictionary 
    newPlayerList = list()
    for key, value in inputDictionary.items():
        if value not in inputPlayerList:
            userChoice = input("New player: " + value + ". Add as new player or edit tag?\nType in add to add as new player, edit to edit the tag, or press any key to exit.\n")
            if userChoice.lower() == "add":
                inputPlayerList.append(value)
            else:
                break
            if userChoice.lower() == "edit":
                newTag = input("Enter the new tag: ")
                if newTag not in inputPlayerList:
                    inputPlayerList.append(newTag)
                else: 
                    break
            
    return newPlayerList

   
def main():
    #input text file of existing players
    while(True):
        playerListFile = input("Enter the file name of your list of players: ")
        try:
            playerList = open(playerListFile, "r")
            break
        except:
            print("Cannot find the file.")
    
    #create a list for existing players from input file
    thePlayerList = list()
    #only works with input files having names separated by spaces atm
    playerList = playerList.read()
    playerList = playerList.splitlines()
    for line in playerList:
        for player in line.split():
            if player.lower() not in thePlayerList:
                thePlayerList.append(player)     

    #get rid of hardcode later
    name = "edmmelee-SmashAtCASE042817Melee"
    apiKey = "iRZrPhoDkyLV2xFXyUuJ5pVauosMlZPGMMmCdSaE"
   
    players = getParticipants(name, apiKey)
    updatePlayerList(thePlayerList, players)
    
    #update player list text file
    outputFile = open(playerListFile, "w")
    outputFile.write("")
    outputFile.close()
    outputFile = open(playerListFile, "a")
    for player in thePlayerList:
        #print(player)
        outputFile.write(player + "\n")
    outputFile.close()
    
    #print(thePlayerList)

    #initialize player instances
    playerClass = []
    for player in thePlayerList:
        player = Player(player)
        playerClass.append(player)    



    
    #open player match file to read
    matchOutput = open("test.txt", "r")
    matchOutput = matchOutput.read()
    #split each word
    matchOutput = matchOutput.split()
    matchOutput.pop(0)

    #add opponents
    for x in range(1, len(matchOutput), 4):
        if matchOutput[x] > matchOutput[x+2]:
            for player in playerClass:
                if matchOutput[x-1] in player.name:
                    player.addMatch(matchOutput[x+1], 1)
                if matchOutput[x+1] in player.name:
                    player.addMatch(matchOutput[x-1], 0)
                
        elif matchOutput[x] < matchOutput[x+2] and int(matchOutput[x]) >=0: 
            for player in playerClass:
                if matchOutput[x-1] in player.name:
                    player.addMatch(matchOutput[x+1], 0) 
                if matchOutput[x+1] in player.name:
                    player.addMatch(matchOutput[x-1], 1)
        
                    
    outputMatches = open("outputMatches.txt", "w")
    #for player in playerClass:
        #outputMatches.write(player.name + player.opponentList + player.resultList + player.rating + player.rd)
    #for player in playerClass:
        #print(dir([player]))
        #outputMatches.write(dir([player]))

        
    #figure out how to print player attributes to output file
    for player in playerClass:
        print(player.name, player.opponentList)


    
main()

    
