import random

low_num = 1
high_num = 10

random_number = random.randint(low_num,high_num)
attempt = 0
max_attempt = 5
correct_guess = False


print(f"Guess the correct number between {low_num}, and the {high_num}")
print(f"You have the {max_attempt} attempts to guess the correct number")

while attempt < max_attempt  and not correct_guess:
    guess = int(input("Guess the correct number: "))
    if guess < 1 or guess > 10:
        print("Out of range, please guess a number between 1 and 10.")
        continue
    attempt +=  1 
    if guess == random_number:
        print(f"congratulations, you guessed correct number {random_number} , in attempt number {attempt}") 
        correct_guess = True
    elif guess < random_number:
        print(f"Too low, Try again")
    elif guess > random_number:
        print("Too high, Try again")

    # match guess:
    #     case _ if guess < random_number:
    #         print("Too low")

    #     case _ if guess > random_number:
    #         print("Too high")
        
    #     case _ if guess == random_number:
    #         print("congrats")

if not correct_guess:
    print(f"Sorry you have used all {max_attempt} attempts, the correct number was {random_number}")