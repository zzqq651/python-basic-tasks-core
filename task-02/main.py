from math import sqrt
from abc import ABC, abstractmethod

PI = 3.1414
# Самостоятельная работа №2


print('=' * 10)
print('Задача №1. Конвертация верблюда в змею')

def camel_case_to_snake_case(line: str) -> str:
    if not line:
        return line
    list_index_up_symb = [elem for elem in range(0, len(line)) if line[elem].isupper()]
    if list_index_up_symb[0] != 0:
        list_index_up_symb.insert(0, 0)
    if len(list_index_up_symb) == 1:
        return line.lower()
    list_words = []
    last_ind = 0
    for cur_ind in list_index_up_symb[1:]:
        list_words.append(line[last_ind:cur_ind].lower())
        last_ind = cur_ind
    list_words.append(line[last_ind:].lower())
    return "_".join(list_words)


print(camel_case_to_snake_case('Person'))
print(camel_case_to_snake_case('SuperUser'))
print(camel_case_to_snake_case('SomeCustomName'))
print(camel_case_to_snake_case('anotherCamelCase'))
print(camel_case_to_snake_case(''))



print('=' * 10)
print('Задача №2. Повторение')

class Person:
    def __init__(self, fist_name, last_name):
        self.first_name = fist_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


person = Person("John", "Smith")
print(repr(person.full_name))



print('=' * 10)
print('Задача №3. Неабстрактные формы')

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return PI * self.radius ** 2

    def perimeter(self):
        return 2 * PI * self.radius


rectangle = Rectangle(4, 6)
print(rectangle.area())
print(rectangle.perimeter())
print('---')
circle = Circle(5)
print(circle.area())
print(circle.perimeter())


print('=' * 10)
print('Задача №4. Ошибка суммы')

class SecretResultReached(ValueError):
    pass

def add(param1, param2):
    sum = param1 + param2
    if sum == 42:
        raise SecretResultReached('find secrer value')
    return sum

print(add(5, 5))
try:
    add(40, 2)
except ValueError as e:
    print('find secter value', e)

print('=' * 10)
print('Задача №5*. Габариты экрана')

class Screen:
    def __init__(self, diagonal, pixels_w, pixels_h):
        self.diagonal = diagonal
        self.pixels_w = pixels_w
        self.pixels_h = pixels_h

    @property
    def aspect_ratio(self):
        return self.pixels_w / self.pixels_h

    @property
    def height(self):
        return self.diagonal / sqrt(self.aspect_ratio ** 2 + 1)

    @property
    def width(self):
        return self.aspect_ratio * self.height

    @property
    def height_cm(self):
        return self.height * 2.54

    @property
    def width_cm(self):
        return self.width * 2.54

    @property
    def area(self):
        return self.width * self.height

    @property
    def area_cm(self):
        return self.width_cm * self.height_cm


screen = Screen(
    diagonal=15.6,
    pixels_w=1920,
    pixels_h=1080,
)
print(screen.aspect_ratio)
print(screen.width)
print(screen.width_cm)
print(screen.height)
print(screen.height_cm)
print(screen.area)
print(screen.area_cm)


print('=' * 10)
print('Задача №6*. Валидные скобки')
def valid_parentheses(obj):
    ...