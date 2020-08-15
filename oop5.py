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




    def __repr__(self):
        return  " Employee ( '{}' , {} , {} ) ".format(self.first , self.last , self.pay)



    def __str__(self):
        return '{} , {}'.format(self.fullName(), self.email)


emp_1 = Employee('rakib' , 'hossain' , 50000 )
emp_2 = Employee('mofiz' , 'faruk' , 20000)

print(emp_1.__repr__())
print(emp_1.__str__())
print(emp_1)