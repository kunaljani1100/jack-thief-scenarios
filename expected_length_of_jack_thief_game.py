import numpy as np
from constants import numberOfPlayers, numberOfCardsPerPlayer, numberOfCardsInDeck


def createCardDeck(numberOfCards):
    """
    This function creates a card dock based on the number of players and the number of cards per player with an odd number of jack cards with the value 11.
    :param numberOfCards: The number of cards that are present as a part of our deck.
    :return: The created card deck.
    """
    cardDeck = []
    cardDeck.append(11)  # jack is given card number 11
    for i in range(numberOfCards - 1):
        cardDeck.append(int((i / 4) + 1))  # every number has 4 copies
    return cardDeck

def countNumberOfJacks(cardDeck):
    """
    This function counts the number of jacks that are present in the card deck.
    :param cardDeck: The card deck that is being used to play the game.
    :return: The number of jacks i.e. the number of cards having the integer value 11.
    """
    countJacks = 0
    # count the number of jacks since we need to see if the number of jacks are odd or even
    for i in range(len(cardDeck)):
        if (cardDeck[i] == 11):
            countJacks = countJacks + 1
    return countJacks

def makeJacksOdd(cardDeck):
    """
    Checks if the number of jacks are even in the card deck and removes the first card if the number of jacks is an odd number.
    :param cardDeck: The card deck that is being used.
    :return: True if the number of jacks is even, false otherwise.
    """
    # if the number of jacks are even, then we will remove 1 jack from the entire set
    if (countNumberOfJacks(cardDeck) % 2 == 0):
        cardDeck.pop(0)
    return cardDeck

def dealCardsForPlayer(cardList):
    """
    Shuffles the card decks and pass the card to each player.
    :param cardList: The card deck from which cards are assigned to the players.
    :return: The cards that are assigned to each player.
    """

    playerCards = []
    # storing cards of all the  players
    for i in range(numberOfPlayers):
        cardsOfSinglePlayer = []  # cards of the particular player are stored here
        if (i == 0):  # give one extra cards to the first player
            for j in range(numberOfCardsPerPlayer + 1):
                rndnum = len(cardList) * np.random.uniform(0, 1)
                rdnum = int(rndnum)
                cardsOfSinglePlayer.append(cardList[rdnum])
                cardList.pop(rdnum)
        else:  # do not give one extra cards to the other players
            for j in range(numberOfCardsPerPlayer):
                rndnum = np.random.uniform(0, len(cardList))
                rdnum = int(rndnum)
                cardsOfSinglePlayer.append(cardList[rdnum])
                cardList.pop(rdnum)
        # append the values in the end
        playerCards.append(cardsOfSinglePlayer)
    return playerCards

def removeMatchingCards(playerCards):
    """
    Remove all the matching cards for each player.
    :param playerCards: The players and their list of cards.
    :return: The players list without any matching cards.
    """
    for i in range(numberOfPlayers):
        numberOfCardsPaired = 0
        for j in range(len(playerCards[i])):
            for k in range(j):
                # assign mathcing cards 0 value
                if (playerCards[i][j] == playerCards[i][k]):
                    playerCards[i][j] = 0
                    playerCards[i][k] = 0
                    numberOfCardsPaired = numberOfCardsPaired + 2
        numberOfcardsLeft = len(playerCards[i])
        for j in range(numberOfCardsPaired):
            for k in range(numberOfcardsLeft):
                if (playerCards[i][k] == 0):
                    # pop the value of the cards whose value os zero
                    playerCards[i].pop(k)
                    break
            numberOfcardsLeft = numberOfcardsLeft - 1
    return playerCards

def playCardGame(player):
    """
    Play the game where a card is passed from one player to another and removes a matching pair for each player.
    :param player: The player list of cards that is updated in each iteration.
    :return: Number of turns played before a game is completed.
    """
    numberOfRounds = 0
    while (True):
        for i in range(numberOfPlayers):
            if (i == numberOfPlayers - 1):  # passing of cards from 1 player to the other player
                rndnum = len(player[i]) * np.random.uniform(0, 1)
                rdnum = int(rndnum)
                player[0].append(player[i][rdnum])
                player[i].pop(rdnum)
            else:  # other condition of passing of cards from one player to the other
                rndnum = len(player[i]) * np.random.uniform(0, 1)
                rdnum = int(rndnum)
                player[i + 1].append(player[i][rdnum])
                player[i].pop(rdnum)
            numberOfCardsPaired = 0

            if (i == numberOfPlayers - 1):
                nm = 0
                # check if the next player has cards with him or her or not
                while (True):
                    if (len(player[nm]) == 0):
                        if (nm == numberOfPlayers - 1):
                            nm = 0
                        else:
                            nm = nm + 1
                    else:
                        break
                for j in range(len(player[nm])):
                    for k in range(j):
                        if (player[nm][j] == player[nm][k]):
                            player[nm][j] = 0
                            player[nm][k] = 0
                            numberOfCardsPaired = numberOfCardsPaired + 2
                cards_left = len(player[nm])
                for j in range(numberOfCardsPaired):
                    for k in range(cards_left):
                        if (player[nm][k] == 0):
                            player[nm].pop(k)
                            break
                    cards_left = cards_left - 1

            else:
                nm = i + 1
                while (True):
                    if (len(player[nm]) == 0):
                        if (nm == numberOfPlayers - 1):
                            nm = 0
                        else:
                            nm = nm + 1
                    else:
                        break
                for j in range(len(player[nm])):
                    for k in range(j):
                        if (player[nm][j] == player[nm][k]):
                            player[nm][j] = 0
                            player[nm][k] = 0
                            numberOfCardsPaired = numberOfCardsPaired + 2
                cards_left = len(player[nm])
                for j in range(numberOfCardsPaired):
                    for k in range(cards_left):
                        if (player[nm][k] == 0):
                            player[nm].pop(k)
                            break
                    cards_left = cards_left - 1

        numberOfRounds = numberOfRounds + 1
        print(player)
        iscontinue = False

        for i in range(numberOfPlayers):
            if (len(player[i]) > 1):
                iscontinue = True
        if (iscontinue == False):
            break
    return numberOfRounds

cardDeck = createCardDeck(numberOfCardsInDeck)
numberOfJacks = countNumberOfJacks(cardDeck)
cardDeck = makeJacksOdd(cardDeck)
player = dealCardsForPlayer(cardDeck)
player = removeMatchingCards(player)
print(playCardGame(player))
