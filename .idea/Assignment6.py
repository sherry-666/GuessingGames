# #Assignment 6
# #
# Ask user to think of a number between 1 and 100.
# 
# Computer should print a number in that range and ask the user about it.
# User can answer if the number is equal, greater than or less than what she had thought.
# The game continues till computer finds the number that user had thought of..
from typing import Any

lowest_num=0
highest_num=100
equal='equal'
import random
feedback =''  # type: string


print ('Welcome to the game! Think of a number that is between {} and {}, and I will guess it!'.format(lowest_num,highest_num))

while feedback != equal:

    print("current guess range is {}-{}.".format(lowest_num,highest_num))


    guess = random.randint(lowest_num,highest_num)


    feedback=input('Is the number equal, greater than or less than {} ?'.format(guess))
    if feedback == 'equal':
        print ("Yay! I got it correct! I know I'm smart!")
    elif feedback == 'greater than':
        lowest_num = guess

    elif feedback == 'less than':
        highest_num = guess

    else:
        print("Sorry, I dont't understand. Please enter 'equal', 'greater than' or 'less than' for me.")
        



