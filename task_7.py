#Create a function that takes an array of values resistance that are connected in series, and calculates the total resistance of the circuit in ohms. The ohm is the standard unit of electrical resistance in the International System
# of Units ( SI).Create a function that takes an array of values resistance that are connected in series, and calculates the total resistance of the circuit in ohms. The ohm is the standard unit of electrical resistance in the International System of Units ( SI).

lst = [16, 3.5, 6]
result = 0

def ohms(msv, rezultat):
    for num in msv:
        rezultat += num
    print(f"{rezultat} ohms")


ohms(msv=lst, rezultat=result)