# Shree

x = 7
while x < 1000:
    print('Current value of x is:', x)
    x = x * 1.75
# end of code block

# defining function

def profit(sales, cost):
    return sales - cost
# calling function with arguments
income = profit(1299345, 761245)
print('The gross profit from this months sale is:', income)
# end of code block

# code block for defining class

class Car:
    def __init__(self, make, model, year, color, fuel):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.fuel = fuel
    
def describe_car(self):

    car_1 = Car('volkswagen', 'polo', 2023, 'curcuma yellow', 'petrol')
    car_2 = Car('skoda', 'superb', 2024, 'wine red', 'diesel')
    car_1.describe_car()
    car_2.describe_car()

# end of code block


# new code block

class Patient:
    def __init__(self, name, age, gender, aadhar):
        self.name = name
        self.age = age
        self.gender = gender
        self.aadhar = aadhar

    def patient_info(self):
        
# creating patient objects

patient_1 = Patient('shamita mehra', 46, 'female', 453423324523)
patient_2 = Patient('Taran Sachdeva', 53, 'male', 343456340934)

patient_1.patient_info()
patient_2.patient_info()
# end of code block

# control flow
# conditional statements

x = 19
if x < 15:
    print('Push to category-a')
elif x == 15:
    print('Push to category-b')
else:
    print('Push to category-c')
# end of code block


# loops

# for loop
for x in range(100)
print(x)