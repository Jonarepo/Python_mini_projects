# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 16:55:17 2022

@author: Admin
"""


import random
Num_digits = 3  
max_guess = 10


def main():
    print("""Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com
I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say: That means:
    
Pico One digit is correct but in the wrong position.
Fermi One digit is correct and in the right position.
Bagels No digit is correct.

For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.""".format(Num_digits))

    while True:
        secretnum = getsecretnum()
        print("I have thought up a number.")
        print("You have {} guesses to get it." .format(max_guess))
        
        numguess = 1
        while numguess <= max_guess:
            guess = ''
            while len(guess) != Num_digits or not guess.isdecimal():
                print('Guess #{}: '.format(numguess))
                guess = input('>')
                
            clues = getclues(guess, secretnum)
            print(clues)
            numguess += 1
                
            if guess == secretnum:
                break
            if numguess > max_guess:
                print('You ran out of guess')
                print('The answer was {}.'.format(secretnum))
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')
                    
def getsecretnum():
    numbers = list('0123456789')
    random.shuffle(numbers)
    
    secretnum = ''
    for i in range(Num_digits):
        secretnum += str(numbers[i])
    return secretnum

def getclues(guess, secretnum):
    if guess == secretnum:
        return 'You got it!!'
    
    clues=[]
    
    for i in range(len(guess)):
        if guess[i] == secretnum[i]:
            clues.append('Fermi')
        
        elif guess[i] in secretnum:
            clues.append('Pico')
    
    if len(clues) == 0:
        return 'Bagles'
    
    else:
        
        clues.sort()
        return''.join(clues)
        
if __name__ == "__main__":
    main()
        
            

