#!/usr/bin/env python3

def happy_new_year():
    # Prints a countdown from 10 to 1, then prints "Happy New Year!"
    for i in range(10, 0, -1):
        print(i)
    print("Happy New Year!")

def square_integers(int_list):
    # Returns a list of squared integers
    return [i ** 2 for i in int_list]

def fizzbuzz():
    # Prints numbers from 1 to 100, replacing multiples of 3 with "Fizz",
    # multiples of 5 with "Buzz", and multiples of both with "FizzBuzz"
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
