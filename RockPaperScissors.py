player1 = ""
player2 = ""

while True:
    if player1 == player2:
        player1 = input("enter your move player 1: ")
        player2 = input("enter your move player 2: ")
    elif player1 == "rock" and player2 == "scissors":
        print("Player 1 WINS!")
    break

    #elif player1 == "scissors" and player2 == "paper":
       # print("Player 1 WINS!")
    #elif player1 == "paper" and player2 == "rock":
        #print("Player 1 WINS!")
    #elif player1 == "scissors" and player2 == "rock":
        #print("Player 1 WINS!")
    #elif player1 == "paper" and player2 == "scissors":
        #print("Player 2 WINS!")
    #elif player1 == "rock" and player2 == "paper":
        #print("Player 2 WINS!")
    #break
