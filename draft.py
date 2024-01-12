lst = [3,4]
lst2 = [4,7]

def find(msv, msv2):
    for num in msv:
        if num in msv2:
            print("true")
            break
    else:
        print("false")

find(msv=lst, msv2=lst2)