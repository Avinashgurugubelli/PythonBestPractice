class Employee:
    _employe_counter=0
    def __init__(self):
        self.employee_name=""
        self.__employee_id= Employee.get_employee_id()
        self.gender=""
        self.__salary=2000 #Private Variable as it defined by 2 underscore symbol @beginning
#Mutator:- Methods used to set value for the private variable
    def set_salary(self,salary):
        self.__salary= salary
#Accessor:- Methods used to get value of the private variable
    def get_salary(self):
        return  self.__salary

        """
        static method :- same copy of method will be used for all the objects of a class,
                        as static method not belongs to object it does not have self attribute hence v can not use r call non static members inside a static method
        """

    @staticmethod
    def get_employee_id():
         Employee._employe_counter+= 1
         return Employee._employe_counter
    def calculate_monthly_salary(self,bonous):
        return self.__salary+bonous

class skill:
    def __init__(self):
        self.skill_name= None
        self.proficiency_level= None

if __name__ == '__main__':
    emp1= Employee();

    emp1.employee_name="Avinash"
    emp1.gender="Male"
    emp1.salary= 5 #As salary is private variable of the employee class it will store as _Employee__salary, here a new attribute only for this
                   #employee obj (emp1) will get created
    #Private variable Accessing
    emp1._Employee__salary=1000  #setting Value for the private Variable
    emp1.set_salary(3000)        #Another way of setting Value for the private Variable by mutator
    emp1_currentmonth_salary=emp1.calculate_monthly_salary(100)
    print(emp1_currentmonth_salary) #output :- 1100 if salary is 1000
    print("Employee 1 :- "+ str(emp1._Employee__employee_id))
    emp1 = Employee();

    emp1.employee_name = "Ravi"
    emp1.gender = "Male"
    print("Employee 2 :- "+ str(emp1._Employee__employee_id))