# regular method , class methdo and static method






import datetime

class Employee:

    raise_amount = 1.04
    num_of_employee = 0

    def __init__(self , first , last , pay ):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@company.com"

        Employee.num_of_employee += 1


    def fullName(self):
        return '{} {}'.format(self.first , self.last)


    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)





    @classmethod

    def set_raise_ammount(cls , ammount):
        cls.raise_amount = ammount


    @classmethod

    def from_string(cls ,  emp_str):
        first , last , pay = emp_str.split('-')
        return cls(first , last , pay)



    @staticmethod

    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True









print(Employee.num_of_employee)
emp_1 = Employee('rakib' , 'hossain' , 50000 )
emp_2 = Employee('mofiz' , 'faruk' , 20000)


print(Employee.num_of_employee)

print(emp_1)
print(emp_2)



# ekhane speciall emp1 er raise ammount value take amu shudhu change korsi baki der ta kori nai 


Employee.set_raise_ammount(1.50)

print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)

emp_str_1 = 'Denver-jhon-7000'

first , last , pay = emp_str_1.split('-')

emp_3 = Employee(first , last , pay)

print(emp_3.email)

emp_4_string = 'Coran-jaylm-8000'
emp_4 = Employee.from_string(emp_4_string)
print(emp_4.email)


my_date = datetime.date(2016  , 7 , 11)

print(Employee.is_workday(my_date))