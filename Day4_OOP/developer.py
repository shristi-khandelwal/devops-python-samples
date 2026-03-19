from Day4_OOP.employees import Employees

class Developer(Employees):
    def __init__(self, name, programming_language, age, salary):
        super().__init__(name, age, salary)
        self.programming_language = programming_language

    def display(self):
        super().display()
        print(f"Programming Language: {self.programming_language}")