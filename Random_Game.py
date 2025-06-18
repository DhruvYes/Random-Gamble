import random

random_number1 = random.randint(1, 50)  # gives a random integer from 1 to 100 (inclusive)
print(random_number1)

print("Welcome to Random Gamble")
print("Computer will generate a random number and you have to guess it")
print("Rules are as follows: ")
print("1. There are 3 levels as follows: ")
print("Level 1: 1-50, \nTo pass 1st level guess the word within 10 guesses")
print("Level 2: 1-100, \nTo pass 2st level guess the word within 7 guesses")
print("Level 3: 1-200, \nTo pass 3st level guess the word within 4 guesses")

print("1st Level starts")

count1 = 1     
k = int(input("Enter your guess: "))
print(k)
if(k>random_number1):
        print("Make a smaller guess than", k)
elif(k<random_number1):
        print("Make a bigger guess than", k)
while(k!=random_number1):
    k = int(input("Enter your guess: "))
    print(k)
    count1 = count1 +1
    if(k>random_number1):
        print("Make a smaller guess than", k)
    elif(k<random_number1):
        print("Make a bigger guess than", k)
else:
    print("Congratulations you have guessed the word and your number of guesses are: ", count1)

if(count1<10):
    print("Loading 2nd level")
    random_number2 = random.randint(1, 100)
    print(random_number2)

    count2 = 1
    l = int(input("Enter your guess: "))
    print(l)
    if(l>random_number2):
        print("Make a smaller guess than", l)
    elif(l<random_number2):
        print("Make a bigger guess than", l)
    while(l!=random_number2):
        l = int(input("Enter your guess: "))
        print(l)
        count2 = count2 +1
        if(l>random_number2):
                print("Make a smaller guess than", l)
        elif(l<random_number2):
                print("Make a bigger guess than", l)
    else:
        print("Congratulations you have guessed the word and your number of guesses are: ", count2)
else:
     print("Your number of guesses in 1st round is more than 10 so you LOOSE")


if(count2<7):
    print("Loading 3nd level")
    random_number3 = random.randint(1, 200)
    print(random_number3)

    count3 = 1
    m = int(input("Enter your guess: "))
    print(m)
    if(m>random_number3):
        print("Make a smaller guess than", m)
    elif(m<random_number3):
        print("Make a bigger guess than", m)
    while(m!=random_number3):
        m = int(input("Enter your guess: "))
        print(m)
        count3 = count3 +1
        if(m>random_number3):
                print("Make a smaller guess than", m)
        elif(m<random_number3):
                print("Make a bigger guess than", m)
    else:
        print("Congratulations you have guessed the word and your number of guesses are: ", count3)
else:
     print("Your number of guesses in 2st round is more than 7 so you LOOSE")


if(count3<4):
     print("Congratulations You have won all the 3 levels")
     print("Guesses in 1st round: ", k)
     print("Guesses in 2nd round: ", l)
     print("Guesses in 3rd round: ", m)
else:
     print("You loose")    
