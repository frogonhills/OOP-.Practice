





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
        self.pay = int(self.pay *1.04)




print(Employee.num_of_employee)
emp_1 = Employee('rakib' , 'hossain' , 50000 )
emp_2 = Employee('mofiz' , 'faruk' , 20000)


print(Employee.num_of_employee)

print(emp_1)
print(emp_2)


#emp_1.first = "rakib"
#emp_1.email = "rakib@gogole.com"

#emp_2.email = "jolol@google.com"

#print(emp_1.first)
#print(emp_2.email)


print(emp_1.email)
print(emp_2.email)
print('{} {}'.format(emp_1.first , emp_1.last))

print(emp_2.fullName())
#to run manually including tah class name 

print( 'running from manual :  ' +  Employee.fullName(emp_2))

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

emp_1.raise_amount = 3

# ekhane speciall emp1 er raise ammount value take amu shudhu change korsi baki der ta kori nai 


print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(emp_2.__dict__)