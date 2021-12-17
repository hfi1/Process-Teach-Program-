import tkinter as tk #tkinter is the Graphical User Interface (GUI) that has all the functions we need to design the interface
from tkinter import Tk, mainloop, TOP #TK is just short hand to call tkinter functions, mainloop allows the program to run and end, TOP is used for the pages/classes and framing of GUI
import tkinter.messagebox #allows for the function tk.entry, tk.label to output messages
from tkinter import * #just allows us to call from more functions in tkinter if needed

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        root.title('Menu')
    def show(self):
        self.lift()
#class is like def function in python, but for larger amount of variables  
class Page1(Page): #page 1 is a class
   def __init__(self, *args, **kwargs): #self is the root (frame for page1) *args and **kwargs take arguments in a class or function and make them operable to variables 
       Page.__init__(self, *args, **kwargs)
       ild = tk.Label(self, text = "Please Enter ILD Result").place(x = 30,y = 50) #tk.Label is how you make txt boxes that appear on the interface
       shot_time= tk.Label(self, text = "Please Enter Shot Time").place(x = 30, y = 90)
       mix_ratio = tk.Label(self, text = "Please Enter Mix Ratio").place(x = 30, y = 130)
       hr3_label = tk.Label(self, text = "HR3 Program| Quality Spec (16.1-23.9N)| Nominal ILD is 20N", bg ='light green').place(x=270, y =20) #bg is background color

       #Entry for ILD
       e1 = tk.Entry(self, textvariable = vars) #tk.Entry is a function that allows users to input data and vars just makes the txt into integers 
       e1.place(x=160, y=50)#.place is how you position tk.Entry, tk.Label, or buttons
       #entry for shot time
       e2 = tk.Entry(self, textvariable = vars)
       e2.place(x=160, y=90)
       #entry for the mix ratio
       e3 = tk.Entry(self, textvariable =vars)
       e3.place(x=160, y=130)
       #ild entry
       def values(): 
           global ild
           ild_n= float((e1.get())) #float allows python to work with decimals, you cant use int function because that only works with whole numbers or base 10 integers 
           st_n=float((e2.get())) #the get.())) command allows us to grab the data from the tk.entry and use for calculations 
           mr = float(e3.get())
#if less than 8 increase shot by .15 and mix ratio by .3
           if ild_n<8:
               ns = st_n + .15
               nm = mr + .3
               if nm > .58:  
                   box2 = tk.Label(self, text= ("Caution Out Of Normal Mix Ratio Parameters! " +'{:.3f}'.format(nm)), bg='yellow')
               box1= tk.Label(self, text= ("Increase shot time and mix ratio to: "+'{:.3f}'.format(ns))+' and ''{:.3f}'.format(nm), bg='red')
               box1.place(x = 160, y = 150)
               def destroy():
                   box1.destroy()
                   box2.destroy()
               b2=tk.Button(self,text='Clear New Output', command=destroy, bg='blue')
               b2.place(x= 160, y =260) 
            

#if between 9 and 11.9  increase shot time by .03 and mix ratio by .024
           elif 9 <= ild_n <= 11.9:
               ns= st_n + .03
               nm = mr + .024
               #if new mix ratio is greater than .59 an alert is sent out
               if nm > .58:
                   box2 = tk.Label(self, text= ("Caution Out Of Normal Mix Ratio Parameters! " +'{:.3f}'.format(nm)), bg='yellow') 
                   box2.place(x=160, y= 180)

               box1= tk.Label(self, text= ("Increase shot time and mix ratio to: "+'{:.3f}'.format(ns))+' and ''{:.3f}'.format(nm), bg='red')
               box1.place(x = 160, y = 150)
               def destroy(): #def destory is used as a command for b2 below and that just deletes the new output data
                   box1.destroy()
                   box2.destroy()
               b2=tk.Button(self,text='Clear New Output', command=destroy, bg='blue')
               b2.place(x= 160, y =260)
#if between 12 and 13.9 increase shot time by .035 and mix ratio by .004
           elif 12 <= ild_n <=13.9 :
               ns1  = st_n + .025 #shot time
               nm1 = mr + .022
               if nm1 > .58:
                   box2 = tk.Label(self, text= ("Caution Out Of Normal Mix Ratio Parameters! " +'{:.3f}'.format(nm1)), bg='yellow') 
                   box2.place(x=160, y= 180)
               box1= tk.Label(self, text= ("Increase shot time and mix ratio to: "+'{:.3f}'.format(ns1))+' and ''{:.3f}'.format(nm1), bg='red')
               box1.place(x = 160, y = 170)
               def destroy():
                   box1.destroy()
               b2=tk.Button(self,text='Clear New Output', command=destroy, bg='yellow')
               b2.place(x= 160, y =200)
##if between  14 and 16.0 increase shot time by .02 and mix ratio by .0021
           elif 14.0<= ild_n <=16.0:
               ns2  = st_n + .02
               nm2 = mr + .015
               if nm2 > .58:
                   box2 = tk.Label(self, text= ("Caution Out Of Normal Mix Ratio Parameters! " +'{:.3f}'.format(nm2)), bg='yellow') 
                   box2.place(x=160, y= 280)
               box1= tk.Label(self, text= ("Increase shot time and mix ratio to: "+'{:.3f}'.format(ns2))+' and ''{:.3f}'.format(nm2), bg='red')
               box1.place(x = 160, y = 170)
               def destroy():
                   box1.destroy()
               b2=tk.Button(self,text='Clear New Output', command=destroy, bg='yellow')
               b2.place(x= 160, y =200)
#if between 16.1 and 19.9 increase shot by .01 and mix by .009
           elif 16.1<= ild_n <=19.9:
               ns2  = st_n + .02
               nm2 = mr + .012
               if nm2 > .58:
                   box2 = tk.Label(self, text= ("Caution Out Of Normal Mix Ratio Parameters! " +'{:.3f}'.format(nm2)), bg='yellow') 
                   box2.place(x=160, y= 180)
               box1= tk.Label(self, text= ("Tool in Spec, but not Nominal. Increase shot time and mix ratio to: "+'{:.3f}'.format(ns2))+' and ''{:.3f}'.format(nm2), bg='orange')
               box1.place(x = 160, y = 170)
               def destroy():
                   box1.destroy()
               b2=tk.Button(self,text='Clear New Output', command=destroy, bg='yellow')
               b2.place(x= 160, y =200)
               
#if between 21.0 and 23.9 decrease shot time .000 and decrease mix ratio by .008
           elif 21.0 <=ild_n <23.9:
                ns = st_n - .009
                nm = mr - .008
                if nm > .58:
                   box2 = tk.Label(self, text= ("Caution Out Of Normal Mix Ratio Parameters! " +'{:.3f}'.format(nm)), bg='yellow') 
                   box2.place(x=160, y= 180)
                box1= tk.Label(self, text= ("In Spec but not a nominal. Decrease shot time and mix ratio to: "+'{:.3f}'.format(ns))+' and ''{:.3f}'.format(nm), bg='orange')
                box1.place(x = 160, y = 170)
                def destroy():
                   box1.destroy()
                b2=tk.Button(self,text='Clear New Output', command=destroy, bg='yellow')
                b2.place(x= 160, y =200)
#if between 24.0 and 27.1  decreases shot by .015 and mix ratio by .015
           elif  24.0 <= ild_n <=25.1:
               ns3 = st_n - .015
               nm3 = mr - .015
               if nm3 > .58:
                   box2 = tk.Label(self, text= ("Caution Out Of Normal Mix Ratio Parameters! " +'{:.3f}'.format(nm3)), bg='yellow') 
                   box2.place(x=160, y= 180)
               box1= tk.Label(self, text= ("Decrease shot time and mix ratio to: "+'{:.3f}'.format(ns3))+' and ''{:.3f}'.format(nm3), bg='red')
               box1.place(x = 160, y = 170)
               def destroy():
                   box1.destroy()
               b2=tk.Button(self,text='Clear New Output', command=destroy, bg='yellow')
               b2.place(x= 160, y =200)
#if between 25.2 and 26.9 decrease shot by .02 and mix ratio by .02
           elif 25.2 <= ild_n <=26.9:
               ns4 = st_n - .02
               nm4 = mr - .02
               box1= tk.Label(self, text= ("Decrease shot time and mix ratio to: "+'{:.3f}'.format(ns4))+' and ''{:.3f}'.format(nm4), bg='red')
               box1.place(x = 160, y = 170)
               def destroy():
                   box1.destroy()
               b2=tk.Button(self,text='Clear New Output', command=destroy, bg='yellow')
               b2.place(x= 160, y =200)
#if between 27 and 31.9 decrease shot by .25 and mix ratio by .25
           elif 27<= ild_n <=31.9:
               ns5 = st_n - 0.25
               nm5 = mr - .25
               if nm5 > .58:
                   box2 = tk.Label(self, text= ("Caution Out Of Normal Mix Ratio Parameters! " +'{:.3f}'.format(nm5)), bg='yellow') 
                   box2.place(x=160, y= 180)
               box1 = tk.Label(self, text = ("Decrease shot time and mix ratio to: " +'{:.3f}'.format(ns5))+ ' and' '{:.3f}'.format(nm5), bg='red')
               box1.place(x = 160, y = 170)
               def destroy():
                   box1.destroy()
               b2=tk.Button(self,text='Clear New Output', command=destroy, bg='yellow')
               b2.place(x= 160, y =200)
#if between 32 and 36.9: decrease shot by .35 and mix ratio by .3
           elif 32 <= ild_n <=36.9:
               ns5 = st_n - 0.3
               nm5 = mr - .3
               if nm5 > .58:
                   box2 = tk.Label(self, text= ("Caution Out Of Normal Mix Ratio Parameters! " +'{:.3f}'.format(nm5)), bg='yellow') 
                   box2.place(x=160, y= 180)
               box1 = tk.Label(self, text = ("Decrease shot time and mix ratio to: " +'{:.3f}'.format(ns5))+ ' and' '{:.3f}'.format(nm5), bg='red')
               box1.place(x = 160, y = 170)
               def destroy():
                   box1.destroy()
               b2=tk.Button(self,text='Clear New Output', command=destroy, bg='yellow')
               b2.place(x= 160, y =200)
#if between 37 and 40: decrease shot by .4 and mix ratio by .3
           elif 37 <= ild_n <=40: 
               ns5 = st_n - 0.4
               nm5 = mr - .3
               if nm5 > .58:
                   box2 = tk.Label(self, text= ("Caution Out Of Normal Mix Ratio Parameters! " +'{:.3f}'.format(nm5)), bg='yellow') 
                   box2.place(x=160, y= 180)
               box1 = tk.Label(self, text = ("Decrease shot time and mix ratio to: " +'{:.3f}'.format(ns5))+ ' and' '{:.3f}'.format(nm5), bg='red')
               box1.place(x = 160, y = 170)
               def destroy():
                   box1.destroy()
               b2=tk.Button(self,text='Clear New Output', command=destroy, bg='yellow')
               b2.place(x= 160, y =200)
#if between 40 and 45: decrease shot by .45 and mix ratio by .35
           elif 40 <= ild_n <=45:
               ns5 = st_n - 0.45
               nm5 = mr - .35
               if nm5 > .58:
                   box2 = tk.Label(self, text= ("Caution Out Of Normal Mix Ratio Parameters! " +'{:.3f}'.format(nm5)), bg='yellow') 
                   box2.place(x=160, y= 180)
               box1 = tk.Label(self, text = ("Decrease shot time and mix ratio to: " +'{:.3f}'.format(ns5))+ ' and' '{:.3f}'.format(nm5), bg='red')
               box1.place(x = 160, y = 170)
               def destroy():
                   box1.destroy()
               b2=tk.Button(self,text='Clear New Output', command=destroy, bg='yellow')
               b2.place(x= 160, y =200)
#If between 45.1 and 50 decrease by .5 and mix ratio by .5
           elif 45.1 <= ild_n <=50:
               ns5 = st_n - 0.5
               nm5 = mr - .5
               box1 = tk.Label(self, text = ("Decrease shot time and mix ratio to: " +'{:.3f}'.format(ns5))+ ' and' '{:.3f}'.format(nm5), bg='red')
               box1.place(x = 160, y = 170)
               def destroy():
                   box1.destroy()
               b2=tk.Button(self,text='Clear New Output', command=destroy, bg='yellow')
               b2.place(x= 160, y =200)
#If greater than 50: decrease shot by .55 and mix ratio by .55
           elif ild_n >=50.1:
               ns5 = st_n - 0.55
               nm5 = mr - .55
               if nm5 > .58:
                   box2 = tk.Label(self, text= ("Caution Out Of Normal Mix Ratio Parameters! " +'{:.3f}'.format(nm5)), bg='yellow') 
                   box2.place(x=160, y= 180)
               box1 = tk.Label(self, text = ("Decrease shot time and mix ratio to: " +'{:.3f}'.format(ns5))+ ' and' '{:.3f}'.format(nm5), bg='red')
               box1.place(x = 160, y = 170)
               def destroy():
                   box1.destroy()
               b2=tk.Button(self,text='Clear New Output', command=destroy, bg='yellow')
               b2.place(x= 160, y =200)

#if none of the other conditions are met then the tool is in spec 
           else:
              box1 = tk.Label(self, text = ("Tool is in nominal : " +'{:.1f}'.format(ild_n)), bg='green')
              box1.place(x = 160, y = 170)
              def destroy():
                  box1.destroy()
              b2=tk.Button(self,text='Clear New Output', command=destroy, bg='yellow')
              b2.place(x= 160, y =200)
              
#calculate botton for new shot time and mix ratio
       button1 = tk.Button(self, text = 'Calculate New Shot Time', command = values, bg='orange').place(x=160 , y=220)





class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       ody_label = tk.Label(self, text = "ODY Program| Quality Spec (17N-21N| Nominal ILD is 19N", bg ='light green').place(x=270, y =20)
       ild = tk.Label(self, text = "Please Enter ILD Result").place(x = 30,y = 50)
       shot_time= tk.Label(self, text = "Please Enter Shot Time").place(x = 30, y = 90)
       mix_ratio = tk.Label(self, text = "Please Enter Mix Ratio").place(x = 30, y = 130)

       #Entry for ILD
       e1 = tk.Entry(self, textvariable = vars)
       e1.place(x=160, y=50)
       #entry for shot time
       e2 = tk.Entry(self, textvariable = vars)
       e2.place(x=160, y=90)
       #entry for the mix ratio
       e3 = tk.Entry(self, textvariable =vars)
       e3.place(x=160, y=130)
       #ild entry
       def values():
           global ild
           ild_n= float((e1.get()))
           st_n=float((e2.get()))
           mr = float(e3.get())
#if less than or equal to 8.9 increase shot time by .2 and mix by.25
           if ild_n <= 8.9:
               ns = st_n + .2
               nm = mr + .25
               if nm > .58:
                   box3 = tk.Label(self, text = ('Caution out of normal mix ratio parameters!' + '{:.3f}'.format(nm)), bg='yellow')
                   box3.place(x=160, y = 180)
               box1= tk.Label(self, text= ("Increase shot time and mix ratio to: "+'{:.3f}'.format(ns))+' and ''{:.3f}'.format(nm), bg='red')
               box1.place(x = 160, y = 150)
               def destroy():
                   box1.destroy()
                   box3.destroy()
               b2=tk.Button(self,text='Clear New Output', command=destroy, bg='blue')
               b2.place(x= 160, y =260)
#If  between 9 and 13 increase shot time by .15 and mix by .2
           elif 9 <= ild_n <=13.0:
               ns= st_n + 0.070
               nm = mr + .08
               if nm > .58:
                   box2 = tk.Label(self, text= ("Caution Out Of Normal Mix Ratio Parameters! " +'{:.3f}'.format(nm)), bg='yellow')
                   box2.place(x=160, y= 180)

               box1= tk.Label(self, text= ("Increase shot time and mix ratio to: "+'{:.3f}'.format(ns))+' and ''{:.3f}'.format(nm), bg='red')
               box1.place(x = 160, y = 150)
               def destroy():
                   box1.destroy()
                   box2.destroy()
               b2=tk.Button(self,text='Clear New Output', command=destroy, bg='blue')
               b2.place(x= 160, y =260)

#If between 13.1 and 16.0 increase shot by .2 and mix ratio by .8
           elif 13.1 <= ild_n <=16:
               ns = st_n + .045
               nm = mr + .08
               if nm >.58:
                   box2 = tk.Label(self, text = ("Caution out of normal mix ratio parameters!" +'{:.3f}'.format(nm)),bg='yellow')
                   box2.place(x=160, y=180)
                             
               box1= tk.Label(self, text= ("Increase shot time and mix ratio to: "+'{:.3f}'.format(ns))+' and ''{:.3f}'.format(nm), bg='red')
               box1.place(x = 160, y = 150)
               def destroy():
                   box1.destroy()
                   box2.destroy()
               b2=tk.Button(self,text='Clear New Output', command=destroy, bg='blue')
               b2.place(x= 160, y =260)

#If betweeen 16.1 and 16.9 increase shot by .15 and mix ratio by .15
           elif 16.1 <= ild_n <=16.9:
               ns = st_n + .015
               nm = mr + .1
               if nm >.58:
                   box2 = tk.Label(self, text = ("Caution out of normal mix ratio parameters!" +'{:.3f}'.format(nm)),bg='yellow')
                   box2.place(x=160, y=180)
                             
               box1= tk.Label(self, text= ("Increase shot time and mix ratio to: "+'{:.3f}'.format(ns))+' and ''{:.3f}'.format(nm), bg='red')
               box1.place(x = 160, y = 150)
               def destroy():
                   box1.destroy()
                   box2.destroy()
               b2=tk.Button(self,text='Clear New Output', command=destroy, bg='blue')
               b2.place(x= 160, y =260)
#if 17 and 18.9 increase shot time by .1 and mix ratio by .1
           elif 17 <= ild_n <=18.9:
               ns = st_n + .015
               nm = mr + .1
               if nm >.58:
                   box2 = tk.Label(self, text = ("Caution out of normal mix ratio parameters!" +'{:.3f}'.format(nm)),bg='yellow')
                   box2.place(x=160, y=180)
                             
               box1= tk.Label(self, text= ("Tool in spec, but not Nominal. Increase shot time and mix ratio to: "+'{:.3f}'.format(ns))+' and ''{:.3f}'.format(nm), bg='orange')
               box1.place(x = 160, y = 150)
               def destroy():
                   box1.destroy()
                   box2.destroy()
               b2=tk.Button(self,text='Clear New Output', command=destroy, bg='blue')
               b2.place(x= 160, y =260)
#if between 20 and 21.1 decrease shot time by .1 and mix ratio by .1
           elif 20 <= ild_n <=21.1:
               ns = st_n - .015
               nm = mr - .1
               if nm >.58:
                   box2 = tk.Label(self, text = ("Caution out of normal mix ratio parameters!" +'{:.3f}'.format(nm)),bg='yellow')
                   box2.place(x=160, y=180)
                             
               box1= tk.Label(self, text= ("Tool in spec, but not Nominal. Decrease shot time and mix ratio to: "+'{:.3f}'.format(ns))+' and ''{:.3f}'.format(nm), bg='orange')
               box1.place(x = 160, y = 150)
               def destroy():
                   box1.destroy()
                   box2.destroy()
               b2=tk.Button(self,text='Clear New Output', command=destroy, bg='blue')
               b2.place(x= 160, y =260)

#if between 21.2 and 24.9 decrease shot time by .2 and mix ratio by .15
           elif 21.2 <= ild_n <=24.9:
               ns = st_n  - .035
               nm = mr - .1
               if nm >.58:
                   box2 = tk.Label(self, text = ("Caution out of normal mix ratio parameters!" +'{:.3f}'.format(nm)),bg='yellow')
                   box2.place(x=160, y=180)
                             
               box1= tk.Label(self, text= ("Decrease shot time and mix ratio to: "+'{:.3f}'.format(ns))+' and ''{:.3f}'.format(nm), bg='red')
               box1.place(x = 160, y = 150)
               def destroy():
                   box1.destroy()
                   box2.destroy()
               b2=tk.Button(self,text='Clear New Output', command=destroy, bg='blue')
               b2.place(x= 160, y =260)

#if between 25 and 28.9 decrease shot time by .3 and mix ratio by .25 
           elif  25 <= ild_n <=28.9:
               ns = st_n - .04
               nm = mr - .2 
               if nm >.58:
                   box2 = tk.Label(self, text = ("Caution out of normal mix ratio parameters!" +'{:.3f}'.format(nm)),bg='yellow')
                   box2.place(x=160, y=180)
                             
               box1= tk.Label(self, text= ("Decrease shot time and mix ratio to: "+'{:.3f}'.format(ns))+' and ''{:.3f}'.format(nm), bg='red')
               box1.place(x = 160, y = 150)
               def destroy():
                   box1.destroy()
                   box2.destroy()
               b2=tk.Button(self,text='Clear New Output', command=destroy, bg='blue')
               b2.place(x= 160, y =260)

#if  between 29.0 and 32.9 decrease shot time by .053 and mix ratio by .27
           elif  29 <= ild_n <=32.9:
               ns = st_n - .053
               nm = mr - .22
               if nm >.58:
                   box2 = tk.Label(self, text = ("Caution out of normal mix ratio parameters!" +'{:.3f}'.format(nm)),bg='yellow')
                   box2.place(x=160, y=180)
                             
               box1= tk.Label(self, text= ("Decrease shot time and mix ratio to: "+'{:.3f}'.format(ns))+' and ''{:.3f}'.format(nm), bg='red')
               box1.place(x = 160, y = 150)
               def destroy():
                   box1.destroy()
                   box2.destroy()
               b2=tk.Button(self,text='Clear New Output', command=destroy, bg='blue')
               b2.place(x= 160, y =260)
#if between 33 and 37 decrease shot time by .075 and mix ratio by .289
           elif  33 <= ild_n <=37.9:
               ns = st_n - .075
               nm = mr - .23
               if nm >.58:
                   box2 = tk.Label(self, text = ("Caution out of normal mix ratio parameters!" +'{:.3f}'.format(nm)),bg='yellow')
                   box2.place(x=160, y=180)
                             
               box1= tk.Label(self, text= ("Decrease shot time and mix ratio to: "+'{:.3f}'.format(ns))+' and ''{:.3f}'.format(nm), bg='red')
               box1.place(x = 160, y = 150)
               def destroy():
                   box1.destroy()
                   box2.destroy()
               b2=tk.Button(self,text='Clear New Output', command=destroy, bg='blue')
               b2.place(x= 160, y =260)
#if greater than  38 decrease shot time by .09 and mix ratio by .3
           elif  ild_n >=38:
               ns = st_n - .09
               nm = mr - .25
               if nm >.58:
                   box2 = tk.Label(self, text = ("Caution out of normal mix ratio parameters!" +'{:.3f}'.format(nm)),bg='yellow')
                   box2.place(x=160, y=180)
                             
               box1= tk.Label(self, text= ("Decrease shot time and mix ratio to: "+'{:.3f}'.format(ns))+' and ''{:.3f}'.format(nm), bg='red')
               box1.place(x = 160, y = 150)
               def destroy():
                   box1.destroy()
                   box2.destroy()
               b2=tk.Button(self,text='Clear New Output', command=destroy, bg='blue')
               b2.place(x= 160, y =260)
# tool in spec
           else:              
               box1= tk.Label(self, text= ("Tool is in nominal. "+'{:.1f}'.format(ild_n)), bg='green')
               box1.place(x = 160, y = 150)
               def destroy():
                   box1.destroy()
               b2=tk.Button(self,text='Clear New Output', command=destroy, bg='blue')
               b2.place(x= 160, y =260)
#calculate botton for new shot time and mix ratio
       button1 = tk.Button(self, text = 'Calculate New Shot Time', command = values, bg='orange').place(x=160 , y=220)

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       rdx_label = tk.Label(self, text = "RDX Program| Quality Spec (11N-15N| Nominal ILD is 13N", bg ='light green').place(x=270, y =20)
       ild = tk.Label(self, text = "Please Enter ILD Result").place(x = 30,y = 50)
       shot_time= tk.Label(self, text = "Please Enter Shot Time").place(x = 30, y = 90)
       mix_ratio = tk.Label(self, text = "Please Enter Mix Ratio").place(x = 30, y = 130)

       #Entry for ILD
       e1 = tk.Entry(self, textvariable = vars)
       e1.place(x=160, y=50)
       #entry for shot time
       e2 = tk.Entry(self, textvariable = vars)
       e2.place(x=160, y=90)
       #entry for the mix ratio
       e3 = tk.Entry(self, textvariable =vars)
       e3.place(x=160, y=130)
       #ild entry
       def values():
           global ild
           ild_n= float((e1.get()))
           st_n=float((e2.get()))
           mr = float(e3.get())
           #if less than 8 increase shot by .15 and mix ratio by .3
           if ild_n<8:
               df= abs(13-ild_n) #nominal placement - ild entered  = differnce from ild
               n_df = (df) #makes workable
               ns = n_df*(.011)+ (st_n) #diffrence from ild times .011 plus inputed shot time 
               nm = n_df*(.006) + mr #ild differnce times .006 plus inputed mix ratio 
               if nm > .58:  
                   box2 = tk.Label(self, text= ("Caution Out Of Normal Mix Ratio Parameters! " +'{:.3f}'.format(nm)), bg='yellow')
               box1= tk.Label(self, text= ("Increase shot time and mix ratio to: "+'{:.3f}'.format(ns))+' and ''{:.3f}'.format(nm), bg='red')
               box1.place(x = 160, y = 150)
               def destroy():
                   box1.destroy()
                   box2.destroy()
               b2=tk.Button(self,text='Clear New Output', command=destroy, bg='blue')
               b2.place(x= 160, y =260) 
            

#if between 9 and 10.9  increase shot time by .03 and mix ratio by .024
           elif 9 <= ild_n <= 10.9:
               df = abs(13-ild_n)
               n_df = (df)
               ns= n_df*(.00271828) + (st_n)
               nm = n_df*(.006) + mr
               #if new mix ratio is greater than .59 an alert is sent out
               if nm > .58:
                   box2 = tk.Label(self, text= ("Caution Out Of Normal Mix Ratio Parameters! " +'{:.3f}'.format(nm)), bg='yellow') 
                   box2.place(x=160, y= 180)

               box1= tk.Label(self, text= ("Increase shot time and mix ratio to: "+'{:.3f}'.format(ns))+' and ''{:.3f}'.format(nm), bg='red')
               box1.place(x = 160, y = 150)
               def destroy(): #def destory is used as a command for b2 below and that just deletes the new output data
                   box1.destroy()
                   box2.destroy()
               b2=tk.Button(self,text='Clear New Output', command=destroy, bg='blue')
               b2.place(x= 160, y =260)

#if between 11 and 12.9 increase shot time not mix ratio 
           elif 11 <= ild_n <= 12.9:
               df = abs(13-ild_n)
               n_df = (df)
               ns = n_df *(.00271828) + (st_n)
               nm = n_df*(0) + mr 
               if nm > .58:
                   box2 = tk.Label(self, text= ("Caution Out Of Normal Mix Ratio Parameters! " +'{:.3f}'.format(nm)), bg='yellow') 
                   box2.place(x=160, y= 180)

               box1= tk.Label(self, text= ("Tool in spec, but NOT Nominal. Increase shot time: "+'{:.3f}'.format(ns)), bg='red')
               box1.place(x = 160, y = 150)
               def destroy(): #def destory is used as a command for b2 below and that just deletes the new output data
                   box1.destroy()
                   box2.destroy()
               b2=tk.Button(self,text='Clear New Output', command=destroy, bg='blue')
               b2.place(x= 160, y =260)
#id between 14 and 15 decrease shot time 
           elif 14 <= ild_n <= 15.9:
               df = abs(13-ild_n)
               n_df = (df)
               ns = (st_n) - n_df*(.00271828)
               nm = n_df*(0) + mr 
               if nm > .58:
                   box2 = tk.Label(self, text= ("Caution Out Of Normal Mix Ratio Parameters! " +'{:.3f}'.format(nm)), bg='yellow') 
                   box2.place(x=160, y= 180)

               box1= tk.Label(self, text= ("Tool in spec, but NOT Nominal. Decrease shot time: "+'{:.3f}'.format(ns)), bg='red')
               box1.place(x = 160, y = 150)
               def destroy(): #def destory is used as a command for b2 below and that just deletes the new output data
                   box1.destroy()
                   box2.destroy()
               b2=tk.Button(self,text='Clear New Output', command=destroy, bg='blue')
               b2.place(x= 160, y =260)
#if between 16 and 17.9 decrease shot time and mix ratio
           elif 16<= ild_n <=17.9:
               df = abs(13-ild_n)
               n_df = (df)
               ns = (st_n) - n_df*(.00271828)
               nm = mr- n_df*(.00271828) 
               if nm > .58:
                   box2 = tk.Label(self, text= ("Caution Out Of Normal Mix Ratio Parameters! " +'{:.3f}'.format(nm)), bg='yellow') 
                   box2.place(x=160, y= 180)

               box1= tk.Label(self, text= ("Decrease shot time and mix ratio: "+'{:.3f}'.format(ns) +' and ' '{:.3f}'.format(nm)), bg = 'red')
               box1.place(x = 160, y = 150)
               def destroy():
                       box1.destroy()
                       box2.destroy()
                       values.destroy()
    
               button2 = tk.Button(self, text = 'Clear All', command = destroy, bg ='blue').place(x=160, y =260)
#if between 18 and 20 decrease shot time and mix ratio
           elif 18<= ild_n <=20.0:
               df = abs(13-ild_n)
               n_df = (df)
               ns = (st_n) - n_df*(.00271828)
               nm = mr- n_df*(.00271728) 
               if nm > .58:
                   box2 = tk.Label(self, text= ("Caution Out Of Normal Mix Ratio Parameters! " +'{:.3f}'.format(nm)), bg='yellow') 
                   box2.place(x=160, y= 180)

               box1= tk.Label(self, text= ("Decrease shot time and mix ratio: "+'{:.3f}'.format(ns) +' and' '{:.3f}'.format(nm)), bg = 'red')
               box1.place(x = 160, y = 150)
               def destroy():
                       box1.destroy()
                       box2.destroy()
                       values.destroy()
               button2 = tk.Button(self, text = 'Clear All', command = destroy, bg ='blue').place(x=160, y =260)

#if between 20.1 and 23.0: decrease shot time
           elif 20.1 <= ild_n <=23.0:
               df = abs(13-ild_n)
               n_df = (df)
               ns = (st_n) - n_df*(.005)
               nm = mr- n_df*(.004) 
               if nm > .58:
                   box2 = tk.Label(self, text= ("Caution Out Of Normal Mix Ratio Parameters! " +'{:.3f}'.format(nm)), bg='yellow') 
                   box2.place(x=160, y= 180)
               box1= tk.Label(self, text= ("Decrease shot time and mix ratio: "+'{:.3f}'.format(ns) +' and' '{:.3f}'.format(nm)), bg = 'red')
               box1.place(x = 160, y = 150)
               def destroy():
                       box1.destroy()
                       box2.destroy()
                       values.destroy()
               button2 = tk.Button(self, text = 'Clear All', command = destroy, bg ='blue').place(x=160, y =260)
#if between 23.1 and 25.0 decrease
           elif 23.1 <= ild_n <=25.0:
               df = abs(13-ild_n)
               n_df = (df)
               ns = (st_n) - n_df*(.005)
               nm = mr- n_df*(.004) 
               if nm > .58:
                   box2 = tk.Label(self, text= ("Caution Out Of Normal Mix Ratio Parameters! " +'{:.3f}'.format(nm)), bg='yellow') 
                   box2.place(x=160, y= 180)

               box1= tk.Label(self, text= ("Decrease shot time and mix ratio: "+'{:.3f}'.format(ns) +' and' '{:.3f}'.format(nm)), bg = 'red')
               box1.place(x = 160, y = 150)
               def destroy():
                       box1.destroy()
                       box2.destroy()
                       values.destroy()
               button2 = tk.Button(self, text = 'Clear All', command = destroy, bg ='blue').place(x=160, y =260)
#if >= 26 decrease shot time:
           elif  ild_n >=26:
               df = abs(13-ild_n)
               n_df = (df)
               ns = (st_n) - n_df*(.007)
               nm = mr -n_df*(.006)
               if nm > .58:
                   box2 = tk.Label(self, text= ("Caution Out Of Normal Mix Ratio Parameters! " + '{:.3f}'.format(nm)), bg='yellow') 
                   box2.place(x=160, y= 180)

               box1= tk.Label(self, text= ("Decrease shot time and mix ratio: "+'{:.3f}'.format(ns) + ' and' '{:.3f}'.format(nm)), bg = 'red')
               box1.place(x = 160, y = 150)
               def destroy():
                       box1.destroy()
                       box2.destroy()
                       values.destroy()
               button2 = tk.Button(self, text = 'Clear All', command = destroy, bg ='blue').place(x=160, y =260)
# if tool is nominal           
           else:
               box1= tk.Label(self, text= ("Keep parameters, tool in NOMINAL.: "+'{:.3f}'.format(ild_n)), bg = 'red')
               box1.place(x = 160, y = 150)
               def destroy():
                   box1.destroy()
                   box2.destroy()
                   values.destroy()
               button2 = tk.Button(self, text = 'Clear All', command = destroy, bg ='blue').place(x=160, y =260)
               


               
#calculate botton for new shot time and mix ratio
       button1 = tk.Button(self, text = 'Calculate New Shot Time', command = values, bg='orange').place(x=160 , y=220)
class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self, bg='light blue')
        p2 = Page2(self, bg='light blue')
        p3 = Page3(self, bg ='light blue')

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="HR3 Program", command=p1.show)
        b2 = tk.Button(buttonframe, text="ODY", command=p2.show)
        b3 = tk.Button(buttonframe, text="RDX", command=p3.show)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("600x450")
    root.mainloop()
