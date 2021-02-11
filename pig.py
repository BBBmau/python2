import random

'''global variables used throughout the gameOfPigs'''

preGame = []
scores = []
pig_fall = ['Pink', 'Dot', 'Razorback',
            'Trotter', 'Snouter', 'Leaning Jowler']
pig_luck = ['normal', 'oinker', 'piggyback']

soloPigPoints= [0,0,5,5,10,15]

def gameSet(playerNames):
    "Function sets presets for game: [player1, player2, targetScore]"
    "into preGame List"
    
    print("Enter All Player Names(When done enter 'X')")
    targetScore = 0
    count = 1
    while(True):
        player = input("Enter Player " + str(count)+ " Name: ")
        if player == "X":
            break
        preGame.append(player)
        scores.append(0)
        count += 1
        
    while(int(targetScore) <= int(0)):
        targetScore = input("Enter Target Score: ")
        if(int(targetScore) <= int(0)):
            print("Enter a Valid Number for Game")
        assert (int(targetScore) > int(0)), "Target should be a reachable number"
    preGame.append(targetScore)

def checkWinner(score, targetScore):
    
    '''checks if player met targetScore'''
    if int(score) >= int(targetScore):
        return True
    else:
        return False



def pigPoints(pig1, pig2, player):
    '''Calculates the score from roll of player'''
    
    index1 = pig_fall.index(pig1)
    index2 = pig_fall.index(pig2)
    
    if (pig1 == 'Pink' and pig2 == 'Dot') or (pig1 == 'Dot' and pig2 == 'Pink'):
        scores[player] = scores[player] + 1
        
    elif (pig1 == 'Razorback' and pig2 == 'Razorback'):
        scores[player] = scores[player] + 20
    elif (pig1 == 'Trotter' and pig2 == 'Trotter'):
        scores[player] = scores[player] + 20
        
    elif (pig1 == 'Snouter' and pig2 == 'Snouter'):
        scores[player] = scores[player] + 40
        
    elif (pig1 == 'Leaning Jowler' and pig2 == 'Leaning Jowler'):
        scores[player] = scores[player] + 60
    else:
        scores[player] = scores[player] + soloPigPoints[index1]
        scores[player] = scores[player] + soloPigPoints[index2]
        
def pigRoll(player):
    '''Rolls for the current player with weighted chance'''
    
    while True:
        rolls = str(input("Pass or Roll? "))
        if rolls.lower() == "pass":
            break
        if rolls.lower() != "roll":
            print("Please re-enter either (PASS/ROLL)")
        else:
            pig1 = random.choices(pig_fall, [35,30,20,10,4,1])[0]
            pig2 = random.choices(pig_fall, [35,30,20,10,4,1])[0]
            pigTop = random.choices(pig_luck,[75,20,3])[0]

            if pigTop == 'normal':
                pigPoints(pig1,pig2, player)
                print("Score is now " + str(scores[player]))
            elif pigTop == 'oinker':
                print("OINKER!")
                scores[player] = 0
                print("Score is now " + str(scores[player]))
                break
            else:
                print("PIGGYBACK!!!")
                print(preGame[player] + " is out of the game!")
                preGame.pop(player)
                scores.pop(player)
                break
  

def game(preGame):
    '''Initializes the game with the set players and target'''
    
    winner = False
    
    while winner == False:
        for i in range(len(preGame) - 1):
            print("It is " + preGame[i] + "'s turn!")
            rolls = pigRoll(i)

            if(len(preGame) - 1 == 1):
                '''For when only one player is left.'''
                print(preGame[1] + " is the Winner!")
                break

            if checkWinner(scores[i], preGame[-1]):
                print(preGame[i] + " is the Winner!")
                winner = True
                break

if __name__ == "__main__":
    gameSet(preGame)
    game(preGame)
