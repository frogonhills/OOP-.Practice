class Employee:

    raise_amount = 1.04

    def __init__(self , first , last , pay ):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@company.com"


    def fullName(self):
        return '{} {}'.format(self.first , self.last)


    def apply_raise(self):
        self.pay = int(self.pay *1.04)





emp_1 = Employee('rakib' , 'hossain' , 50000 )
emp_2 = Employee('mofiz' , 'faruk' , 20000)

print(emp_1)
print(emp_2)
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print(emp_2.pay)
emp_2.raise_amount = 3
emp_2.apply_raise()
print(emp_2.pay)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(emp_2.__dict__)
print(emp_1.__dict__)