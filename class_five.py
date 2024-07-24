#USAGE OF DESTRUCTOR

'''class resourcemanager:
    def __init__(self, file_name):
#CONSTRUCTOR: OPEN THE FILE FOR WRITTING
        self.file = open(file_name, 'w')
        print(f"File{file_name}opened")

    def write_to_file(self, data):
#METHOD TO WRITE DATA TO THE FILE
        self.file.write(data)

    def __del__(self):
#DESTRUCTOR: CLOSE THE FILE
        self.file.close()
        print("File closed")

#CREATING AND USING THE resourcemanager OBJECT
resource = resourcemanager('practice.txt')
resource.write_to_file("this is a test")
# deleting the object to trigger the destructor
del resource

#INHERITAN(CODE REUSABILITY,MAINTAINABILITY)

class vehicle:
    def __init__(self,make,model):
        self.make = make
        self.model = model

    def start(self):
        print(f"The {self.make} {self.model} is starting")

#DERIVED CLASS
class car(vehicle):
    def __init__(self,make,model,number_of_doors):
        #call the constructor of the base class
        super().__init__(make,model)
        self.number_of_doors = number_of_doors

    def honk(self):
        print("Honk! Honk")

#CREATING AN INSTANCE OF CAR
my_car = car("TOYOTA","Corolla",4)
my_car.start()
my_car.honk()


class shape:
    def __init__(self,color):
        self.color = color

    def name(self):
        print(f"the name of shape is {shape}")


class circle(shape):
    def __init__(self,color,radius):
        super(). __init__(color)
        self.radius = radius

class square(shape):
        def __init__(self, color, sides):
            super().__init__(color)
            self.sides = sides

    def area(self):
        nummber = 4* self.value_of_side
       print("hello")

my_circle = circle("yellow",4)
my_circle.name()
my_circle.area()'''

#MRO  stands for method resolution order [mro() or __mro__]
class A:
    def method(self):
        print("method in class A")

class B(A):
    def method(self):
        print("method in class B")

class C(A):
    def method(self):
        print("method in class C")

class D(B,C):
    pass

d = D()
d.method()
print(D.mro())





