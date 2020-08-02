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


# etar maddhome amra parrent class  er akj korte parbo jemn employee create kora 
# ekhne amra j value ba function use korbo ta ekhnner tai use hobe abut ja ja ekhne nai ta ta employee class er gulai use hobe 
class Developer(Employee):    
    raise_amount = 1.10

    def __init__(self , first , last , pay  , prog_lang):

        super().__init__(first , last , pay)
        self.prog_lang = prog_lang








emp_1 = Employee('rakib' , 'hossain' , 50000 )
emp_2 = Employee('mofiz' , 'faruk' , 20000)

dev_1 = Developer('mj' , 'Developer', 2500 , 'python')
dev_2 = Developer('nj' , 'Developer', 28000 , 'java')


# print(dev_1.email)
# print(dev_2.email)

# print(help(Developer))   eta diye  kon theke ki ki ashtese ta dekha jay 

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
print(dev_1.prog_lang)