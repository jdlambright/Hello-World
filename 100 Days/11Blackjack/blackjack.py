import random
#from replit import clear
from art import logo


# function to deal cards to user and computer
def deal_card():
    """Returns a random card from deck. """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

#declaring this function here to call it later
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "draw"
    elif user_score == 0:
        return "You win with a Blackjack"
    elif computer_score == 0:
        return "The dealer won with a Blackjack"
    elif user_score > 21:
        return "You Bust"
    elif computer_score > 21:
        return "You win the dealer bust"
    elif user_score > computer_score:
        return "You Win!!"
    elif computer_score > user_score:
        return "The dealer won"
print(logo)

def play_game():
    # starts an empty list for user and computers
    user_cards = []
    computer_cards = []
    is_game_over= False
    # this adds the two cards to user and computer's list
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    #prompts user to play til game is over
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your Cards: {user_cards}, current score is {user_score}")
        print(f"Computer's first Card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True

        else:
            response = input("Would you like to draw another card? 'y' for 'yes' or 'n' for 'pass': ").lower()
            if response == "y":
                user_cards.append(deal_card())

            else:
                is_game_over = True

    #this determines if the computer plays again
    while computer_score != 0 and computer_score <17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"    Your final hand: {user_cards}, and final score was {user_score}")
    print(f"    The dealer's final hand: {computer_cards}, and final score was {computer_score}")
    print(compare(user_score, computer_score))
#This allows game to be played
while input("Would you like to play blackjack? type 'y' or 'n': ")== "y":
    #clear()
    play_game()
