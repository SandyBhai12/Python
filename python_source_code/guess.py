import random

target=random.randint(1,100)

while True:
     
     userGuess=input("Guess the target or press the (Q) to quit the game ")

     if(userGuess=="Q"):
          print("havent guess")
          break
     
     userGuess=int(userGuess)
     if(userGuess==target):
          print("Success : Guess it Correct")
          break
     elif(userGuess<target):
          print("userGuess is too small . Guess the big number")
     else:
          print("userGuess is too Big . Guess the small number")

print("____________Game Over__________________")
     