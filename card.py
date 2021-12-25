import random
import authenticate

p1 = authenticate.authenticate(1)
p2 = authenticate.authenticate(2)

cardColour = ['Red', 'Yellow', 'Black']
deck = []
player1 = []
player2 = []

for i in range(1, 11):
    for card in cardColour:
        cardValue = '%s %i' % (card, i)
        deck.append(cardValue)

random.shuffle(deck)
# print(deck)

def takeCard(id):
    if(id == 1):
        player1.append(deck[0])
        deck.pop(0)
    else:
        player2.append(deck[0])
        deck.pop(0)

def loseCard(id):
    if(id == 1):
        player1.pop(len(player1)-1)
    else:
        player2.pop(len(player2)-1)

def cardSuffix(cardNumber):
    if cardNumber == 1:
        return '1st'
    if cardNumber == 2:
        return '2nd'
    if cardNumber == 3:
        return '3rd'
    else:
        return '%sth' % (cardNumber)

def playerAction(player, cardNumber):
    if player == player1:
        id = 1
    else:
        id = 2
    cardCount = cardSuffix(cardNumber)
    input('Player %s press Enter to take your %s card' % (id, cardCount))
    takeCard(id)
    print('length of array = %s' % len(player))
    print('player %s has taken %s card from the deck' % (id, player[len(player)-1]))

def checkWinner(card1, card2):
    def colour(card):
        spacePosition = card.index(' ')
        # print(card[:spacePosition])
        return card[:spacePosition]

    def value(card):
        spacePosition = card.index(' ')
        return card[spacePosition:]

    if (colour(card1) == 'Red' and colour(card2) == 'Black'):
        print('Player 1 wins!')
        player1.append(player2[len(player2)-1])
        player2.pop(len(player2)-1)

    if (colour(card1) == 'Red' and colour(card2) == 'Yellow'):
        print('Player 2 wins!')
        player2.append(player1[len(player1)-1])
        player1.pop(len(player1)-1)
    
    if (colour(card1) == 'Yellow' and colour(card2) == 'Red'):
        print('Player 1 wins!')
        player1.append(player2[len(player2)-1])
        player2.pop(len(player2)-1)

    if (colour(card1) == 'Yellow' and colour(card2) == 'Black'):
        print('Player 2 wins!')
        player2.append(player1[len(player1)-1])
        player1.pop(len(player1)-1)
    
    if (colour(card1) == 'Black' and colour(card2) == 'Yellow'):
        print('Player 1 wins!')
        player1.append(player2[len(player2)-1])
        player2.pop(len(player2)-1)
    
    if (colour(card1) == 'Black' and colour(card2) == 'Red'):
        print('Player 2 wins!')
        player2.append(player1[len(player1)-1])
        player1.pop(len(player1)-1)

    if (colour(card1) == colour(card2)):
        if (int(value(card1)) > int(value(card2))):
            player1.append(player2[len(player2)-1])
            player2.pop(len(player2)-1)
            print('Both players have the same colour card, player 1 has a high card.  Player 1 wins!')
        else:
            player2.append(player1[len(player1)-1])
            player1.pop(len(player1)-1)
            print('Both players have the same colour card, player 2 has a high card.  Player 2 wins!')
    

def gameLoop(i):
    playerAction(player1, i)
    # print(player1)
    playerAction(player2, i)
    # print(player1)
    checkWinner(str(player1[len(player1)-1]), str(player2[len(player2)-1]))
    input('')

for i in range(1, 16):
    gameLoop(i)

print('\nPlayer 1 has %s cards' % len(player1))
print('Player 2 has %s cards\n' % len(player2))

if (len(player1) > len(player2)):
    print('Player 1 %s is the winner!' % p1)
else:
    print('Player 2 %s is the winner' % p2)


# yellow_cards = ["yellow 1","yellow 2","yellow 3","yellow 5","yellow 6","yellow 7","yellow 8","yellow 9","yellow 10"]
# random.shuffle(yellow_cards)
# random_yellow_card = random.choice(yellow_cards)

# red_cards = ["red 1","red 2","red 3,","red 5","red 6","red 7","red 8","red 9","red 10"]
# random.shuffle(red_cards)
# random_red_card = random.choice(red_cards)

# black_cards = ["black 1","black 2","black 3","black 5","black 6","black 7","black 8","black 9","black 10"]
# random.shuffle(black_cards)
# random_black_card = random.choice(black_cards)

# random_card = []
# random_card.append(random_black_card)
# random_card.append(random_red_card)
# random_card.append(random_yellow_card)

# current_card_pone = random.choice(random_card )
# random_card.remove(current_card_pone)


# print("Player one you got a" , current_card_pone)

# current_card_ptwo = random.choice(random_card)
# random_card.remove(current_card_ptwo)

# print("Player two you got a" ,current_card_ptwo)