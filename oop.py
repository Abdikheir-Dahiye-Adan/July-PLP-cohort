
#  activity 1

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def write(self):
        print(f"{self.title} is written by {self.author} in {self.year}")

        # adding inheritance
class EBook(Book):
    def __init__(self, title, author, year, pages):
        super().__init__(title, author, year)
        self.pages = pages

    def read(self):
        print(f"{self.title} by {self.author} published in {self.year} has {self.pages} pages")
my_hardbook = EBook("The Chosen One", "George Mark", "1950", 300)
my_hardbook.read()


      # activity 2
class Animal:
    def __init__(self, name):
        self.name = name
    def move(self):
        print(f"{self.name} is moving")
class Bird(Animal):
    def move(self):
        print(f"{self.name} is running")
class Fish(Animal):
    def move(self):
        print(f"{self.name} is swimming")
class Mammal(Animal):
    def move(self):
        print(f"{self.name} is walking")
animals = [Bird("Eagle"), Fish("Shark"), Mammal("Dog")]
for animal in animals:
    animal.move()

