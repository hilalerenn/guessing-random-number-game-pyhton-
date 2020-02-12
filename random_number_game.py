import random
import time
random_number= random.randint(1,50)
print("""
****************************
TRY AND GUESS THE NUMBER BETWEEN 1 AND 50 
YOU HAVE 5 GUESSES 
GOOD LUCK :)
****************************


""")
guess=5
while True:
    your_number = int(input("enter your guess:"))
    if(your_number<random_number):
        guess -= 1
        print("processing.....")
        time.sleep(1)
        print("your number is too small. Enter a greater number..")
        print("you have {} guesses left ;) ".format(guess))
        print(" ")

    elif(your_number>random_number):
        guess -= 1
        print("processing.....")
        time.sleep(1)
        print("your number is too great.Enter a smaller number..")
        print("you have {} guesses left ;) ".format(guess))
        print(" ")

    else:
        print("processing.....")
        time.sleep(1)
        print("Congragulations! Your guess is correct ! ")
        print(" ")
        time.sleep(20)
        break
    if(guess==0):
            print("You failed :( You are out of guesses..  THE NUMBER WAS:",random_number)
            print(" ")
            time.sleep(20)
            break
