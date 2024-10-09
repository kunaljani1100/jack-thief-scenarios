# Jack Thief
This repository has been created to simulate the real life card game of jack thief. A regular card game of jack thief is generally played with 52 cards, but this card game can change based on the number of players as well as the number of cards that are assigned per player. These parameters can easily be changed in the `constants.py` file.

## Steps to run the simulation
Run the file `expected_length_of_jack_thief_game.py` to ensure to play the game. The output will show the cards that the player has for each iteration as well as the number of rounds it took to complete the game for a player at each iteration.

## Rules of the gamee jack thief.

1. A card deck is created with even number of cards representing each number and odd number of the card 11, which represents the jack in the deck.
2. All the players are assigned cards equally, while one of the players in the deck is assigned an extra card.
3. All the players remove the pairs from their deck.
4. The game starts now where each player chooses a card at random from the previous deck. If the card chosen forms a pair, then the pair is removed from the player's list of card.
5. This game continues until only one player is left with one jack and all the other cards are removed from the game.
