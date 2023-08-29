import random

NUM = random.randint(1, 100)
print(NUM)  

def guess_the_number():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    max_attempts = 10 if difficulty == 'easy' else 5

    for attempt in range(max_attempts, 0, -1):
        print(f"You have {attempt} attempts to guess the number.")
        guess = int(input("Make a guess: "))

        if guess < NUM:
            print("Too low.") 
        elif guess > NUM:
            print("Too high.")  
        else:
            print(f"You got it! The number was {NUM}")
            break
    
        if attempt != 1:
            print("Try again.")
    else:
        print("You've run out of guesses, you lose.")


if __name__ == "__main__":
    guess_the_number()