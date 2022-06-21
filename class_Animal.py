from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, type, age, weight, time):
        pass

    @abstractmethod
    def Action(self):
        pass

    @abstractmethod
    def Eat(self):
        print('Ест')
        pass

    @abstractmethod
    def Sleep(self):
        print('Животное спит. Попробуйте связаться с ним после 6 утра.')

    @abstractmethod
    def Shower(self):
        print('Животное сейчас ещё спит.')

    @abstractmethod
    def Activity(self):
        print()
        pass

    @abstractmethod
    def info_weight(self):
        pass

    @abstractmethod
    def info_age(self):
        pass

class Animal2(ABC):
    def __init__(self, sex = 'girl'):
        self.sex = sex

class Dog(Animal, Animal2):
    def __init__(self, name, type, age, weight, time):
        super().__init__(name, type, age, weight, time)
        self.name = name
        self.type = type
        self.age = age
        self.weight = weight
        self.time = time

    def Action(self):
        super().Action()
        if 1 <= time < 9 or 23 <= time < 25:
            self.Sleep()
        elif 9 <= time < 11 or 22 <= time < 23:
            self.Shower()
        elif 11 <= time < 13 or 16 <= time < 18 or 20 <= time < 22:
            self.Eat()
        elif 13 <= time < 16 or 18 <= time < 20:
            self.Activity()

    def Eat(self):
        print(f'Выберите, что сегодня будет есть ваше животное в {time}:00: овощи, капуста, трава, мясо, корм, колбаса.')
        an_food = input('').lower()
        tasty_food = ['мясо', 'корм', 'колбаса']
        not_tasty_food = ['овощи', 'капуста', 'трава']
        if an_food in tasty_food:
            self.weight += 0.5
            self.age += 0.05
            self.info_weight()
            self.info_age()
        elif an_food in not_tasty_food:
            self.weight -= 0.3
            self.info_weight()
        else:
            print('Нет в списке')
            self.weight -= 1
            self.info_weight()

    def Sleep(self):
        print(f'Сейчас время {time}:00, {self.name} спит в будке. Попробуйте связаться с ним после 8 утра.') #переопределение метода

    def Shower(self):
        print(f'Сейчас время {time}:00, {self.name} умывается.') #переопределение метода

    def Activity(self):
        print(f"""Чем займётся {self.name} сегодня в {time}:00 (выберите цифру): 
           1. Пойдёт на прогулку, 
           2. Поплавает в озкрк,
           3. Побегает за палкой""")
        an_action = int(input(''))
        self.weight -= 0.1
        self.info_weight()

    def info_weight(self):
        print(f"Вес = {self.weight}")

    def info_age(self):
        print(f"{self.name} стал старше {self.age}")

    def __protected(self):
        print('Save')


class Cat(Animal):
    def __init__(self, name, type, age, weight, time):
        super().__init__(name, type, age, weight, time)
        self.name = name
        self.type = type
        self.age = age
        self.weight = weight
        self.time = time

    def Action(self):
        super().Action()
        if 1 <= time < 9 or 23 <= time < 25:
            self.Sleep()
        elif 9 <= time < 11 or 22 <= time < 23:
            self.Shower()
        elif 11 <= time < 13 or 16 <= time < 18 or 20 <= time < 22:
            self.Eat()
        elif 13 <= time < 16 or 18 <= time < 20:
            self.Activity()

    def Eat(self):
        print(f'Выберите, что сегодня будет есть ваше животное в {time}:00: овощи, капуста, трава, мясо, рыба, колбаса.')
        an_food = input('').lower()
        tasty_food = ['мясо', 'рыба', 'колбаса']
        not_tasty_food = ['овощи', 'капуста', 'трава']
        if an_food in tasty_food:
            self.weight += 0.5
            self.age += 0.05
            self.info_weight()
            self.info_age()
        elif an_food in not_tasty_food:
            self.weight -= 0.3
            self.info_weight()
        else:
            print('Нет в списке')
            self.weight -= 1
            self.info_weight()

    def Sleep(self):
        print(f'Сейчас время {time}:00, {self.name} спит в шкафу. Попробуйте связаться с ним после 8 утра.') #переопределение метода

    def Shower(self):
        print(f'Сейчас время {time}:00, {self.name} умывается.') #переопределение метода

    def Activity(self):
        print(f"""Чем займётся {self.name} сегодня в {time}:00 (выберите цифру): 
           1. Поиграет с клубком, 
           2. Поточит когти,
           3. Побегает за бабочкой""")
        an_action = int(input(''))
        self.weight -= 0.1
        self.info_weight()

    def info_weight(self):
        print(f"Вес = {self.weight}")

    def info_age(self):
        print(f"{self.name} стал старше {self.age}")



name = input('Введите имя животного: ')
type = input('Введите вид животного (Cat or Dog): ')
age = int(input('Введите возраст животного: '))
weight = int(input('Введите вес животного: '))
print('Вы сами будете определять действие питомца (Да/ Нет)?')
choice = input('').title()
if choice == 'Да':
    time = int(input('Выберите время с 1:00 до 24:00: '))
    if type == 'Dog':
        Dog1 = Dog(name, type, age, weight, time)
        while time <= 24:
            Dog1.Action()
            time = int(input('Выберите время с 1:00 до 24:00: '))
    if type == 'Cat':
         Cat1 = Cat(name, type, age, weight, time)
         while time <= 24:
             Cat1.Action()
             time = int(input('Выберите время с 1:00 до 24:00: '))
else:
    time = int(input('Выберите время с 1:00 до 24:00: '))
    if type == 'Dog':
        Dog1 = Dog(name, type, age, weight, time)
        while time < 25:
            Dog1.Action()
            Dog1._Dog__protected() #Инкапсуляция
            time += 1
            if time == 25:
                print('Новый день')
                time = int(input('Выберите время с 1:00 до 24:00: '))
    if type == 'Cat':
        Cat1 = Cat(name, type, age, weight, time)
        Cat_sex = Animal2()
        print(Cat_sex.sex) #значение по умолчанию
        while time < 25:
            Cat1.Action()
            time += 1
            if time == 25:
                print('Новый день')
                time = int(input('Выберите время с 1:00 до 24:00: '))
