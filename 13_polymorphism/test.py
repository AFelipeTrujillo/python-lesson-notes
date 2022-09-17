from Employer import Employer
from Manager import Manager

def print_details(obj):
    #print(obj)
    print(type(obj))
    print(obj.show())
    if isinstance(obj, Manager):
        print(obj.department)

e = Employer('Martha', 200000)
print_details(e)

m = Manager('Ann', 300000, 'IT')
print_details(m)