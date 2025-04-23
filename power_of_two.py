#!/usr/bin/env python3
# Created by: Gustav I
# Created on: April 19, 2025
# This program executes a for loop for a number in range of the user's number.

try:
    # Ask the user for a whole number
    user_input = input("Enter a whole number: ")
    user_num = int(user_input)

    if user_num < 0:
        print("Please enter a non-negative whole number.")
    else:
        # Loop from 0 to user_num and print the square of each number
        for i in range(user_num + 1):
            square = i * i
            print(f"{i}^2 = {square}")
except ValueError:
    # Handle invalid (non-integer) input
    print("Invalid input! Please enter a valid whole number.")
