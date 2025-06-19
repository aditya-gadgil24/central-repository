# SCRIPT1

"""Defining class and objects for practice purpose"""

# BEGIN

class Mobilephone:
    def __init__(self, brand, model, price):    # Using constructor for initializing objects
        self.brand = brand
        self.model = model
        self.price = price

# Creating objects of the class

model1 = Mobilephone('Apple', 'iphone16', 115000)
model2 = Mobilephone('GooglePixel', 'Pixel10', 145000)
print(model1.brand)
print(model2.model)
# END

# BEGIN
"""Creating a new class where the objects would hold multiple values for an attribute"""
class Apps:
    def __init__(self, name, platforms, size, category):
        self.name = name
        self.platforms = platforms
        self.size = size
        self.category = category

    def display_info():
        app1 = Apps('netflix', {'android', 'apple'}, '103.32', 'entertainment')
        app2 = Apps('hotstar', {'android', 'apple'}, '98.04', 'entertainment')

        app1.display_info()
        app2.display_info()
        



