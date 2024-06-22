import random

# create deck and shuffle 
def createShuffledDeck(rank, suits):
    deck = []
    for s in suits:
        for r in rank:
            deck.append(r + "-" + s)
    random.shuffle(deck)
    return deck

# giving user cards
def SendCard(deck, Ace, value):
    card = deck[0]
    # rank of the current card
    r = (card.split("-"))[0]
    del deck[0]

    # ACE case
    if r == "ACE":
        if value + 11 > 21 or Ace:
            value += 1
        else:
            value += 11
            Ace = True
    # JACK, QUEEN, KING case
    elif len(r) > 2:
        value += 10
    # 1 to 10
    else:
        value += int(r)

    # change ACE's value from 11 to 1 if the sum of ranks exceeds 21 
    if value > 21 and Ace:
        value -= 10
        Ace = False
    
    return value, card, Ace

# 13 ranks and 4 suits
rank = ["ACE", "2", "3", "4", "5", "6", "7", 
        "8", "9", "10", "JACK", "QUEEN", "KING"]
suits = ["SPADE", "HEART", "DIAMOND", "CLUB"]

def main():
    # storing cards picked
    card_ls = []
    # summation of card ranks
    value = 0
    Ace = False

    # user's round
    print()
    deck = createShuffledDeck(rank, suits)
    value, card1, Ace = SendCard(deck, Ace, value)
    value, card2, Ace = SendCard(deck, Ace, value)
    card_ls.append(card1)
    card_ls.append(card2)

    # Blackjack case
    if value == 21:
        print("Your current value is Blackjack! (21)")
        print("with the hand: ", ", ".join(card_ls), "\n")
    else:
        print("Your current value is %d" %value)
        print("with the hand:", ", ".join(card_ls), "\n")

    while True:
        Hit = int(input("Hit or stay? (Hit = 1, Stay = 0): "))
        if Hit:
            value, card, Ace = SendCard(deck, Ace, value)
            card_ls.append(card)
            # Blackjack case
            if value == 21:
                print("You draw %s \n" % card)
                print("Your current value is Blackjack! (21)")
                print("with the hand: ", ", ".join(card_ls), "\n")
            # Bust case
            elif value > 21:
                print("You draw %s \n" % card)
                print("Your current value is Bust! (>21)")
                print("with the hand: ", ", ".join(card_ls), "\n")
                print("*** Dealer wins! *** \n")
                return 0
            else:
                print("You draw %s \n" % card)
                print("Your current value is %d" % value)
                print("with the hand: ", ", ".join(card_ls), "\n")
        else:
            print()
            break

    # dealer's round
    d_Ace = False
    d_value = 0
    d_card_ls = []
    hit = False

    d_value, d_card1, d_Ace = SendCard(deck, d_Ace, d_value)
    d_value, d_card2, d_Ace = SendCard(deck, d_Ace, d_value)
    d_card_ls.append(d_card1)
    d_card_ls.append(d_card2)

    # Blackjack case
    if d_value == 21:
        print("Dealer's current value is Blackjack! (21)")
        print("with the hand: ", ", ".join(d_card_ls), "\n")
    # Bust case
    else:
        print("Dealer's current value is %d" % d_value)
        print("with the hand:", ", ".join(d_card_ls), "\n")

    while d_value < 17:
        d_value, d_card, d_Ace = SendCard(deck, d_Ace, d_value)
        d_card_ls.append(d_card)
        print("Dealer draws", d_card)
        hit = True
    print()

    if hit:
        # Blackjack case
        if d_value == 21:
            print("Dealer's current value is Blackjack! (21)")
            print("with the hand: ", ", ".join(d_card_ls), "\n")
        # Bust case
        elif d_value > 21:
            print("Dealer's current value is Bust! (>21)")
            print("with the hand: ", ", ".join(d_card_ls), "\n")
            print("*** You beat the dealer! *** \n")
            return 0
        else:
            print("Dealer's current value is %d" % d_value)
            print("with the hand: ", ", ".join(d_card_ls), "\n")

    # comparision
    if value > d_value:
        print("*** You beat the dealer! *** \n")
    elif value < d_value:
        print("*** Dealer wins! *** \n")
    else:
        print("*** You tied the dealer, nobody wins. *** \n")

main()
while True:
    PlayAgain = input("Want to play again? (y/n): ")
    if PlayAgain == "y":
        print("\n---------------------------------------- \n")
        main()
    else:
        break