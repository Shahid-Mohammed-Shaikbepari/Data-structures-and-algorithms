class Person:
    def set_details(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print('I am ', self.name)
    def greet(self):
        if self.age < 80:
            print('Hi, How are you doing ?')
        else:
            print('Hello, How do you do ?')
        self.display()

# p1 = Person()
#
# p1.name = "shahid"
#
# print(p1.name)


class Book():
    x = 5
    def __init__(self):
        self.x = 100
    def display(self):
        print(self.x)
        print(Book.x)

# b = Book()
# b.display()

class Account:
    rate = 5
a1 = Account()
a2 = Account()

Account.rate = 6
print(Account.rate)
print(a1.rate)
print(a2.rate)