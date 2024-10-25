""" Полиморфизм """
# def work_firs():
  
#   num1 = 1
#   num2 = 2

#   string1 = 'Hello'
#   string2 = 'Geeks'

#   print(num1 + num2)
#   print(string1 + string2) 
#   print(len('Python - язык программирование')) # 30
#   print(len(['python', 'JS', 'PHP', 'Scala', 'Ruby'])) # 5
#   print(len({'python': 'Django', 'Aiogram': 'Bot' })) # 2
  
# work_firs()

# class Cat:
#   def __init__(self, name, preferences):
#     self.name = name
#     self.preferences = preferences
    
#   def info(self):
#     print(f'Я кот. Меня зовут {self.name}. мне {self.preferences} Года')
    
#   def make_sound(self):
#     print('Мяу!')
    
# class Dog:
#   def __init__(self, name, preferences):
#     self.name = name
#     self.preferences = preferences
    
#   def info(self):
#     print(f'Я собака. Меня зовут {self.name}. мне {self.preferences} Года')
    
#   def make_sound(self):
#     print('Гаф!')
    
# cat = Cat('Васька', 2)
# dog = Dog('Мухтар', 3)

# for who_is in (dog,cat): 
#   who_is.info()
#   who_is.make_sound()
  
# class PaymentMethod:
#   def pay(self, amount):
#     pass
  
# class CreditCart(PaymentMethod):
#   def pay(self, amount):
#     return f'Сумма {amount}, оплачивается по кредитной карте'
  
# class PayPaL(PaymentMethod):
#   def pay(self, amount):
#     return f'Сумма {amount}, оплачивается по кредитной PayPal'
  
# class BankTransfer(PaymentMethod):
#   def pay(self, amount):
#     return f'Сумма {amount}, оплачивается по банковскому переводу'
   
# payment = [CreditCart(), PayPaL(), BankTransfer()]

# for payments in payment:
#   print(payments.pay(100))
  
# from abc import abstractmethod

# class Vehicle:
#   def start_engine(self):
#     pass
  
#   def stop_engine(self):
#     pass
  
#   def drive(self):
#     pass
  
# class Car(Vehicle):
#   def start_engine(self):
#     return '\/\/\/\/\/Двигатель автомобиля заведена  \/\/\/\/\/'
  
#   def stop_engine(self):
#     return '\/\/\/\/\/Двигатель автомобиля не заведён\/\/\/\/\/'
  
#   def drive(self):
#     return '\/\/\/\/\/        Автомобиль едет        \/\/\/\/\/'
  
# class Bycycle(Vehicle):
#   def start_engine(self):
#     return '\/\/\/\/\/  У велосипеда нету двигателя  \/\/\/\/\/'
  
#   def stop_engine(self):
#     return '\/\/\/\/\/  У велосипеда нету двигателя  \/\/\/\/\/'
  
#   def drive(self):
#     return '\/\/\/\/\/        Велосипед едет         \/\/\/\/\/'
  
# vehicle = [Car(), Bycycle()]

# for vehicles in vehicle:
#   print(vehicles.start_engine())
#   print(vehicles.stop_engine())
#   print(vehicles.drive())
  
  
# Задание: Система оплаты сотрудников

# Описание:
# Ваша задача — создать систему для расчета зарплаты сотрудников, которая демонстрирует абстракцию, наследование и полиморфизм. Не используйте модуль abc, используйте только базовые механизмы Python.

# Требования:
# Базовый класс Employee:

# Создайте класс Employee с методом calculate_salary(), который возвращает нулевую зарплату по умолчанию. Также добавьте метод display_info(), который выводит информацию о сотруднике.
# Конструктор класса должен принимать имя сотрудника и его базовую ставку.
# Классы-наследники для разных типов сотрудников:

# Создайте классы FullTimeEmployee и PartTimeEmployee, которые наследуются от класса Employee.
# Для класса FullTimeEmployee метод calculate_salary должен возвращать зарплату как базовую ставку умноженную на фиксированный коэффициент (например, 1.2).
# Для класса PartTimeEmployee метод calculate_salary должен возвращать зарплату как базовую ставку умноженную на коэффициент, зависящий от количества отработанных часов (например, базовая ставка умноженная на 0.5 за каждый час).
# Использование полиморфизма:

# Создайте функцию process_salary(employee), которая принимает объект типа Employee и вызывает его методы calculate_salary и display_info.
# Функция должна корректно работать для всех производных классов, демонстрируя полиморфизм


class Employee:
  def __init__(self, salary, person_info) -> None:
    self.__salary = salary
    self.__person_info = person_info
    
  def calculate_salary(self):
    return f"Ваша зарплата {self.__salary}"
  
  def display_info(self):
    return f'Ваши данные {self.__person_info}'
  
employee = Employee(12,'Андрей')  
  
class FullTimeEmployee(Employee):
  def __init__(self, salary, person_info):
    super().__init__(salary, person_info)
    
  def calculate_salary(self):
    return f"Ваша зарплата {self.__salary * 1.2} с коэффицентом 1.2"
  
fulltimeemployee = FullTimeEmployee(12,'Илья')
    
class PartTimeEmployee(Employee):
  def __init__(self, salary, person_info, work_time):
    super().__init__(salary, person_info)
    self.work_time = work_time
    
  def calculate_salary(self):
    return f"Ваша зарплата {self.__salary * self.work_time} с коэффицентом отработанных часов"
  
parttimeemployee = PartTimeEmployee(12,"Максим", 7)


def process_salary(employee):
  print(employee.calculate_salary())
  print(employee.display_info())
  
parttimeemployee.process_salary()