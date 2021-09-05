import random

def myNum(num):
    return [int(b) for b in str(num)]

def noNumTwice(num):
    num2 = myNum(num)
    if len(num2) == len(set(num2)):
        return True
    else:
        return False

def randomNum():
    while True:
        num = random.randint(1000, 9999)
        if noNumTwice(num):
            return num

def BullsAndCows(num, guess):
    bull_cow = [0, 0]
    num2 = myNum(num)
    guess2 = myNum(guess)
    for b, c in zip(num2, guess2):
        if c in num2:
            if c == b:
                bull_cow[0] += 1
            else:
                bull_cow[1] += 1
    return bull_cow

num = randomNum()
countguess = 0
maxguess = 999
cara = "-" * 40

print("Hi there!")
print(cara)
print("I've generated random 4 digit number for you. \n"
      "Let's play a bulls and cows game.")
print(cara)

while maxguess > 0:
    guess = int(input("Enter a number: "))
    if not noNumTwice(guess):
        print("Number shouldn't have 2 same digits. Try again.")
        continue
    if guess < 1000 or guess > 9999:
        print("Enter 4 digit number only. Try again. (Number can't start with 0)")
        print(cara)
        continue

    bull_cow = BullsAndCows(num, guess)
    print(f"{bull_cow[0]} bulls, {bull_cow[1]} cows")
    print(cara)
    maxguess -= 1
    countguess += 1

    if bull_cow[0] == 4:
        print("Correct, you've guessed the right number")
        print(f"in {countguess} guesses!")
        break
else:
    print(f"You ran out of tries. Number was {num}")
