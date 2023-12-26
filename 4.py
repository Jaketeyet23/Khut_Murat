A = int(input("Введите число A:"))
B = int(input("Введите число B:"))
sum_even = 0
sum_odd = 0
for num in range(A,B+1):
    if num % 2 ==0:
        sum_even += num
    else:
        sum_odd += num
print("Сумма четных чисел:", sum_even)
print("Сумма нечетных чисел:", sum_odd)
