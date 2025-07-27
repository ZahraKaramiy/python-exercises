import random


def welcome():
    print(" ** welcome to  this funny game ** ")
    print("I will guess a number between 1 to 100")
    print(" you have to guess it...")
    print("go go go ")
    print()


def finish(number, count):
    print("..**.. Good Game ..**..")
    print(f"my number was {number} and you found it in {count} guesses.")
    print()
    answer = input("Do you want to play again ? (Y/N) ")
    if answer.upper() in ['Y', 'yes', 'Are']:
        return True
    else:
        return False
    

def win(computer_number, guess):
    return computer_number == guess


def answer(computer_number, guess):
    if computer_number > guess:
        return "my number is larger o_o"
    if computer_number < guess:
        return "Ooooohhhhhaaa you went so large!!! mine is smaller :)"
    
    return " WOw! you win *..* Good guess :))"


def get_a_guess():
    ans = input("Give me your guess number LOve:)) ")
    return int(ans)


welcome()
continue_playing = True
while (continue_playing):
    # computer random number between 1 to 20
    computer_number = random.randint(1, 20)
    
    # start with a wrong guss
    guess = 0
    
    count = 0
    
    while (not win(computer_number, guess)):
        guess = get_a_guess()
        count += 1
        print(answer(computer_number, guess))
        
    continue_playing =finish(computer_number, count)
    