#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Employeee class
class EMP:
    def __init__(self,id_no,name,sal):
        self.id_no = id_no
        self.name = name
        self.sal = sal
        
        
    def payslip(self):
        self.hra = (self.sal *(18/100))
        
        self.da = (self.sal * (10/100))
        
        self.tax =(self.sal * (3/100))
        
        self.gross_sal = self.sal + self.hra + self.da
        
        self.net_sal = ((self.gross_sal) - ((10/100)*self.gross_sal))
        
        print("\n\nEMP ID :",self.id_no)
        print("\nEMP NAME :",self.name)
        print("\nEMP BASIC :",self.sal)
        print("\nEMP HRA :",self.hra)
        print("\nEMP DA :",self.da)
        print("\nEMP TAX :",self.tax)
        print("\nEMP GROSS SAL :",self.gross_sal)
        print("\nEMP NET SAL :",self.net_sal)
        
        
        
a = []
b = []
c = []
n = int(input("number of employees :"))
for i in range(0,n):
    print("\nEnter the details of employee ",i+1)
    p = input("Name :")
    b.append(p)
    
    q = int(input("ID number :"))
    a.append(q)
    
    r = int((input("salary :")))
    c.append(r)
    
m = int(input("\n\nWHich employee pay slip do you want :"))


EMP_object = EMP(a[m-1],b[m-1],c[m-1])
EMP_object.payslip()



# In[9]:


#18th sum

import math
class polygon:
    
    class triangle:
        def __init__(self,s_1,s_2,s_3):
            self.s_1 = s_1
            self.s_2 = s_2
            self.s_3 = s_3
            
        def area_triangle(self):
            self.s =  self.s_1 + self.s_2 + self.s_3
            self.area_t = math.sqrt((self.s-self.s_1)*(self.s-self.s_2)*(self.s-self.s_3))
            print("Area of triangle is ",self.area_t)
            
    class Rectangle:
        def __init__(self,s_1,s_2):
            self.s_1 = s_1
            self.s_2 = s_2
            
        def area_Rectangle(self):
            self.area_r = self.s_1 * self.s_2
            print("Area of rectangle is ",self.area_r)
            
    class Square:
        def __init__(self,s_1):
            self.s_1 = s_1
            
        def area_Square(self):
            
            self.area_s = self.s_1*self.s_1
            print("Area of square is ",self.area_s)
            
a = []
b = []

print("Enter three sides of triangle :")
for i in range (0,3):
    n = int(input())
    a.append(n)
    
    
print("Enter two sides of rectangle :")
for i in range (0,2):
    n = int(input())
    b.append(n)

c = int(input("enter a side of a square :")) 

p =  polygon()

t = polygon().triangle(a[0],a[1],a[2])
t.area_triangle()

r = polygon().Rectangle(b[0],b[1])
r.area_Rectangle()

s = polygon().Square(c)
s.area_Square()




# In[16]:


class Car:

    def __init__(self, model,speed,price):
        self.model= model
        self.speed = speed
        self.price = price


class firingCar(Car):

    def __init__(self, model,speed, price):
        super().__init__( model,speed, price)
        def fire(self,no_of_bullets):
            return self.no_of_bullets

C1=firingCar("Ford",220,400000)

C1.__str__()
C1.no_of_bullets = 10
print(f"{C1.model} has {C1.no_of_bullets} firing bullets and it has {C1.speed} speed which costs {C1.price}.")


# In[ ]:





# In[ ]:




