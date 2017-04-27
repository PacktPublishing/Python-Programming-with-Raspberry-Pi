#!/usr/bin/python3

import random

if __name__ == "__main__":
    count = 0
    valid_count = 0
    while True:
        # generate a random number between 0 and 9
        rand_num = random.randrange(0,10)

        # prompt the user for a number
        value = input("Enter a number between 0 and 9: ")

        if value == 'x':
            print("Thanks for playing! Bye!")

        try:
            input_value = int(value)  
        except ValueError as error: 
            print("The value is invalid %s" % error)
        else:
            if input_value < 0 or input_value > 9:
                print("Input invalid. Enter a number between 0 and 9.")
                continue
            
            valid_count += 1   
            if input_value == rand_num:
                print("Your guess is correct! You win!")
                break
            else:
                print("Nope! The random value was %s" % rand_num)
        finally:
            count += 1

    print("You won the game in %d attempts "\
          "and %d inputs were valid" % (count, valid_count))
