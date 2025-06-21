class calculator :
    def __init__(self,number):
        self.number=number
        self.square=number**2
        self.cube=number**3
        self.square_root=number**0.5
        @staticmethod
        def greet():
            print("hello")
number=int(input("enter any number  "))
cal=calculator(number)
# print(cal.squre,cal.cube,cal.squre_root)
print(f'''square of {cal.number} is {cal.square}
cube of {cal.number} is {cal.cube}
squre root of {cal.number} is {cal.square_root}''')
