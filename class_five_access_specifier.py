#ACCESS SPECIFIER [Public(no need of special syntax),Private(self_),Protected(self__)]
'''class car:
    def __init__(self,make,model):
        self._make = make
        self._model = model

    def _display_info(self):
        print(f"Make: {self._make}, Model: {self._model}")

class electriccar(car):
    def display_info(self):
        self._display_info()


car = car("toyota","corolla")
print(car._make)
car._display_info()


#use name mangling[avoiding name clashes,encapsulation]
#ADDING NESTED CLASS
class outer_class():
    def __init__(self):
        self.outer_value = "this is an outer class"

    def display_outer(self):
        print(self.outer_value)

    class inner_class():
        def __init__(self):
            self.inner_value = "this is an inner class"

        def display_inner(self):
            print(self.inner_value)

outer = outer_class()
inner = outer.inner_class()
inner.display_inner()

#integrating inner class with outer class
class outer_class():
    def __init__(self):
        self.outer_value = "this is an outer class"
        self.inner = self.inner_class()

    def display_outer(self):
        print(self.outer_value)
        self.inner.display_inner()


    class inner_class():
        def __init__(self):
            self.inner_value = "this is an inner class"

        def display_inner(self):
            print(self.inner_value)

outer = outer_class()
outer.display_outer()'''

#understanding scope and access
class outer_class():
    def __init__(self):
        self.outer_value = "this is an outer class"
        self.inner = self.inner_class(self)

    def display_outer(self):
        print(self.outer_value)


    class inner_class():
        def __init__(self,outer_instance):
            self.inner_value = "this is an inner class"
            self.outer_instance = outer_instance

        def display_inner(self):
            print(self.inner_value)
            self.outer_instance.display_outer()

outer = outer_class()
outer.inner.display_inner()



x = (1,2,3)
#del(x[1])
#x[0] = 8
print(x)

y = ([1,2], 3)

del(y[0][1])
print(y)