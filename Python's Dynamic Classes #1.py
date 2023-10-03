# Python's Dynamic Classes #1
# https://www.codewars.com/kata/pythons-dynamic-classes-number-1

#

def class_name_changer(cls, new_name):
    if new_name.istitle():
        ls.__name__ = new_name
    else: Exception

class MyClass:
    pass

class_name_changer(MyClass, "UsefulClass")
print(f'Now MyClass name is {MyClass.__name__}')




#if __name__ == 'main':

