"""
Make a two-player Rock-Paper-Scissors game.

"""


while True:
    print("Please pick one : rock, scissors, paper")
    game_dictionary = {"rock": 1, "scissors": 2, "paper": 3}
    player1, player2 = input("Player 1:"), input("Player 2:")
    difference = game_dictionary.get(player1) - game_dictionary.get(player2)

    if difference in [-1, 2]:
        print("Player1 wins")
    elif difference in [-2, 1]:
        print("Player2 wins")
    else:
        print("Dead-heat")

    answer = input("Do you want to play once again? (Yes or No)")
    if answer == "Yes" or "yes":
        print("New game will be start")
    else:
        print("Game over")
        break
