'We are going to write a program that generates a random number and asks the user to'
'guess it'
'If the player guess is higher than the actual number, the program displays lower number please'
'similary if the users guess is too low, the program prints "higher "'
'when the user guesses the correct number, the program displays the number of guesses the player used to arive at the number.'

# # By using while loop
# import random

# x = random.randint(1, 100)

# y = -1
# guesses = 0

# while y != x:
#     y = int(input("Guess the number: "))
#     guesses += 1

#     if y > x:
#         print("Lower number please")

#     elif y < x:
#         print("Higher number please")

# print(f"You guessed the number correctly in {guesses} attempts")


# BY using for loop 
import random; n = random.randint(1,100) 

guesses = 0
for i in range(1,11):
     a = int(input("Guess the number :"))

     guesses +=1
     if a == n:
          print(f"u guessed the number correctly in {guesses} attempts")
          break
     elif a > n:
          print("Lower number plz")

     else:
          print("higher number plz")

else:
     print(f"Oops ! u didnt guess the number it was {n}")          










