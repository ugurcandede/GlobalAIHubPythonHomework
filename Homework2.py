"""
        Global AI Hub  
    Introduction to Python 
    Homework II — Ugurcan Dede
"""

from datetime import datetime

today = datetime.today()

print("Hello, can you introduce yourself?\n")
name = input("What is your name?\n")

surname = input("Nice to meet you {}\nWhat is your surname?\n".format(name))

year = int(input("Please enter birth year\n"))
age = today.year - year

user = [name, surname, age]

print("\nYour entered values")
for u in user:
    print(u)

if age < 18:
    print("\nYou cant go out because its too dangerous")
else:
    print("\nYou can go to the street")
