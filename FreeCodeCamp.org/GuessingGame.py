secrete_word = "mizan"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guess = False
guess_limit_remain = guess_limit

while guess != secrete_word and not(out_of_guess):
    if guess_count < guess_limit:
        print("You have: " + str(guess_limit_remain) + " try left")
        guess = input("Enter guess: ")
        guess_count += 1
        guess_limit_remain -= 1
    else:
        out_of_guess = True

if out_of_guess:
    print("Out of Guesses, You Lose!!!!!!!!!!")
else:    
    print("Victory!")