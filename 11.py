def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
        return True
    

if __name__ == "__main__":
    num = int(input("Введите целое число: "))
    if is_prime(num):
        print("Число является простым")
    else:
        print("Число не является простым")