from os import system
import time

name = input("What is your name? ")
height = input("How tall are you? ")
age = input("How old are you? ")
weight = input("how much do you weigh? ")

print(f"It's nice to meet you {name}!")
if float(height) < 4:
    print(f"You told me that you are {height} feet tall! Wow that is so short.")
else:
    print(f"You told me that you are {height} feet tall! You are super tall.")

if float(age) < 15:
    print(f"You are only {age} years old? That's so young!")
else:
    print(f"You are {age} years old! Wow you are soooooo old.")

if float(weight) < 65:
    print(f"You weigh only {weight} pounds! Wow that is so light.")
else:
    print(f"You weigh {weight} pounds. That is too heavy.")

time.sleep(5)

system("figlet by the way I am a turtle")
time.sleep(2)
system("open turtle.gif")
print("this program is now over")
