'''Описание:
Ваша задача — разработать систему управления животными в зоопарке, используя принципы абстракции, наследования и полиморфизма.

Требования:
Базовый класс Animal:
Создайте класс Animal с методами make_sound() и display_info().
Конструктор класса должен принимать имя животного и его возраст.
Классы-наследники для разных видов животных:
Создайте классы Lion и Elephant, которые наследуются от класса Animal.
Для класса Lion метод make_sound должен выводить "Рррр!".
Для класса Elephant метод make_sound должен выводить "Ууууу!".
Каждый класс должен также переопределить метод display_info, чтобы выводить специфическую информацию о животном.
Использование полиморфизма:
Создайте функцию introduce_animal(animal), которая принимает объект типа Animal и вызывает его методы make_sound и display_info.
Функция должна корректно работать для всех производных классов.'''

class Animal:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def make_sound(self):
    pass
  
  def display_info(self):
    pass
  
class Lion(Animal):
  def __init__(self, name, age):
    super().__init__(name, age)
    
  def make_sound(self):
    return "Рррр!"
  
  def display_info(self):
    return(f'животное - {self.name}, возраст - {self.age}')
  
lion = Lion("Lion", 3)
  
class Elephant(Animal):
  
  def make_sound(self):
    return "Ууууу!"
  
  def display_info(self):
    return(f'животное - {self.name}, возраст - {self.age}')
  
elephant = Elephant("Elephant", 7)

def introduce_animal(animal):
  for animal in (lion, elephant):
    print(f'Это {animal.display_info()}, Его {animal.make_sound()}')
    
introduce_animal('Who is this?')