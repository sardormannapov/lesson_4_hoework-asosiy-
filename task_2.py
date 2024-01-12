#Write a function that finds the sum of the first n natural numbers.
num = int(input("enter number: "))
summa = 0

def plus(number, sum):
    for num in range(1, number + 1):
        sum += num
    print(sum)


plus(number=num, sum=summa)