import random

def guess (ending_range):
 random_number = random.randint(1,ending_range)
 guess = 0
 while guess != random_number:
      guess = int(input("Enter a number between 1 and " + str(ending_range) + " : "))
      if guess>random_number:
          print("Sorry! Try again Guess is too high")
      elif guess<random_number:
          print("Sorry! Try again Guess is too Low")

          print("Yeah! You have guessed the number " + str(random_number) + "Correctly.")
def computer_guess(ending_range):
    low = 1
    high = ending_range
    feedback = ''
    while feedback !='c':
        if low != high:
            guess =random.randint(low,high)
        else:
            guess = low
            feedback = input("Is the number " + str(guess) + "is too high (h), too low or is it correct (c)")
            if feedback == 'h':
                high = guess - 1
            elif feedback == 'l':
                low = guess + 1
                print("Thank God Guessed the number is correctly!")
                computer_guess(100)