""""
Aggregation:- In OOPS, it is possible to have a relationship b/w classes when an OBJ of a class becomes the instance variable of another class.
              It is also known as HAS-A Relationship
              Ex:- 1. Car has a Sterio
                   2. Employee has a Bank Account

"""

class Employee:
    _employe_counter = 0
    def __init__(self,emp_name,gender,salary,skills):
        self.employee_name=emp_name
        self.gender=gender
        self.salay=salary
        self.id= Employee.get_employee_id()
        self.skillset=skills # Aggregation
#static method :- same copy of method will be used for all the objects of a class, as static method not belongs to object it does not have self attribute
    @staticmethod
    def get_employee_id():
         Employee._employe_counter+= 1
         return Employee._employe_counter
    def get_employee_skills(self):
        print("Skill Name \t\t Proficiency level \t\t Last used")
        print("------------ \t\t ----------------\t\t -----------")
        for skill in self.skillset:
            print(skill.name +"\t\t\t\t"+ str(skill.skill_proficiency) +"\t\t\t\t\t\t"+ str(skill.last_used))
class skills:
    def __init__(self,skill_name,proficiency_level,last_used):
        self.name=skill_name
        self.skill_proficiency=proficiency_level
        self.last_used=last_used

if __name__ == '__main__':
    skill1=skills("Python",3,2018)
    skill2=skills("Flask",1,2018)
    skill3=skills("C#",5,2018)
    skill4=skills("ASP.Net MVC",4,2018)
    skill5=skills("HTML",5,2016)
    skill6=skills("ELK",2,2017)
    skills_set=[skill1,skill2,skill3,skill4,skill5,skill6]
    emp1= Employee("Avinash","Male",500000,skills_set)
    emp1.get_employee_skills()