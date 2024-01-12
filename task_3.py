lst = ["arrey", "print", "return", "index", "reverse"]
lst2 = ["arrey", "print", "return", "index", "reserve"]

def clone(msv, msv2):
    for num in msv:
        for num2 in msv2:
            if num == num2:
                print("1")
                break
        else:
            print("-1")


clone(msv=lst, msv2=lst2)