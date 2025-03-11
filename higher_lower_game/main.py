import game_data
import art
import random


def compare_checker(compare_a, compare_b):
    while compare_a == compare_b:  # compare_a must not equal to compare_b:
        compare_a = game_data.data[random.randint(0, len(game_data.data))]
        compare_b = game_data.data[random.randint(0, len(game_data.data))]

def le_game():
    game_over = False
    score = 0
    while not game_over:
        print(art.logo)
        compare_a = game_data.data[random.randint(0, len(game_data.data))]
        compare_b = game_data.data[random.randint(0,len(game_data.data))]
        compare_checker(compare_a,compare_b)
        followers_a = compare_a['follower_count']
        followers_b = compare_b['follower_count']

        print(f"Compare A followers: {followers_a}") #for testing
        print(f"Compare B followers: {followers_b}")#for testing

        print(f"Compare A: {compare_a['name']},a {compare_a['description'].lower()} from {compare_a['country']}")
        print(art.vs)
        print(f"Compare B: {compare_b['name']},a {compare_b['description'].lower()} from {compare_b['country']}")

        user_answer = input("Who has more followers? Type 'a' or 'b':   ")

        if user_answer == "a" and followers_a > followers_b:
            score += 1
            print(f"You are right! Current score: {score}")
        elif user_answer == "b" and followers_b > followers_a:
            score += 1
            print(f"You are right! Current score: {score}")
        else:
            print(f"Sorry that is wrong. Final score {score}")
            game_over = True

le_game()

play_again = input("Type y to play again  ")
if play_again == "y":
    print("\n"*20)
    le_game()
