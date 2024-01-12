lst = ["Abdulaziz", "Sardor", "Abdurauf", "Iskandar", "Mardon"]
inp = input("Enter: ")
lst2 = []

def find_letter(msv, input, msv2):
    for x in msv:
        if input in x:
            lst2.append(x)
    print(sorted(msv2))


find_letter(msv=lst, input=inp, msv2=lst2)