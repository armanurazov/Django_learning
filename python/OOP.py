# class creation and instance of the class 

class Student():

    college = 'Seneca' # class object attribute

    def __init__(self, name, grade):  # similar to Constructor in C++
        self.name = name  # attributes
        self.grade = grade

stud1 = Student(name = 'Arman', grade = 80)
print(stud1)

# TASK: Create the dogs.
# MAKE SURE TO READ THE FULL INSTRUCTIONS ABOVE CAREFULLY, AS THE EVALUATION SCRIPT IS VERY STRICT.

class Dog():
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        
dog1 = Dog('Hans', 'German Shepherd')
dog2 = Dog('Lou', 'Lobrador')

print(f'{dog1.name} and {dog2.name} are friends')

# methods

class Circle():
    pi = 3.14
    def __init__(self, radius = 4): #default value 4
        self.radius = radius
    def area(self):
        return self.radius**2 * self.pi

circle1 = Circle(10)
print(circle1.area())

# TASK: Implement the dog class with age translation.
# MAKE SURE TO READ THE FULL INSTRUCTIONS ABOVE CAREFULLY, AS THE EVALUATION SCRIPT IS VERY STRICT.

class Dog():
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    def calculate_human_age(self):
        self.age = self.age*7
        return self.age
        
dog = Dog('Hans', 'German Shepherd', 7)
print(dog.calculate_human_age())



#########################################################
###################  Inheritance  #######################
#########################################################

class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def hello(self):
        print(f'hello {self.first_name}')
    def report(self):
        print(f'I am {self.first_name} {self.last_name}')

class Student(Person):
    def show_grades(self, grade):
        if(grade>70):
            return 'Passed'
        else:
            return 'Failed'
    def __str__(self):
        return f"object Student named: {self.first_name} {self.last_name}"
    def __len__(self):
        return 13 #any number       
        
x = Student('Arman', 'Urazov')
print(x.show_grades(66))   
print(x) 
print(len(x))
# TASK: Implement the Animal class and create two child classes called Cat and Dog.
# MAKE SURE TO READ THE FULL INSTRUCTIONS ABOVE CAREFULLY, AS THE EVALUATION SCRIPT IS VERY STRICT.

class Animal():
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def greet(self):
        print(f"Hi! My name is {self.name} and I am a {self.species}")

class Cat(Animal):
    def sound(self):
        print('meow')
        
class Dog(Animal):
    def sound(self):
        print('ruff')

cat = Cat('Kitty', 'Cat')
cat.sound()


