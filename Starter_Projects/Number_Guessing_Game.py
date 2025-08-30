from random import randint

lower_num, higher_num = 1, 10
random_number: int = randint(lower_num, higher_num) # Set a number bwt 1 to 10
print(f"The Number Guess between {lower_num} to {higher_num}")
count = 0
while True:
    try:
        user_input: int = int(input("Guess :"))
    except ValueError as e: # valueerror is used for check the input is integer or not
        print("Enter a valid number?")
        continue
    if user_input < random_number: 
        print("Your Guess is Lower.")
        count += 1
    elif user_input > random_number:
        print("Your Guess is Higher.")
        count += 1
    else:
        print("Your Guess is Correct!")
        break # if you guessed it correct then terminate the loop
    
    if count == 3:
        print("Game Over You Lost.")
        break # Within three chance you have to make the guess correctly 
