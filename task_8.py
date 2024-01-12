#Remove enemies from the list of people, even if the enemy shows up twice
inp = input("Enter enemy: ")
lst = ["Adam", "Emmy", "Tanya", "Emmy"]

def enemy_remove(input, msv):
    for x in msv:
        if x == input:
            lst.remove(x)
    print(msv)


enemy_remove(input=inp, msv=lst)