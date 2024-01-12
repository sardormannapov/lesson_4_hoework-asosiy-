#Create a function that takes a list of strings and integers,
# and filters out the list so that it returns a list of integers only.

lst = [1, 2, 3, "a", "b", 4]
lst2 = []

def integer(msv, msv2):
    for num in msv:
        if type(num) == int:
            lst2.append(num)
    print(msv2)


integer(msv=lst, msv2=lst2)