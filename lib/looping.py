#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 0 
    while i <= 10 :
        print(i)
        i += 1
    print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    squared_list = list()

    for item in int_list:
        square = item * item
        squared_list.append(square)

    return squared_list

def fizzbuzz():
    # code goes here!
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0 :
            print("FizzBuzz")
        elif i % 3 == 0 : 
            print("Fizz")
        elif i % 5 == 0 : 
            print("Buzz")
        else: 
            print(i)
