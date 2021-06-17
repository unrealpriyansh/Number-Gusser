print("Welcome to my number guesser")
number_to_be_guessed = 20
i=5
for x in range(1,i+1):
    v=int(input("Enter number\n"))
    if v<number_to_be_guessed:
        print("Try again number is lesser by",number_to_be_guessed-v ,end="\n")
    elif v>number_to_be_guessed:
        print("Try again number is greater by",v-number_to_be_guessed)
    elif v==number_to_be_guessed:
        print("Congratulation,You are very right")
        print("Number of try left ->",i-1)
        break
if i==0:
    print("Try from start")
