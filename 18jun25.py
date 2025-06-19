"""This script will illustrate concepts of classes, their instances or objects, their attributes and other
concepts related to oop such as abstraction, polymorphism, encapsulation demonstrated through self
describing code blocks"""


# block 1

class Datajob:
    pass

job = Datajob()
print(type(job))

# ex 2

class Cars:
    def __init__(self, model, make):
        self.model = model
        self.make = make

car1 = Cars('polo', 'volkswagen')
print(car1)
print(car1.make)
print(car1.model)

print(type(car1))


car2 = Cars('liva', 'toyota')
print(car2)

print(car2.model)
print(car2.make)

print(type(car2))


# ex 3

class DataPipeline:
    def __init__(self, source, destination, input_format, output_format):
        self.source = source
        self.destination = destination
        self.input_format = input_format
        self.output_format = output_format

    


pipeline1 = DataPipeline('gcp bucket', 'db table', 'csv', 'sql')
print(pipeline1)

print(pipeline1.source)
print(pipeline1.destination)
print(pipeline1.input_format)
print(pipeline1.output_format)



# ex 4

class JobCategory:
    defvalue = 'data engineering'

    def _init_(self, name, code):
        self.name = name
        self.code = code

    cat1 = JobCategory('permanent', 1)
    print(cat1)



"""inheritance in class"""


# logic 1

class Car:
    def __init__(self, model):
        self.model = model
        
class SportsCar(Car):
    def _init_(self, model, manufacturer):
        super().__init__(model)
        self.manufacturer = manufacturer

sscar = SportsCar('ferrari', 'exor')
print(sscar)

print(sscar.model)
print(sscar.manufacturer)


"""This code block illustrates class SportsCar inheriting attribute from class Car using the super() function"""


"""Encapsulation, data hiding, access control in python using single and double leading underscores"""

# illustration 1

class Job:
    def _init_(self):
        self._status = 'immutable'   # Proctected


class Secret:
    def _init_(self):
        self.__code = 'confidential'

# logic 2

class SecureJob:
    def __init__(self, job_name, secret_key):
        self.job_name = job_name
        self.__secret_key = secret_key  # private

    @property
    def secret_key(self):
        raise AttributeError("Access denied!")

    def verify_key(self, key):
        return key == self.__secret_key

# end




    

    

    
         
