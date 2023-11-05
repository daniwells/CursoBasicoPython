from PACOTES import textos

class Name:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        textos.title('EMPLOYEE')

        print(f'NAME: {self.name}')
        print(f'SALARY: {self.salary}')

    def increase_salary(self, percentage):

        value_increase = (percentage / 100) * self.salary
        self.salary = self.salary + value_increase

nam = input("What's the name? ")
sal = float(input("What's the salary? "))

employee = Name(nam, sal)

employee.show()

employee.increase_salary(17)

employee.show()