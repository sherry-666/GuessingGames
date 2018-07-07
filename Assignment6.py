# #Assignment 6
# #
# Ask user to think of a number between 1 and 100.
# 
# Computer should print a number in that range and ask the user about it.
# User can answer if the number is equal, greater than or less than what she had thought.
# The game continues till computer finds the number that user had thought of..
from typing import Any

#Logic: start with guess = highest_num/2
# If answer is higher than guess:
#  lowest_num = guess
#loop until answer is lower than the guess:
#  highest_num = guess
#

lowest_num=0
highest_num=100
equal='equal'
import random
feedback =''  # type: string


print ('Welcome to the game! Think of a number that is between {} and {}, and I will guess it!'.format(lowest_num,highest_num))

while feedback != equal:

    #for testing purpose:
    #print("current guess range is {}-{}.".format(lowest_num,highest_num))


    guess = ((highest_num-lowest_num)//2)+lowest_num

    feedback=input('Is the number =, > or < {} ?'.format(guess))
    if feedback == '=':
        print ("Yay! I got it correct! I know I'm smart!")
        break
    #when answer > guess, set guess as lowest_num
    elif feedback == '>':
        lowest_num = guess

    #when answer < guess, set guess as new highest_num
    elif feedback == '<':
        highest_num = guess

    else:
        print("Sorry, I dont't understand. Please enter '=', '>' or '<' for me.")
        



