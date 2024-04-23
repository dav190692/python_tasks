import re
class str_descriptor:

    def __set_name__(self, owner, property_name):
        self.property_name = '__' + property_name


    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.property_name, None)
        
    def __set__(self, instance, value):
        if not isinstance(value, str) or value == "":
            raise ValueError('value must be a string and not empty')
        setattr(instance, self.property_name, " ".join(value.split()))
    
    def __delete__(self, instance):
        delattr(instance, self.property_name)
        
class EmailValidateDscriptor:

    def __set_name__(self, owner, property_name):
        self.property_name = '__' + property_name

    def __get__ (self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.property_name, None)

    def __set__ (self, instance, value):
        if not isinstance(value, str):
            raise ValueError('Please type string')
        else:
            validate_result = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{3,}$', value)
            if not isinstance(value, str) or validate_result is None or value == "":
                raise ValueError('form cannot be empty or type corect email')
            setattr(instance, self.property_name, "".join(value.split()))


    def __delete__(self, instance):
        delattr(instance, self.property_name)        

class PasswordValidateDescriptor:
    def __set_name__(self, owner, property_name):
        self.property_name = '__' + property_name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.property_name, None)
    
    
    def __set__(self, instance, value):
        if isinstance(value, str):
            pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d!@#$%^&*()-=_+]{8,}$'
            if not re.match(pattern, value) or value == "":
                raise ValueError('Please type correct password')
            else:
                hashed_value = hash(value)
                setattr(instance, self.property_name, hashed_value)
  


    def __delete__(self, instance):
        delattr(instance, self.property_name)


class IntegerValueDecorator:
    def __set_name__(self, owner, property_name):
        self.property_name = '__' + property_name

    def __get__(self, instance, owner):
        return getattr(instance, self.property_name, None)
    
    def __set__(self, instance, value):
            if  not isinstance(value, int):
                raise ValueError('Age cannot be negative or type int value')
            if (self.property_name == '__age' and not 0 < int(value) < 120):
                raise ValueError('Age cannot be negative or type int value')
            setattr(instance, self.property_name, value)

    def __delete__(self, instance):
        delattr(instance, self.property_name)



class User:
    first_name = str_descriptor()
    last_name = str_descriptor()
    password = PasswordValidateDescriptor()
    email = EmailValidateDscriptor()
    age = IntegerValueDecorator()


    def __init__(self, first_name, last_name, password, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email
        self.age = age


ob = User('Davit', 'Kirakosyan', "Strong!Passwfefewfewvgewewgeword123", 'uuyyu@gmail.com', 24)

del ob.age
print(ob.__dict__)
print(ob.password)



