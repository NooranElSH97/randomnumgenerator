import random
##import sys
def guess(x):
  random_num = random.randint(1,x)
  guess = 0
  while guess != random_num:
    guess = int(input(f"give me a number between 1 and {x}"))
    if guess < random_num:
     print("Nah, man, that's too low")
    elif guess > random_num:
     print("Nah, man, that's too high")

  print("Oh, yay, you got it! Guess you're actually quite smart...")

guess(10)
##guess(random.randint(1,sys.maxsize))

def computerguess(x):
  low = 1
  high = x
  feedback = ''
  while feedback != 'c':
    guess = random.randint(low, high)
    feedback = input(f'Is it {guess}?').lower()
    if feedback == 'h':
      high = guess - 1
    elif feedback == 'l':
      low = guess + 1
  print('Yay! I got it correct!')
computerguess(100)