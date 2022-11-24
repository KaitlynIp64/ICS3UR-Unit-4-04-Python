#!/usr/bin/env python3
# Created by: Kaitlyn Ip
# Created on: Nov 2022
# This program asks the user to guess a number between 0 to 9
# and tells the user if the guess is right or wrong

import random


def main():
    # generate a number between 0 to 9
    correct_num = random.randint(0, 9)
    # uses a while loop to continue a sequence of until user guesses the right answer
    while True:
        # get the user number as a string
        user_num_string = input("Input a number between 0 - 9: ")
        try:
            user_num_int = int(user_num_string)
        except ValueError:
            print("")
            print("That is not a valid input.")

        else:
            if user_num_int != correct_num:
                print("You guessed incorrectly! Please try again.")
            else:
                print("You guessed correctly! Thank you for playing!")
                break

        print("\nDone.")


if __name__ == "__main__":
    main()
