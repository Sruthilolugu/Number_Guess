import random
print("Hi miss i have a number and i want to check your sensing skills😄 please enter a number that you guessed! and i will check whether it is correct or wrong")
number=random.randrange(1,100)
guess_count=0
chances=7
while guess_count <chances:
    guess_number=int(input("enter your guess number between 1 to 100:"))
    if guess_number==number:
        guess_count+=1
        print(f"wow the number {guess_number} is correct hoorayy🥳! you guessed the number in just {guess_count} attempts")
        break 
    elif guess_number>number:
        print("the guessed number is greater than original number🙃! made another try:")
        guess_count+=1
    elif guess_number<number:
        print("the guessed number is lesser than original number🙃! made another try:")
        guess_count+=1    
    elif guess_count==chances:
        print(f"you have used all your {chances} chances🥲! better luck in next time........")    