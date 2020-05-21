from abc import ABC, abstractmethod


class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(ABC):

    @abstractmethod
    def __init__(self, code, name, salary):
        self.code = code
        self.name = name
        self.salary = salary
        self.hours = 8

    def calc_bonus(self):
        pass

    def get_hours(self):
        return self.hours


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__departament = Department('managers', 1)

    def calc_bonus(self):
        return self.salary * 0.15

    def get_departament(self):
        return self.__departament.name

    def set_department(self, department, code):
        self.__departament.name = department
        self.__departament.code = code


class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__departament = Department('sellers', 2)
        self.__sales = 0

    def calc_bonus(self):
        return self.__sales * 0.15

    def get_sales(self):
        return self.__sales

    def put_sales(self, valor):
        self.__sales += valor

    def get_departament(self):
        return self.__departament.name

    def set_department(self, department):
        self.__departament.name = department
        self.__departament.code = code

vend1 = Seller(5, 'A', 3000)
ger1 = Manager(6, 'B', 10000)

print(ger1.calc_bonus())
vend1.put_sales(1000)
vend1.put_sales(2000)
print(vend1.get_sales())
print(vend1.calc_bonus())
# print(vend1.get_hours())
print(ger1.get_departament())
print(vend1.get_departament())
