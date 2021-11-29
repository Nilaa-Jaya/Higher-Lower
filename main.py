from random import randint
from game_data import data
from art import logo
from art import vs
# import os


def Compare(n1, n2):
    global score
    global is_end_game
    print(f"Compare A: {n1['name']}, a {n1['description']}, from {n1['country']}.")
    print(f"\n\n{vs}\n\n")
    print(f"Compare B: {n2['name']}, a {n2['description']}, from {n2['country']}.")
    user_choice = input("Who has more followers? Type 'A' or 'B' :   ")
    if n1['follower_count'] > n2['follower_count'] and user_choice == "A":
        # os.system('cls')
        score += 1
        print(f"\n\n{logo}\n\n")
        print(f"You are right! Current score :  {score}")
        return n2

    elif n1['follower_count'] < n2['follower_count'] and user_choice == "B":
        # os.system('cls')
        score += 1
        print(f"\n\n{logo}\n\n")
        print(f"You are right! Current score :  {score}")
        return n2

    else:
        # os.system('cls')
        print(f"\n\n{logo}\n\n")
        print(f"Sorry, that's wrong. Final Score :  {score}.")
        is_end_game = True
        return {}


is_end_game = False
score = 0
A = {}
B = {}
print(f"\n\n{logo}\n\n")
while not is_end_game:
    if A == {}:
        A = data[randint(0, len(data)-1)]
    B = data[randint(0, len(data)-1)]
    while A['name'] == B['name']:
        B = data[randint(0, len(data)-1)]

    A = Compare(A, B)
