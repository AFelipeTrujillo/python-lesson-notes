class MyClass:
    my_var_class = 'Class var'

    def __init__(self, instance_var):
        self.instance_var = instance_var

    @staticmethod
    def static_method():
        print(MyClass.my_var_class)

    @classmethod
    def method_class(cls):
        print(cls.my_var_class)

    def instance_method(self):
        self.method_class()
        self.static_method()
        print(self.instance_var)

MyClass.method_class()
myObj1 = MyClass('my var')
myObj1.method_class()
myObj1.instance_method()