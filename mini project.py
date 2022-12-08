from random import * # the python import random module which define the series of function
import os#allows us to run a commend in python script

print("Here are some rules of game you must follow before playing it.")
print("\t1.You Must guess the number between a to b.")
print("\t2.You Will Have Maximum three chances to guess.")
print("\t3.You Will Have Minimum one chances to guess.")

a = int(input("Enter the starting index for generating the number : "))
b = int(input("Enter the ending index for generating the number : "))

random_value = randint(a, b)

count = 0
win = 0
# print("The random Generated value was : ", random_value)

while (count < 3): #
  count += 1
  userGuess = int(input("Enter your number: "))
  if (userGuess == random_value):
    os.system('cls')
    print("\t\t\tCongratulations!!😍😍😍 You Guessed it right in ", count,
          " times.")
    win += 1
    break
  elif (userGuess > random_value):
    print("Your guess is more then the generated random value.. Try Again..")
  elif (userGuess < random_value):
    print("Your guess is less then the generated random value.. Try Again..")
  if (count == 3):
    os.system('cls')
    print("\t\t\tThe random Generated value was : ", random_value)
    print("\t\t\tBetter Luck Next Time!!😥😥😥")

print("You won : ", win, "times.")


