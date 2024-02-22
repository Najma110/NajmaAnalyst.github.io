from tkinter import* 
from database import insert_booking 

#Create window

window=Tk() 
window.geometry('1000x600') 
window.title('Cruise holidays') 
window.resizable(True, True)
#create colour for the window 
window.configure(bg="#336d92")

#create frame for the window
frame=Frame(window, relief= 'groove', height=20, width=1000, borderwidth=10) 
frame.pack()
frame.configure(bg="white") 
titleframe=Label(frame, text='         Welcome to Abbas Cruise         ', font=('Arial',20,'bold'))
titleframe.grid(  sticky='news', padx='10', pady='10',) 

systemFrame=Frame(window, relief= 'sunken',height=80, width=1000, borderwidth=20, pady=20)
systemFrame.pack()

#create option list 

choose_passangers=[1,2,3,4,5,6] 
optional_destinations=['Santorini','Amalfi Coast', 'Maldives', 'Bali', 'Meeru Island', 'Bora Bora'] 
choose_date_time=['23/06/23 2:30PM', '20/07/23 8:00AM','15/08/23 11:00AM', '22/09/23 10:00AM', '23/10/23 5:00pm','24/12/23 4:00PM'] 
alist= []

#create dictionary of booking
holiday_dict=dict() 
holiday_dict['Santorini']= 800 
holiday_dict['Amalfi Coast']= 1100 
holiday_dict['Maldives']= 900 
holiday_dict['Bali']= 1200 
holiday_dict['Meeru Island']= 1300 
holiday_dict['Bora Bora']= 2100 

#create the Variables
no_passangers=StringVar(window) 
itinerary=StringVar(window) 
date_time=StringVar(window) 

    
total=0
#create function 

def submit():
     
    global total
    global selected
    global choosed
    global choice
    
    selected=no_passangers.get()
    choosed=itinerary.get()
    choice=date_time.get()
    
    try:
        if itinerary.get()==optional_destinations[0]:
            noOfPassenger=int(no_passangers.get())
            total += holiday_dict['Santorini'] * noOfPassenger
            price=holiday_dict['Santorini']
            subtotal=price *noOfPassenger
            result= selected,choosed, choice, price, subtotal
            alist.append(result)
        
        if itinerary.get()==optional_destinations[1]:
           noOfPassenger=int(no_passangers.get())
           total += holiday_dict['Amalfi Coast'] * noOfPassenger
           price=holiday_dict['Amalfi Coast']
           subtotal=price * noOfPassenger
           result= selected, choosed, choice, price, subtotal
           alist.append(result)
        
        if itinerary.get()==optional_destinations[2]:
           noOfPassenger=int(no_passangers.get())
           total += holiday_dict['Maldives'] * noOfPassenger
           price=holiday_dict['Maldives']
           subtotal=price * noOfPassenger
           result= selected, choosed, choice, price, subtotal
           alist.append(result)
        
        if itinerary.get()==optional_destinations[3]:
           noOfPassenger=int(no_passangers.get())
           total += holiday_dict['Bali'] * noOfPassenger
           price=holiday_dict['Bali']
           subtotal=price * noOfPassenger
           result= selected, choosed, choice, price, subtotal
           alist.append(result)
        
        if itinerary.get()==optional_destinations[4]:
           noOfPassenger=int(no_passangers.get())
           total += holiday_dict['Meeru Island']* noOfPassenger
           price=holiday_dict['Meeru Island']
           subtotal=price * noOfPassenger
           result= selected, choosed,choice, price, subtotal
           alist.append(result)
        
        if itinerary.get()==optional_destinations[5]:
           noOfPassenger=int(no_passangers.get())
           total += holiday_dict['Bora Bora']* noOfPassenger
           price=holiday_dict['Bora Bora']
           subtotal=price * noOfPassenger
           result= selected, choosed, choice,  price, subtotal
           alist.append(result)

        else:
          if noOfPassenger >=4:
            discount=int(total-(0.2*total))
            print('Group charges after discount is £ ',discount)
            result=selected, choosed, choice, price, discount
            alist.append(result)

    except Exception:
        print("Must select the number of holiday makers and available dates")

    print("total price is £",total)
         

    for index in range(len(alist)):
         if noOfPassenger>=4:
            discount=int(total-(0.2*total))
            insert_booking(alist[index][0], alist[index][1], alist[index][2], alist[index][3], alist[index][4])
         else:
            insert_booking(alist[index][0], alist[index][1], alist[index][2], alist[index][3], alist[index][4])
            
def calculation():
    try:
        noOfPassenger=int(no_passangers.get())
        if noOfPassenger>=4:
            discount=int(total-(0.2*total))
            total_label=Label(systemFrame, text=(f'CONGRATULATIONS! YOU GET DISCOUNT \n GROUP CHARGES IS £ {discount}.'), font=('calibri',14,'bold'), fg='BROWN').grid(row=6, column=0, columnspan=2)
        else:
            total_label=Label(systemFrame, text=(f'TOTAL PRICE IS £{total}.'), font=('calibri',14,'bold'), fg='#000000').grid(row=6, column=0, columnspan=2)

    except Exception:
        total_label=Label(systemFrame, text=(f'TOTAL PRICE IS £{total}.'), font=('calibri',14,'bold'), fg='#000000').grid(row=6, column=0, columnspan=2)

         
          
#create combonents 

no_passangers.set("Select") 
itinerary.set("Select") 
date_time.set("Select")

#creating widget and place on grid
passangers=Label(systemFrame, text='Travellers',font=('Helvetica',12,'bold'), fg='#7f7fff') 
passangers.grid(row=1,column=0,sticky='w', padx='20') 
options=OptionMenu(systemFrame,no_passangers,*choose_passangers).grid(row=1,column=1, sticky='e', padx='20') 
destination=Label(systemFrame, text='Destination',font=('Helvetica',12,'bold'), fg='#7f7fff').grid(row=2, column=0, sticky='w', padx='20') 
option=OptionMenu(systemFrame,itinerary,*optional_destinations, ).grid(row=2, column=1, sticky='e', padx='20') 
dateTime=Label(systemFrame, text='Date & Time',font=('Helvetica',12,'bold'), fg='#7f7fff').grid(row=3, column=0, sticky='w', padx='20') 
select=OptionMenu(systemFrame,date_time,*choose_date_time,).grid(row=3,column=1, sticky='e', padx='20') 
submit_button=Button(systemFrame, text="Submit", command=submit, width=10).grid(row=4, column=1,sticky='e', padx='20')  
total_btn=Button(systemFrame, text="Show Total", command=calculation).grid(row=5, column=0, columnspan=2, padx='20',ipadx=137)
 



window.mainloop()

    

 
