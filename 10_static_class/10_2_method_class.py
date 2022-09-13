class MyClass:
    my_var_class = 'Class var'

    def __init__(self, instance_var):
        self.instance_var = instance_var

    @staticmethod
    def static_method():
        print(MyClass.my_var_class)

MyClass.static_method()