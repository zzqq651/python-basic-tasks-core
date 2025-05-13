# Самостоятельная работа №1

# Задача №1. Куб
def make_cube(n):
    return n ** 3

# Задача №2. Повторение
def repeat(x):
    if isinstance(x, str):
        return x * 3
    return str(x) * 2

# Задача №3. Возведение в степень
def create_powers(*args, p=2):
    return [elem ** p for elem in args]

# Задача №4. Разворот числа
def reverse_number(num):
    res = 0
    while num:
        last = num % 10
        res = res * 10 + last
        num //= 10
    return res

# Задача №5*. Рекурсия (задача со звёздочкой)
def fac(n):
    if n <= 1:
        return 1
    return fac(n-1) * n


def main():
    print(make_cube(3))
    print(repeat(123))
    print(create_powers(1, 2, 3, p=2))
    print(reverse_number(12345))
    print(fac(5))

if __name__ == '__main__':
    main()