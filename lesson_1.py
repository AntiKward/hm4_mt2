""" ООП - Объектно Ориентированое Програмирование """

# hello_world_geeks_backend = "Geeks" # Змеинный регистр

# HelloWorld = "Geeks" # Верблюжий регистр

# def geeks(num1 : int, num2 : int = 20) -> int:
#     return (num1 * num2)

# print(geeks(20))

# class Car: # Шаблон или чертеж
#     def __init__(self, wheel, motor, body): # __init__ - это конструктор
#         self.wheel = wheel
#         self.motor = motor # self - ссылка на текущий объект
#         self.body = body # атрибут класса
        
#         self.bak = 20
#         self.is_start = False
    
#     def info(self): # функция внутри класса превращается в метод
#         print(f"Колесо - {self.wheel}, Мотор - {self.motor}, Кузов - {self.body} ")
        
#     def start(self):
#         if self.bak > 0:
#             self.is_start = True
#             print(f"Машина заведена")
#         else:
#             print("У машины нет топлива")
            
#     def stop(self):
#         self.is_start = False
#         print("Машина заглушена")
        
#     def drive(self, city):
#         if self.is_start == True:
#             print(f"Машина едет в {city}")
#         else:
#             print("Машина не заведена")
        
# car = Car("R20", "V8", "Sedan") # экземпля́р класса
# car.info() # вызов метода, обращаясь к экземпля́ру
# car.start()
# # car.stop()
# car.drive("Дубай")


# """Домашка №1"""
# class Books:
#   def __init__(self, creater, book_name, year):
#     self.creater = creater
#     self.book_name = book_name
#     self.year = year
    
    
    
#   def info(self):
#     print(f'Книга - {self.creater}, Автор - {self.book_name}, Год - {self.year}')
    
# books = Books(input("Введите название автора: "), input("Введите название книги: "), input("Введите год книги: "))
    
# book.info()

class Fruits:
    def __init__(self,name,color,weight):
        self.name = name
        self.color = color
        self.weight = weight
        
    def info(self):
        return f'Фрукт - {self.name},Цвет - {self.color},Вес - {self.weight}'
    
apple = Fruits("Apple","Red","30g")
banana = Fruits("Banana","Yellow","70g")
mango = Fruits("Mango","yellow-orange","130g")
    
print(f'{apple.info()}; {banana.info()}; {mango.info()}')    

# class Book:
#     def __init__(self,title,author,pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
        
#     def page_check(self):
#         if self.pages <= 100:
#             print(f'У вас маленький слой страниц {self.pages}')
#         elif 200 >= self.pages >= 100:
#             print(f'У вас среднее слой страниц {self.pages}')
#         elif 300 >= self.pages >= 200:
#             print(f'У вас большой слой страниц {self.pages}')
#         else:
#             print('У вас больше трёх ста страниц')
        
#     def info(self):
#         print(f'Название - {self.title},Автор - {self.author},Страниц - {self.pages}')
        
# book = Book('Война и мир', 'Лев Толстой', 286)
# book.info()
# book.page_check()