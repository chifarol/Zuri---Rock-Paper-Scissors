import random

options = ["R", "P", "S"]

def player_choice():
    choice = input("Pick an option between 'R', 'P' or 'S' \n")
    return choice
def start():
    player1 = player_choice()
    player1 = player1.upper()
    # print(player1.upper())
    if(player1 == "R" or player1 == "P" or player1 == "S"):
        
        comp = random.choice(options)
        print('Player ({0}) : CPU ({1})'.format(player1, comp))
        if comp == player1:
            print('Stalemate')
            start()
        else:
            winner = check_winner(player1, comp)
            print('The winner is {0}'.format(winner))
    else:
        print('Invalid input')
        start()

def check_winner(p1, comp):
    if(p1=="R" and comp == "S"):
        return p1
    elif(p1=="S" and comp == "R"):
        return comp
    else:
        op = ["R","P","S"]
        x = op.index(p1)
        y = op.index(comp)
        if x > y:
            return p1
        else:
            return comp





    

start()

