from ast import While
import random
import math
while True:
    print("Rules: Dealer must hit on 16 and stay on 17./n In an event of a tie, it is called a push and nobdy wins./n If both Player and Dealer get blackjack, the Dealer wins")
    print("Player will only see Dealers second card after he stays on a given number")

# Create a list that looks like a dictionary that has all 52 cards in a deck of cards
    cards =  [["2s",2], ["3s",3], ["4s",4], ["5s",5], ["6s",6], ["7s",7], ["8s",8], ["9s",9], ["10s",10], ["Js",10], ["Qs",10], ["Ks",10], ["As",11],
["2h",2], ["3h",3], ["4h",4], ["5h",5], ["6h",6], ["7h",7], ["8h",8], ["9h",9], ["10h",10], ["Jh",10], ["Qh",10], ["Kh",10], ["Ah",11],
["2c",2], ["3c",3], ["4c",4], ["5c",5], ["6c",6], ["7c",7], ["8c",8], ["9c",9], ["10c",10], ["Jc",10], ["Qc",10], ["Kc",10], ["Ac",11],
["2d",2], ["3d",3], ["4d",4], ["5d",5], ["6d",6], ["7d",7], ["8d",8], ["9d",9], ["10d",10], ["Jd",10], ["Qd",10], ["Kd",10], ["Ad",11]]

#Now we are going to shuffle those cards since they are typed in order and is common convention in Blackjack
#We will print the cards to show that they are shuffled
    random.shuffle(cards)
    print(cards)

#Create a function to pop(take a card) we do pop(0) so that it is at the top of the shuffled deck, this will be the first players card and will be visible
    def draw():
        return cards.pop(0)

#lists for player hand and dealer hand
    player_hand = []
    dealer_hand = []

# now we will append the previous pop cards into the created list
    player_hand.append(draw())
    dealer_hand.append(draw())
    player_hand.append(draw())
    dealer_hand.append(draw())

    print(cards)
#showing each other hands

    print(f'You drew {player_hand[0][0]} and a {player_hand[1][0]}')
    print(f'The dealers upcard is {dealer_hand[1][0]}')


    def get_hand(hand):
        counter = 0
        x = 0
        while x < len(hand):
            counter += hand[x][1]
            x += 1
        return counter
        
    while True:
        answer = input("Would you like to hit or stay??? ")
        if answer == "stay":
            break
        else:
            player_hand.append(draw())
            value = get_hand(player_hand)
            print(f"Your current hand is {player_hand}")
            if value >= 21:
                break
    while True:
        value = get_hand(dealer_hand)
        if value <=16:
            dealer_hand.append(draw())
        elif value >=17:
            break
    
    print(player_hand)
    print(dealer_hand)

    player_total = get_hand(player_hand)
    dealer_total = get_hand(dealer_hand)

    if player_total == dealer_total:
        print("PUSH")
    elif player_total > 21:
        print("Player Busted")
    elif dealer_total > 21:
        print("Dealer Busted, Player wins")
    elif player_total == 21:
        print("Player Winnnnnnnnnnnnnssssssss")
    elif dealer_total == 21:
        print("Dealer Wins :(")
    elif player_total > dealer_total:
        print("Player Winnnns")
    elif dealer_total > player_total:
        print("Dealer Wins, Boo")

    end_game = input("Would you like to play again? yes or no?: ")
    if end_game == "no".lower():
        break

print("Thanks for playing!!")

        