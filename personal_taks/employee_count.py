class Employee:

    employee_count = 0

    def __init__(self, name, position):
        self.name = name
        self.position = position
        Employee.employee_count += 1

    @classmethod
    def get_employee_count(cls):
        return cls.employee_count

e1=Employee("raj",'fresher')
e2=Employee("mark",'head')

print(e2.get_employee_count())