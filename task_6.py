lst = [10, 5, 3, 7, 8]
inp = int(input("Enter number: "))

def append(msv, input):
    for num in msv:
        if num == input:
            lst.remove(num)
            lst.append(num)
            print(msv)
            break
    else:
        print("we don't have this number")


append(msv=lst, input=inp)