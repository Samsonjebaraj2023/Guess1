import random
n = input("Enter the Range to guess a number : ")
if n.isdigit():
    n = int(n)
    if n <= 0 :
        print("Plese Enter a number which is meed to be greater than 0 next time!!")
        quit()
else:
    print("Please enter number next time ")
    quit()
count = 0
Random_num = random.randint(0,n)
while True:
    count +=1
    User_guess = input("You May Guess now: ")
    if User_guess.isdigit():
        User_guess = int(User_guess)
    else:
        print("Please enter a number ")
        break
    if User_guess == Random_num:
        print("You Guess it !!")
        break
    else:
        if User_guess < Random_num:
            print("You were below the number !")
        else:
            print("You were above the number")
print("You Got it in ",count,"Guess")