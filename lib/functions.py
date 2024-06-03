#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
    return

def greet(name):
    name = "Guido"
    print(f"Hello, {name}!")
    return  

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
    pass

def add(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    return num1 + num2
    pass

def halve(number):
    number = int(number) / 2
    return number
    pass
