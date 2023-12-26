def hypotenuse(first_leg, second_leg):
    return(round((first_leg ** 2 + second_leg ** 2) ** 0.5, 2))
    
first_leg = float(input("Введите первый катет: "))
second_leg = float(input("Введите второй катет: "))
print('Гипотенуза равна:', hypotenuse(first_leg, second_leg))