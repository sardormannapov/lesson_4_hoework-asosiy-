names = ["Sarvar", "Sardor", "Sanjar"]

def index(ism):
    for x in ism:
        if "Sardor" in x:
            result = names.index(x)
            print(result)
            break
    else:
        print("-1")


index(ism=names)