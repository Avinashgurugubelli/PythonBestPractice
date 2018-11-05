""""
Inheritance enables new classes to receive—or inherit—the properties and methods of existing classes.
we learned that an object is a self-contained component that contains properties and methods needed to make a certain type of data useful.
we also learned that a class is a blueprint or template to build a specific type of object and that every object is built from a class.
Inheritance is a way to express a relationship between blueprints (classes).
It's a way of saying: I want to build a new object that is similar to one that already exists, and instead of creating the new class from scratch,
I want to reference the existing class and simply indicate what's different.

    - It also called as IS-A Relationship
    Ex:- Car is a type of vehicle
"""

class Employee:
    _employe_counter=0
    def __init__(self,basic_salary):
        self.basic_salary= basic_salary
        self.employee_id= Employee.get_employee_id()
        self.total_salary= None
    @staticmethod
    def get_employee_id():
        Employee._employe_counter += 1
        return Employee._employe_counter
    def get_total_salary(self):
        self.total_salary=self.basic_salary
        print("Employee Salary: " + str(self.total_salary))
        #return  self.total_salary

class softwareEngineer(Employee):
    def __init__(self,basic_salary,incentive):
        super().__init__(basic_salary)
        self.employee_performance_incentive=incentive
    def get_total_salary(self):
        self.total_salary=self.basic_salary+self.employee_performance_incentive
        print("Employee Performance incentive:"+ str(self.employee_performance_incentive))
        print("TOtal Salary of an software engineer with employee id "+str(self.employee_id)+" : "+str(self.total_salary))


class TechnologyAnalyst(Employee):
    def __init__(self,basic_salary,company_Performance_incentive):
        super().__init__(basic_salary)
        self.company_Performance_incentive=company_Performance_incentive
    def get_total_salary(self):
        self.total_salary=self.basic_salary+self.company_Performance_incentive
        #self.total_salary=super().get_total_salary()+self.company_Performance_incentive
        print("company Performance incentive:"+ str( self.company_Performance_incentive))
        print("TOtal Salary of an Technology Analyst with employee id "+str(self.employee_id)+" : "+str(self.total_salary)+"\n")


class InformationManagementDesk:
    def printEmployeeDetails(self,employee):
        print("Employee ID: "+ str(employee.employee_id))
        employee.get_total_salary()

if __name__ == '__main__':
    emp1= Employee(2000)
    infoDesk= InformationManagementDesk()
    infoDesk.printEmployeeDetails(emp1)

    softwareEngineer_obj= softwareEngineer(5000,500)
    infoDesk.printEmployeeDetails(softwareEngineer_obj)

    ta= TechnologyAnalyst(8000,800)
    infoDesk.printEmployeeDetails(ta)