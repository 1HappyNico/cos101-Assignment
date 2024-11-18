#Cos 101 Assignment
print("Welcome to Physcis 101 and MTH 101")

first_name = "Emmanuel"
middle_name = "Manasoko"
last_name = "Mamman"
department = "Info Technology"
matric_num = "BHU/24/04/10/0037"

print(first_name,middle_name,last_name,matric_num,department)

def scienctific_formulas():

    velocity = int(input("Enter value for velocity"))
    time = int(input("Enter value for time"))
    accelaration= velocity//time
    print(f"The accelaration is {accelaration} m/s")

    length = int(input("Enter Value for length"))
    breath = int(input("Enter value for breath"))
    area = length * breath
    print(f"The Area is {area} cm^2")

    mass = int(input("Enter value for mass"))
    volume: int = int(input("Enter value for volume"))
    density = mass//volume
    print(f"The Density is {density} kgm^3")

    force = int(input("Enter value for force"))
    area = int(input("Enter value for area"))
    pressure = force//area
    print(f"The Pressure is {pressure} N/m^2")

    mass = int(input("Enter value for mass"))
    accelaration = int(input("Enter value for accelaration"))
    force = mass * accelaration
    print(f"The Force is {force}N")
scienctific_formulas()





