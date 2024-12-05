#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. Key Concepts of Object-Oriented Programming (OOP):
# Encapsulation: Wrapping data (attributes) and methods into a single unit (class).
# Abstraction: Hiding implementation details and exposing only necessary functionality.
# Inheritance: Enabling one class to inherit the properties and methods of another.
# Polymorphism: Allowing methods to have different implementations based on the object calling them.


# In[2]:


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"Car Information: {self.year} {self.make} {self.model}"

# below is the Example 
car = Car("Toyota", "Corolla", 2021)
print(car.display_info())


# In[3]:


# Instance Methods: Operate on instance variables of the object.
# Class Methods: Operate on the class itself and are denoted by @classmethod.


# In[4]:


# Python does not support traditional method overloading. Instead, it uses default arguments.

# Example:

class Example:
    def greet(self, name=None):
        if name:
            return f"Hello, {name}!"
        return "Hello!"

# Example usage
e = Example()
print(e.greet())
print(e.greet("Alice"))


# In[5]:


# 5. Access Modifiers in Python:
# Public: Accessible everywhere (default).
# Protected: Denoted with a single underscore _var and accessible within subclasses.
# Private: Denoted with double underscores __var and accessible only within the class.


# In[8]:


# Types of Inheritance in Python are as follows:
# Single Inheritance
# Multiple Inheritance
# Multilevel Inheritance
# Hierarchical Inheritance
# Hybrid Inheritance


class A:
    def method_a(self):
        return "Method from Class A"

class B:
    def method_b(self):
        return "Method from Class B"

class C(A, B):
    pass

# Example usage
c = C()
print(c.method_a())
print(c.method_b())


# In[9]:


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# In[10]:


def calculate_area(shape):
    print(f"The area is {shape.area()}")

circle = Circle(5)
rectangle = Rectangle(4, 6)

calculate_area(circle)
calculate_area(rectangle)


# In[11]:


class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance


# In[12]:


class CustomClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"CustomClass with value {self.value}"

    def __add__(self, other):
        return CustomClass(self.value + other.value)

# Example usage
obj1 = CustomClass(10)
obj2 = CustomClass(20)
print(obj1 + obj2)


# In[13]:


# Occurs in multiple inheritance when two parent classes share a common base class.


# In[14]:


class Example:
    count = 0

    def __init__(self):
        Example.count += 1

    @classmethod
    def get_instance_count(cls):
        return cls.count


# In[15]:


class Utils:
    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# In[ ]:




