
#In a range of numbers, identify numbers that are
#multiples of both 3 and 5.
for _ in range (1 ,6):
    number = int(input("enter a number: "))
    if number % 3 ==0 and number % 5 ==0:
        print("this number is multiple of both 3 and 5 : ")
    else :
        print("This number is not multiple of both 3 and 5: ")
