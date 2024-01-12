lst = [-5, -3, -7, -12, 5, -1, 3]
lst2 = []

def morethan0(msv, msv2):
    for num in msv:
        if num > 0:
            lst2.append(num)
    print(msv2)


morethan0(msv=lst, msv2=lst2)