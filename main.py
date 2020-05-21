from abc import ABC, abstractmethod


class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(ABC):

    @abstractmethod
    def __init__(self, code, name, salary, department):
        self.code = code
        self.name = name
        self.salary = salary
        self.hours = 8
        self.__department = department

    @abstractmethod
    def calc_bonus(self):
        pass

    def get_hours(self):
        return self.hours

    def get_departament(self):
        return self.__department.name

    def set_department(self, department, code):
        self.__department.name = department
        self.__department.code = code


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('managers', 1))

    def calc_bonus(self):
        return self.salary * 0.15


class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('sellers', 2))
        self.__sales = 0

    def calc_bonus(self):
        return self.__sales * 0.15

    def get_sales(self):
        return self.__sales

    def put_sales(self, valor):
        self.__sales += valor
