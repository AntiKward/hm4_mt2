""" Инкапсуляция """

# Публичный класс
# class PublicExample: # Публичный класс
#   def __init__(self, value):
#     self.value = value # Публичный метод
    
#   def info(self):
#     return self.value # Публичный метод
  
# public = PublicExample(32)
# # print(public.info()) # Вызов публичного метода
# # print(public.value) # Доступ к публичному атрибуту

# class ProtectedExample:
#   def __init__(self, value):
#       self._value = value # Защищённый атрибут
      
#   def _info(self):
#     return self._value # Защищенный метод
  
# protected = ProtectedExample(32)
# print(protected._info()) # Это работает но противоречит принципам инкапсуляции
# print(protected._value) # Можно получить значение на прямую но это не рекомендуется

# class PrivateExample: # приватный класс
#   def __init__(self, value):
#     self.__value = value # приватный атрибут
    
#   def __info(self):
#     return f'Приватный класс {self.__value}' # приватный метод
  
#   def test(self):
#     return self.__info() # Публичный метод где мы получаем доступ к приватному методу или атрибуту
  
# private123 = PrivateExample(321)

# Прямой вызов приватного метода вызовет ошибку
# print(private123.__info())

# Прямой вызов приватного метода вызовет ошибку
# print(private123.__value)

# Доступ к приватному атрибуту атрибуту либо методу через name mangling 
# print(private123.test())

import datetime
    
class Car:
  def __init__(self, marka, model, year, mileage):
    self.marka = marka
    self.model = model
    self._year = year
    self.__mileage = mileage
    
  def info(self):
    return f'Марка - {self.marka} \nМодель - {self.model}'
  
  def _calculator_age(self):
    current = datetime.datetime.now().year
    return f'Возраст машины - {current - self._year}'
  
  def __update_milage(self):
    return F'Миль - {self.__mileage}'
    
  def set_mileage(self):
    return f'{self.__update_milage()}'

car = Car("BMV", "X5", 2020, 513)
print(car.info())
print(car._calculator_age())
print(car.set_mileage())

"""
1. Создать класс Computer (компьютер) с приватными атрибутами cpu и memory.
2. Добавить в класс Computer приватный метод make_computations, в котором бы выполнялись арифметические вычисления(‘+’,  ‘-’,  ‘*’,  ‘/’ ) с атрибутами объекта cpu и memory результат вывести красиво с помощью ‘ f ’ .
3. Добавить геттеры к существующим атрибутам.
4. Создать класс Laptop - который наследуется от класса Computer с приватным полем memory_card(карта памяти)
5. Добавить геттеры к существующему атрибуту.
6. Распечатать информацию о созданных объектах с помощью метода info
7. Опробовать все возможные методы каждого объекта
"""
class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    def __make_computations(self):
        plus = self.__cpu + self.__memory
        minus = self.__cpu - self.__memory
        mul = self.__cpu * self.__memory
        div = self.__cpu / self.__memory
        return f"Вычисления:\n{self.__cpu} + {self.__memory} = {plus}\n{self.__cpu} - {self.__memory} = {minus}\n{self.__cpu} * {self.__memory} = {mul}\n{self.__cpu} / {self.__memory} = {div}"

    def computations_info(self):
        return self.__make_computations()

    def get_cpu(self):
        return f'Количество cpu: {self.__cpu}'
      
    def get_memory(self):
        return f'Количество memory: {self.__memory}'

class Laptop(Computer):
    def __init__(self, cpu, memory, memory_card):
        super().__init__(cpu, memory)
        self.__memory_card = memory_card
        

    def info(self):
        comp_info = self.computations_info()
        memory_card_info = f"Количество memory card: {self.__memory_card}"
        return f"{comp_info}\n{memory_card_info}"
      
laptop = Laptop(10, 5, 3)
print('Информация о компьютере')
print(laptop.info())
print(laptop.get_cpu())
print(laptop.get_memory())
