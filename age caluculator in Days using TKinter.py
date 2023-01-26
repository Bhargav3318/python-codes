#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import*
import time
import datetime

def age(event):
    a = int(l_2.get())
    b = int(l_4.get())
    c = int(l_6.get())
    a_1 = int(time.strftime("%d"))
    a_2 = int(time.strftime("%m"))
    a_3 = int(time.strftime("%Y"))
    
    d = datetime.datetime(a_3,a_2,a_1)
    e = datetime.datetime(c,b,a)
    
    f = d-e
    
    l_7 = Label(r,text = "The age in days is :")
    l_7.grid(column =1 , row = 6)
    
    l_8 = Label(r,text = f)
    l_8.grid(column=2 , row = 6)
    
    
    
    
r = Tk()

l = Label(r,text = "Date Of Birth",font = "times 20 bold")
l.grid(column= 2,row = 1)
l_1 = Label(r,text="Day",font = "times 10 bold")
l_1.grid(column = 1, row = 2)
l_2 = Entry(r,width = 10)
l_2.grid(column= 2,row = 2)
l_3 = Label(r,text="Month",font = "times 10 bold")
l_3.grid(column = 1, row = 3)
l_4 = Entry(r,width = 10)
l_4.grid(column= 2,row = 3)
l_5 = Label(r,text="Year",font = "times 10 bold")
l_5.grid(column = 1, row = 4)
l_6 = Entry(r,width = 10)
l_6.grid(column= 2,row = 4)

bt = Button(r,text = "caluclate age",font="times 10 bold")
bt.bind("<Button-1>",age)
bt.grid(column= 2,row = 5)


r.mainloop()


# In[ ]:




