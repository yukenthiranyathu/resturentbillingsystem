from tkinter import *
import random
import tkinter
from tkinter import messagebox

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg='orange')
        self.root.title('Resturent Billing System')
        
        title=Label(self.root,text='RESTURENT BILLING SYSTEM',font=('Arial',20,'bold'),bg='white',fg='orange',bd=10,relief=RIDGE,padx=5,pady=5).pack(fill=X)
        
        #--------------------------variables---------------------------------------------#
        self.billno=StringVar()
        self.customername=StringVar()
        self.customerno=StringVar()
        x=random.randint(1000,9999)
        self.billno.set(str(x))
        self.cutlet=IntVar()
        self.samoza=IntVar()
        self.vada=IntVar()
        self.rolls=IntVar()
        self.vegsoup=IntVar()
        self.chickensoup=IntVar()
        self.fruitsalad=IntVar()
        self.chips=IntVar()
        self.total_starter=IntVar()
        self.total_biriyani=IntVar()
        self.total_drinks=IntVar()
        self.a=StringVar()
        self.b=StringVar()
        self.c=StringVar()
        self.cbiri=IntVar()
        self.fbiri=IntVar()
        self.vbiri=IntVar()
        self.bbiri=IntVar()
        self.kuska=IntVar()
        self.dbiri=IntVar()
        self.rice=IntVar()
        self.ebiri=IntVar()
        self.soda=IntVar()
        self.milk=IntVar()
        self.juice=IntVar()
        self.tea=IntVar()
        self.coffie=IntVar()
        self.water=IntVar()
        self.icecream=IntVar()
        self.faluda=IntVar()
        
        #--------------------------customer details panel--------------------------------#
        customer_panel=LabelFrame(self.root,text="Customer Details",font=("Arial Black",10),bg='white',fg='orange',bd=5,relief=GROOVE)
        customer_panel.place(x=0,y=70,relwidth=1)
        customer_name=Label(customer_panel,text='Customer Name : ',font=('Arial Black',11),fg='orange').grid(row=0,column=0,padx=15)
        customer_entery=Entry(customer_panel,borderwidth=4,width=30,textvariable=self.customername).grid(row=0,column=1,padx=8,pady=8)
        
        customer_number=Label(customer_panel,text='Contact No : ',font=('Arial Black',11),fg='orange').grid(row=0,column=2,padx=15)
        number_entery=Entry(customer_panel,borderwidth=4,width=30,textvariable=self.customerno).grid(row=0,column=3,padx=8,pady=8)
        
        customer_bill=Label(customer_panel,text='Bill No : ',font=('Arial Black',11),fg='orange').grid(row=0,column=4,padx=15)
        bill_entery=Entry(customer_panel,borderwidth=4,width=30,textvariable=self.billno).grid(row=0,column=5,padx=8,pady=8)
        
        #--------------------------------Starter Menu----------------------------------#
        starter_menu=LabelFrame(self.root,text='Starter Items',font=('Arial Black',10),bd=5,fg='orange',relief=GROOVE)
        starter_menu.place(x=5,y=145,width=310)
        
        sitem1=Label(starter_menu,text='Samoza',font=('Arial',12,'bold'),fg='orange').grid(row=0,column=0,padx=15)
        sitem1_entery=Entry(starter_menu,borderwidth=4,width=20,textvariable=self.samoza).grid(row=0,column=1,padx=8,pady=8)
        
        sitem2=Label(starter_menu,text='Cutlet',font=('Arial',12,'bold'),fg='orange').grid(row=1,column=0,padx=15)
        sitem2_entery=Entry(starter_menu,borderwidth=4,width=20,textvariable=self.cutlet).grid(row=1,column=1,padx=8,pady=8)
        
        sitem3=Label(starter_menu,text='Rolls',font=('Arial',12,'bold'),fg='orange').grid(row=2,column=0,padx=15)
        sitem3_entery=Entry(starter_menu,borderwidth=4,width=20,textvariable=self.rolls).grid(row=2,column=1,padx=8,pady=8)
        
        sitem4=Label(starter_menu,text='Chips',font=('Arial',12,'bold'),fg='orange').grid(row=3,column=0,padx=15)
        sitem4_entery=Entry(starter_menu,borderwidth=4,width=20,textvariable=self.chips).grid(row=3,column=1,padx=8,pady=8)
        
        sitem5=Label(starter_menu,text='Vada',font=('Arial',12,'bold'),fg='orange').grid(row=4,column=0,padx=15)
        sitem5_entery=Entry(starter_menu,borderwidth=4,width=20,textvariable=self.vada).grid(row=4,column=1,padx=8,pady=8)
        
        sitem6=Label(starter_menu,text='Vegitable Soup',font=('Arial',12,'bold'),fg='orange').grid(row=5,column=0,padx=15)
        sitem6_entery=Entry(starter_menu,borderwidth=4,width=20,textvariable=self.vegsoup).grid(row=5,column=1,padx=8,pady=8)
        
        sitem7=Label(starter_menu,text='Chicken Soup',font=('Arial',12,'bold'),fg='orange').grid(row=6,column=0,padx=15)
        sitem7_entery=Entry(starter_menu,borderwidth=4,width=20,textvariable=self.chickensoup).grid(row=6,column=1,padx=8,pady=8)
        
        sitem8=Label(starter_menu,text='Fruit Salad',font=('Arial',12,'bold'),fg='orange').grid(row=7,column=0,padx=15)
        sitem8_entery=Entry(starter_menu,borderwidth=4,width=20,textvariable=self.fruitsalad).grid(row=7,column=1,padx=8,pady=8)
        
         #--------------------------------Biriyani Menu----------------------------------#
        biriyani_menu=LabelFrame(self.root,text='Biriyani Items',font=('Arial Black',10),bd=5,fg='orange',relief=GROOVE)
        biriyani_menu.place(x=320,y=145,width=310)
        
        bitem1=Label(biriyani_menu,text='chicken biriyani',font=('Arial',12,'bold'),fg='orange').grid(row=0,column=0,padx=15)
        bitem1_entery=Entry(biriyani_menu,borderwidth=4,width=20,textvariable=self.cbiri).grid(row=0,column=1,padx=8,pady=8)
        
        bitem2=Label(biriyani_menu,text='veg biriyani',font=('Arial',12,'bold'),fg='orange').grid(row=1,column=0,padx=15)
        bitem2_entery=Entry(biriyani_menu,borderwidth=4,width=20,textvariable=self.vbiri).grid(row=1,column=1,padx=8,pady=8)
        
        bitem3=Label(biriyani_menu,text='fish biriyani',font=('Arial',12,'bold'),fg='orange').grid(row=2,column=0,padx=15)
        bitem3_entery=Entry(biriyani_menu,borderwidth=4,width=20,textvariable=self.fbiri).grid(row=2,column=1,padx=8,pady=8)
        
        bitem4=Label(biriyani_menu,text='bomboo biriyani',font=('Arial',12,'bold'),fg='orange').grid(row=3,column=0,padx=15)
        bitem4_entery=Entry(biriyani_menu,borderwidth=4,width=20,textvariable=self.bbiri).grid(row=3,column=1,padx=8,pady=8)
        
        bitem5=Label(biriyani_menu,text='dham biriyani',font=('Arial',12,'bold'),fg='orange').grid(row=4,column=0,padx=15)
        bitem5_entery=Entry(biriyani_menu,borderwidth=4,width=20,textvariable=self.dbiri).grid(row=4,column=1,padx=8,pady=8)
        
        bitem6=Label(biriyani_menu,text='egg biriyani',font=('Arial',12,'bold'),fg='orange').grid(row=5,column=0,padx=15)
        bitem6_entery=Entry(biriyani_menu,borderwidth=4,width=20,textvariable=self.ebiri).grid(row=5,column=1,padx=8,pady=8)
        
        bitem7=Label(biriyani_menu,text='kuska',font=('Arial',12,'bold'),fg='orange').grid(row=6,column=0,padx=15)
        bitem7_entery=Entry(biriyani_menu,borderwidth=4,width=20,textvariable=self.kuska).grid(row=6,column=1,padx=8,pady=8)
        
        bitem8=Label(biriyani_menu,text='rice & curry',font=('Arial',12,'bold'),fg='orange').grid(row=7,column=0,padx=15)
        bitem8_entery=Entry(biriyani_menu,borderwidth=4,width=20,textvariable=self.rice).grid(row=7,column=1,padx=8,pady=8)
        
         #--------------------------------Drinks Menu----------------------------------#
        drinks_menu=LabelFrame(self.root,text='Drinks Items',font=('Arial Black',10),bd=5,fg='orange',relief=GROOVE)
        drinks_menu.place(x=635,y=145,width=310)
        
        ditem1=Label(drinks_menu,text='soda',font=('Arial',12,'bold'),fg='orange').grid(row=0,column=0,padx=15)
        ditem1_entery=Entry(drinks_menu,borderwidth=4,width=20,textvariable=self.soda).grid(row=0,column=1,padx=8,pady=8)
        
        ditem2=Label(drinks_menu,text='faluda',font=('Arial',12,'bold'),fg='orange').grid(row=1,column=0,padx=15)
        ditem2_entery=Entry(drinks_menu,borderwidth=4,width=20,textvariable=self.faluda).grid(row=1,column=1,padx=8,pady=8)
        
        ditem3=Label(drinks_menu,text='ice-cream',font=('Arial',12,'bold'),fg='orange').grid(row=2,column=0,padx=15)
        ditem3_entery=Entry(drinks_menu,borderwidth=4,width=20,textvariable=self.icecream).grid(row=2,column=1,padx=8,pady=8)
        
        ditem4=Label(drinks_menu,text='juice',font=('Arial',12,'bold'),fg='orange').grid(row=3,column=0,padx=15)
        ditem4_entery=Entry(drinks_menu,borderwidth=4,width=20,textvariable=self.juice).grid(row=3,column=1,padx=8,pady=8)
        
        ditem5=Label(drinks_menu,text='tea',font=('Arial',12,'bold'),fg='orange').grid(row=4,column=0,padx=15)
        ditem5_entery=Entry(drinks_menu,borderwidth=4,width=20,textvariable=self.tea).grid(row=4,column=1,padx=8,pady=8)
        
        ditem6=Label(drinks_menu,text='coffie',font=('Arial',12,'bold'),fg='orange').grid(row=5,column=0,padx=15)
        ditem6_entery=Entry(drinks_menu,borderwidth=4,width=20,textvariable=self.coffie).grid(row=5,column=1,padx=8,pady=8)
        
        ditem7=Label(drinks_menu,text='milk',font=('Arial',12,'bold'),fg='orange').grid(row=6,column=0,padx=15)
        ditem7_entery=Entry(drinks_menu,borderwidth=4,width=20,textvariable=self.milk).grid(row=6,column=1,padx=8,pady=8)
        
        ditem8=Label(drinks_menu,text='water',font=('Arial',12,'bold'),fg='orange').grid(row=7,column=0,padx=15)
        ditem8_entery=Entry(drinks_menu,borderwidth=4,width=20,textvariable=self.water).grid(row=7,column=1,padx=8,pady=8)
        
        #--------------------------------------print seat--------------------------------#
        billarea=Frame(self.root,bd=5,relief=GROOVE,bg='white')
        billarea.place(x=960,y=145,height=360,width=380)
        
        billtitle=Label(billarea,text='Billarea',font=('Arial',20,'bold'),bg='orange',fg='white',bd=5,relief=GROOVE).pack(fill=X)
        
        scroll_y=Scrollbar(billarea,orient=VERTICAL)
        self.txtarea=Text(billarea,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        
        #---------------------------------------------billing Summery- CodeWithCurious-----------------------#
        billingsummery=LabelFrame(self.root,text='billing Summery- CodeWithCurious',font=('Arial',12,'bold'),bd=5,relief=GROOVE,bg='white',fg='orange')
        billingsummery.place(x=0,y=520,relwidth=1,height=165)
        
        totalstarter=Label(billingsummery,text='total starter',font=('Arial',12,'bold'),fg='orange').grid(row=0,column=0)
        totalstarter_entry=Entry(billingsummery,borderwidth=4,textvariable=self.total_starter).grid(row=0,column=1,padx=8,pady=10)
        
        totalbiriyai=Label(billingsummery,text='total biriyani',font=('Arial',12,'bold'),fg='orange').grid(row=1,column=0)
        totalbiriyani_entry=Entry(billingsummery,borderwidth=4,textvariable=self.total_biriyani).grid(row=1,column=1,padx=8,pady=10)
        
        totaldrinks=Label(billingsummery,text='total drinks',font=('Arial',12,'bold'),fg='orange').grid(row=2,column=0)
        totaldrinks_entry=Entry(billingsummery,borderwidth=4,textvariable=self.total_drinks).grid(row=2,column=1,padx=8,pady=10)
        
        totalstartertax=Label(billingsummery,text='Starter tax',font=('Arial',12,'bold'),fg='orange').grid(row=0,column=2)
        totalstartertax_entry=Entry(billingsummery,borderwidth=4,textvariable=self.a).grid(row=0,column=3,padx=8,pady=10)
        
        totalbiriyaitax=Label(billingsummery,text='Biriyani tax',font=('Arial',12,'bold'),fg='orange').grid(row=1,column=2)
        totalbiriyanitax_entry=Entry(billingsummery,borderwidth=4,textvariable=self.b).grid(row=1,column=3,padx=8,pady=10)
        
        totaldrinkstax=Label(billingsummery,text='Drinks tax',font=('Arial',12,'bold'),fg='orange').grid(row=2,column=2)
        totaldrinkstax_entry=Entry(billingsummery,borderwidth=4,textvariable=self.c).grid(row=2,column=3,padx=8,pady=10)
        
        buttons=Frame(billingsummery,bd=5,bg='white',relief=GROOVE)
        buttons.place(x=500,y=9,width=820,height=120)
        
        totalbill=Button(buttons,text='total bill',font=('Arial',15,'bold'),bd=5,bg='orange',fg='white',padx=5,pady=5,width=20,command=lambda:total(self)).pack(side=LEFT,padx=15)
        clearfield=Button(buttons,text='clear field',font=('Arial',15,'bold'),bd=5,bg='orange',fg='white',padx=5,pady=5,width=20,command=lambda:clear(self)).pack(side=LEFT,padx=15)
        exit=Button(buttons,text='exit',font=('Arial',15,'bold'),bd=5,bg='orange',fg='white',padx=5,pady=5,width=20,command=lambda:exit1(self)).pack(side=LEFT,padx=15)
        intro(self)
        
def intro(self):
    self.txtarea.delete(1.0,END)
    self.txtarea.insert(END,"\tWELCOME TO SUPER MARKET\n\tPhone-no.788648271")
    self.txtarea.insert(END,f"\n\nBill No : {self.billno.get()}")
    self.txtarea.insert(END,f"\nCustomer Name : {self.customername.get()}")
    self.txtarea.insert(END,f"\nPhone Number : {self.customerno.get()}")
    self.txtarea.insert(END,"\n====================================\n")
    self.txtarea.insert(END,"\nProduct\t\tQty\tPrice\n")
    self.txtarea.insert(END,"\n====================================\n")
    
def total(self):
    # if(self.customername.get()=="" or self.customerno.get()==""):
    #       messagebox.showerror("Error","Fill the complete Customer Details!!")
    self.sam=self.samoza.get()*50
    self.cut=self.cutlet.get()*60
    self.rol=self.rolls.get()*70
    self.chi=self.chips.get()*80
    self.vad=self.vada.get()*90
    self.vsp=self.vegsoup.get()*100
    self.csp=self.chickensoup.get()*150
    self.fsd=self.fruitsalad.get()*200
    total_starter_price=(
        self.sam+
        self.cut+
        self.rol+
        self.chi+
        self.vad+
        self.vsp+
        self.csp+
        self.fsd
        )
    self.total_starter.set(str(total_starter_price)+" Rs")
    self.a.set(str(round(total_starter_price*0.05,3))+" Rs")
    
    self.cbi=self.cbiri.get()*550
    self.vbi=self.vbiri.get()*360
    self.fbi=self.fbiri.get()*470
    self.bbi=self.bbiri.get()*780
    self.dbi=self.dbiri.get()*890
    self.ebi=self.ebiri.get()*300
    self.kus=self.kuska.get()*250
    self.ric=self.rice.get()*100
    total_biriyani_price=(
        self.cbi+
        self.vbi+
        self.fbi+
        self.bbi+
        self.dbi+
        self.ebi+
        self.kus+
        self.ric
        )
    self.total_biriyani.set(str(total_biriyani_price)+" Rs")
    self.b.set(str(round(total_biriyani_price*0.01,3))+" Rs")
    
    self.sod=self.soda.get()*100
    self.fal=self.faluda.get()*160
    self.ice=self.icecream.get()*170
    self.jui=self.juice.get()*80
    self.te=self.tea.get()*90
    self.cof=self.coffie.get()*50
    self.mil=self.milk.get()*150
    self.wat=self.water.get()*20
    total_drinks_price=(
        self.sod+
        self.fal+
        self.ice+
        self.jui+
        self.te+
        self.cof+
        self.mil+
        self.wat
        )
    self.total_drinks.set(str(total_drinks_price)+" Rs")
    self.c.set(str(round(total_drinks_price*0.10,3))+" Rs")
    
    self.total_bill=total_starter_price+total_drinks_price+total_biriyani_price+round(total_biriyani_price*0.01,3)+round(total_drinks_price*0.10,3)+round(total_starter_price*0.05,3)
    self.final_bill=str(self.total_bill)+" Rs"
    billarea(self)
    
def billarea(self):
    intro(self)
    if(self.samoza.get()!=0):
        self.txtarea.insert(END,f"samoza\t\t {self.samoza.get()} \t {self.sam}\n")
    if(self.cutlet.get()!=0):
        self.txtarea.insert(END,f"cutlet\t\t {self.cutlet.get()} \t {self.cut}\n")
    if(self.rolls.get()!=0):
        self.txtarea.insert(END,f"rolls\t\t {self.rolls.get()} \t {self.rol}\n")
    if(self.chips.get()!=0):
        self.txtarea.insert(END,f"chips\t\t {self.chips.get()} \t {self.chi}\n")
    if(self.vada.get()!=0):
        self.txtarea.insert(END,f"vada\t\t {self.vada.get()} \t {self.vad}\n")
    if(self.vegsoup.get()!=0):
        self.txtarea.insert(END,f"vegsoup\t\t {self.vegsoup.get()} \t {self.vsp}\n")
    if(self.chickensoup.get()!=0):
        self.txtarea.insert(END,f"chickensoup\t\t {self.chickensoup.get()} \t {self.csp}\n")
    if(self.fruitsalad.get()!=0):
        self.txtarea.insert(END,f"fruitsalad\t\t {self.fruitsalad.get()} \t {self.fsd}\n")
    if(self.cbiri.get()!=0):
        self.txtarea.insert(END,f"chicken biriyani\t\t {self.cbiri.get()} \t {self.cbi}\n")
    if(self.fbiri.get()!=0):
        self.txtarea.insert(END,f"fish biriyani\t\t {self.fbiri.get()} \t {self.fbi}\n")
    if(self.vbiri.get()!=0):
        self.txtarea.insert(END,f"veg biriyani\t\t {self.vbiri.get()} \t {self.vbi}\n")
    if(self.bbiri.get()!=0):
        self.txtarea.insert(END,f"bamboo biriyani\t\t {self.bbiri.get()} \t {self.bbi}\n")
    if(self.ebiri.get()!=0):
        self.txtarea.insert(END,f"egg biriyani\t\t {self.ebiri.get()} \t {self.ebi}\n")
    if(self.dbiri.get()!=0):
        self.txtarea.insert(END,f"dham biriyani\t\t {self.dbiri.get()} \t {self.dbi}\n")
    if(self.kuska.get()!=0):
        self.txtarea.insert(END,f"kuska\t\t {self.kuska.get()} \t {self.kus}\n")
    if(self.rice.get()!=0):
        self.txtarea.insert(END,f"rice & curry\t\t {self.rice.get()} \t {self.ric}\n")
    if(self.soda.get()!=0):
        self.txtarea.insert(END,f"soda\t\t {self.soda.get()} \t {self.sod}\n")
    if(self.faluda.get()!=0):
        self.txtarea.insert(END,f"faluda\t\t {self.faluda.get()} \t {self.fal}\n")
    if(self.tea.get()!=0):
        self.txtarea.insert(END,f"tea\t\t {self.tea.get()} \t {self.te}\n")
    if(self.coffie.get()!=0):
        self.txtarea.insert(END,f"coffie\t\t {self.coffie.get()} \t {self.cof}\n")
    if(self.juice.get()!=0):
        self.txtarea.insert(END,f"juice\t\t {self.juice.get()} \t {self.jui}\n")
    if(self.icecream.get()!=0):
        self.txtarea.insert(END,f"icecream\t\t {self.icecream.get()} \t {self.ice}\n")
    if(self.milk.get()!=0):
        self.txtarea.insert(END,f"milk\t\t {self.milk.get()} \t {self.mil}\n")
    if(self.water.get()!=0):
        self.txtarea.insert(END,f"water\t\t {self.water.get()} \t {self.wat}\n")
    
    self.txtarea.insert(END,f"------------------------------------\n")
    if(self.a.get()!="0.0 Rs"):
        self.txtarea.insert(END,f"Total Starter tax : {self.a.get()}\n")
    if(self.b.get()!="0.0 Rs"):
        self.txtarea.insert(END,f"Total Biriyani tax : {self.b.get()}\n")
    if(self.c.get()!="0.0 Rs"):
        self.txtarea.insert(END,f"Total Drinks tax : {self.c.get()}\n")
    self.txtarea.insert(END,f"Total Bill Amount : {self.final_bill}\n")
    self.txtarea.insert(END,f"------------------------------------\n")
        
def clear(self):
        self.txtarea.delete(1.0,END)
        self.billno.set('')
        self.customername.set('')
        self.customerno.set('')
        self.cutlet.set(0)
        self.samoza.set(0)
        self.vada.set(0)
        self.rolls.set(0)
        self.vegsoup.set(0)
        self.chickensoup.set(0)
        self.fruitsalad.set(0)
        self.chips.set(0)
        self.total_starter.set(0)
        self.total_biriyani.set(0)
        self.total_drinks.set(0)
        self.a.set(0)
        self.b.set(0)
        self.c.set(0)
        self.cbiri.set(0)
        self.fbiri.set(0)
        self.vbiri.set(0)
        self.bbiri.set(0)
        self.kuska.set(0)
        self.dbiri.set(0)
        self.rice.set(0)
        self.ebiri.set(0)
        self.soda.set(0)
        self.milk.set(0)
        self.juice.set(0)
        self.tea.set(0)
        self.coffie.set(0)
        self.water.set(0)
        self.icecream.set(0)
        self.faluda.set(0)
        # intro(self)
    
def exit1(self):
    self.root.destroy()
    
root=Tk()
root.iconphoto(False,tkinter.PhotoImage(file='logo.png'))
Bill_App(root)
root.mainloop()