# Number guessing game
import random
n = random.randrange(1, 10)
guess = int(input("Enter your gues: "))
while n != guess:
  if guess < n:
    print("Too low")
    guess = int(input("Enter your guess: "))

  elif guess > n:
    print("Too high")
    guess = int(input("Enter your guess: "))

  else:
    break
print("Your guess is right!") 
