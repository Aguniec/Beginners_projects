"""
Make a two-player Rock-Paper-Scissors game.

"""

print("Please pick one : rock, scissors, paper")

while True:
    game_dictionary = {"rock": 1, "scissors": 2, "paper": 3}
    player1 = str(input("Player 1:"))
    player2 = str(input("PLayer 2:"))
    a = game_dictionary.get(player1)
    b = game_dictionary.get(player2)
    difference = a - b

    if difference in [-1, 2]:
        print("Player1 wins")
    elif difference in [-2, 1]:
        print("Player2 wins")

    answer = input("Do you want to play once again? (Yes or No)")
    if answer == "Yes":
        print("New game will be start")
    else:
        print("Game over")
        break
