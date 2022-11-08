from abc import ABCMeta, abstractmethod, abstractstaticmethod

class IDepartment(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, employees):
        """ Implement in child class """
    
    @abstractstaticmethod
    def print_department():
        """Implement in child class """
    

class Accounting(IDepartment):

    def __init__(self, employees):
        self.employees = employees
    
    def print_department(self):
        print(f"Accounting Department: {self.employees}")

class Development(IDepartment):
    def __init__(self, employees):
        self.employees = employees
    
    def print_department(self):
        print(f"Development Department: {self.employees}")

class ParentDepartment(IDepartment):
    def __init__(self, employees):
        self.employees = employees
        self.base_employees = employees
        self.sub_depts = []

    def add(self, dept):
        self.sub_depts.append(dept)
        self.base_employees = self.employees 
        self.employees += dept.employees 
    
    def print_department(self):
        print("Parent Department")
        print(f"Parent Department Base Employeess: {self.base_employees}")

        for self.dept in self.sub_depts:
            self.dept.print_department()
            print(f"Total number of employees: {self.employees}")

dept1 = Accounting(200)
dept2 = Development(170)

parent_dept = ParentDepartment(30)
parent_dept.add(dept1)
parent_dept.add(dept2)
parent_dept.print_department()