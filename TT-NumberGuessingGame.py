# """
# Project 1 - Number Guessing Game
# --------------------------------

# For this first project you can use Workspaces. 

# NOTE: If you prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

# """


    # """Psuedo-code Hints
    
    # When the program starts, we want to:
    # ------------------------------------
        # 1. Display an intro/welcome message to the player.
        # 2. Store a random number as the answer/solution.
        # 3. Continuously prompt the player for a guess.
        #   a. If the guess greater than the solution, display to the player "It's lower".
        #   b. If the guess is less than the solution, display to the player "It's higher".
        # 4. Once the guess is correct, stop looping, inform the user they "Got it"
        #   a. and show how many attempts it took them to get the correct number.
        # 5. Save their attempt number to a list.
        # 6. At the end of the game, show the player, 1) their number of attempts, 2) the mean, median, and mode of the saved attempts list.
            
    
    # ( You can add more features/enhancements if you'd like to. )
    # """
    # write your code inside this function.

import statistics
import random

tryLst = []
highScore = 1000

def start_game():
    global highScore
    print("Welcome, time to guess numbers, sucker.")
    print(f"The current High Score is {highScore} attempts, don't hurt yourself trying to beat it.")
    answer = random.randint(1,10)
    guess = 0
    # "wrong" variable actually would be defined as "# of attempts" 
    wrong = 0
    while guess != answer:
        try:
            guess = int(input("Go ahead and start guessing."))
        except ValueError as e:
            print("Please enter a number 1-10.")
            continue
        if guess < 1 or guess > 10:
            print("Please enter a number 1-10.")
        elif guess > answer:
            print("Go Lower")
            wrong += 1
        elif guess < answer:
            print("Go Higher")
            wrong += 1
        elif guess == answer:
            print("You got it, yeehaw!")
            wrong += 1
            tryLst.append(wrong)
            print(f"It took you {wrong} attempts to get it right. Mean: {statistics.mean(tryLst)} Median: {statistics.median(tryLst)} Mode: {statistics.mode(tryLst)}")
            if wrong < highScore:
                highScore = wrong
                print(f"Hey! You got a new High Score of {highScore}! I knew it all along, kid!")
            elif wrong == highScore:               
                print(f"You matched the High Score with {highScore} attempts, not bad, I guess. Probably a fluke.")
            playagain()



            
        
        
    

        # 7. Ask the player if they want to play again.
def playagain():
    answer = input("""Would you like to play again? Type "yes" or "no" """)
    if answer.lower() == "yes":
        start_game()
    elif answer.lower() == "no":
        print("Oh, guess that was too hard for you.")
    else:
        playagain()





# Kick off the program by calling the start_game function.
start_game()

