import game_data
import art
import random

def random_person():
    return random.choice(game_data.data)


score = 0
person_1 = random_person()
while len(game_data.data) != 1:
    person_2 = random_person()

    while person_1 == person_2:
        person_2 = random_person()

    print(f"Compare A: {person_1['name']}, a {person_1['description']}, from {person_1['country']}")
    print(art.vs)
    print(f"Compare B: {person_2['name']}, a {person_2['description']}, from {person_2['country']}")

    guess = input("Who has more followers: ").upper()

    # remove the person that has smaller value from the data so that it would not get picked again by the random picker function
    if person_1["follower_count"] > person_2["follower_count"] and guess == 'A':
        game_data.data.remove(person_2)
        person_1 = person_1
    elif person_2["follower_count"] > person_1["follower_count"] and guess == 'B':
        game_data.data.remove(person_1)
        person_1 = person_2
    elif person_1["follower_count"] == person_2["follower_count"]:
        game_data.data.remove(person_2)
        person_1 = person_1
    else:
        print("\n\tYou lose.")
        break

    score += 1
    print(f"\n\tYou are correct! Current score: {score}\n\n\n")
else:
    print("\tCongratulations! You completed the game")


# todo list:
# ask the user for the guess on which has more follower - DONE
# create a function that tells wheter the guess is correct or not - DONE
# create a while loop that breaks when the user guessed wrong - done
# i need to know who is the winner and give the value of the winner to the person_1 - DONE
# since there is repeated value in the list, i should add an elif for the tie - DONE
# for every correct guess of the user adds 1 to the score - DONE
# stop the while if the user reach the maximum
# highest score is 49 because 50 is the number of dictionaries inside the list



# CHECK THE LIST IF THERE ARE REPETITIVE VALUE
# import game_data

# follower_counts = set()  
# i = 1
# for item in game_data.data:
#     count = item["follower_count"]
#     if count in follower_counts:
#         print(f"{i}. There is a repetition:", count)
#     else:
#         follower_counts.add(count)  
#         print(f"{i}. No repetition:", count)
#     i+=1
    