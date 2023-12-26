def is_power_of_three(n):
    power = 1
    while power <= n:
        if power == n:
            return True
        power *= 3
        return False


n = int(input('Введите целое число N: '))
print(is_power_of_three(n))