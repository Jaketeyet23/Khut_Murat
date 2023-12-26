def taxi_fare(distance):
    return(round((base + add * distance/140), 2))
    
base = 240
add = 15
distance = int(input("Введите расстояние: "))
print('Стоимость поездки: ', taxi_fare(distance))