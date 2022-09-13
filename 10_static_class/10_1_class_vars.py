class MyClass:
    my_var_class = 'Class var'

    def __init__(self, instance_var):
        self.instance_var = instance_var


print(MyClass.my_var_class)
obj = MyClass('Other var')
print(obj.my_var_class, obj.instance_var)

MyClass.other_class_var = 'Class var two'

obj2 = MyClass('Other var 2')
print(obj2.other_class_var)
print(obj.other_class_var)

