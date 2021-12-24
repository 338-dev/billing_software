from tkinter import *
import math,random,os
from tkinter import messagebox



class Billing_System:
   def __init__(self,root):
       self.root=root
       self.root.geometry("1350x700+0+0") 
       self.root.title("InvoiceBooks")
       bg_color="#3ae0b4"
       title=Label(self.root,text="BigM Super Market",bd=5,relief=GROOVE,bg=bg_color,fg="white",font=("montserrat",30,"bold"),pady=2).pack(fill=X)

       # Icon set for program window
       p1 = PhotoImage(file = 'logo1.png')
       self.root.iconphoto(False, p1)


       #var//////////////////////////////////////////

 
       

      #drinks///////////////////////////////////////////
       self.thumbsup=IntVar()
       self.limca=IntVar()
       self.sprite=IntVar()
       self.Pepsi=IntVar()
       self.Fanta=IntVar()
       self.frooti=IntVar()



       

       #grocery//////////////////////////////////////
       self.wheat=IntVar()
       self.sugar=IntVar()
       self.tea=IntVar()
       self.rice=IntVar()
       self.food_oil=IntVar()
       self.daal=IntVar()





       

       
       #cosmetics////////////////////////////////////
       self.soap=IntVar()
       self.face_cream=IntVar()
       self.face_wash=IntVar()
       self.spray=IntVar()
       self.moisturizer=IntVar()
       self.hair_oil=IntVar()






       
   



       
       #taxes and price///////////////////////////////////////////////
       self.cosmetic_price=StringVar()
       self.grocery_price=StringVar()
       self.cold_drink_price=StringVar()

       self.cosmetic_tax=StringVar()
       self.grocery_tax=StringVar()
       self.cold_drink_tax=StringVar()



















       #details of customer////////////////////////////////////////
       self.c_name=StringVar()
       self.c_phone=StringVar()
       
       self.bill_no=StringVar()
       x=random.randint(1000,9999)
       self.bill_no.set(str(x))

       self.search_bill=StringVar()





       
       #customer details frame/////////////////////////////////////////
       F1=LabelFrame(self.root,bd=5,relief=GROOVE,text="Customer details",font=(" calibri",15,"bold"),fg="gold",bg=bg_color)
       F1.place(x=0,y=80,relwidth=1)
       cname_lbl=Label(F1,text="Customer name",bg=bg_color,fg="white",font=(" calibri",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
       cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=3,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

       cphn_lbl=Label(F1,text="Phone No.",bg=bg_color,fg="white",font=(" calibri",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
       cphn_txt=Entry(F1,width=15,textvariable=self.c_phone,font="arial 15",bd=3,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

       c_bill_lbl=Label(F1,text="Invoice no.",bg=bg_color,fg="white",font=(" calibri",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
       c_bill_txt=Entry(F1,width=15,textvariable=self.search_bill,font="arial 15",bd=3,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)
       
       bill_button=Button(F1,text="search",command=self.s_bill,width=10,bd=3,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)




 







       #cosmetics frame///////////////////////////////////////////////////////////
       F2=LabelFrame(self.root,bd=5,relief=GROOVE,text="Cosmetics",font=("calibri",15,"bold"),fg="gold",bg=bg_color)
       F2.place(x=5,y=180,width=325,height=380)

       bath_lbl=Label(F2,text="Bath soap",font=(" calibri",16,"bold"),bg=bg_color,fg="darkgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
       bath_txt=Entry(F2,width=10,textvariable=self.soap,font=(" calibri",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

       Face_cream_lbl=Label(F2,text="Face cream",font=(" calibri",16,"bold"),bg=bg_color,fg="darkgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
       Face_cream_txt=Entry(F2,width=10,textvariable=self.face_cream,font=(" calibri",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

       Face_w_lbl=Label(F2,text="Face wash",font=(" calibri",16,"bold"),bg=bg_color,fg="darkgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
       Face_w_txt=Entry(F2,width=10,textvariable=self.face_wash,font=(" calibri",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

       Hair_s_lbl=Label(F2,text="Hair spray",font=(" calibri",16,"bold"),bg=bg_color,fg="darkgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
       Hair_s_txt=Entry(F2,width=10,textvariable=self.spray,font=(" calibri",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

       Hair_g_lbl=Label(F2,text="Hair gel",font=(" calibri",16,"bold"),bg=bg_color,fg="darkgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
       Hair_g_txt=Entry(F2,width=10,textvariable=self.moisturizer,font=(" calibri",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

       body_lbl=Label(F2,text="Moisturizer",font=(" calibri",16,"bold"),bg=bg_color,fg="darkgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
       body_txt=Entry(F2,width=10,textvariable=self.hair_oil,font=(" calibri",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)





       #groceries/////////////////////////////////////////////////
       F3=LabelFrame(self.root,bd=5,relief=GROOVE,text="Grocery",font=("calibri",15,"bold"),fg="gold",bg=bg_color)
       F3.place(x=670,y=180,width=325,height=380)

       g1_lbl=Label(F3,text="Rice",font=(" calibri",16,"bold"),bg=bg_color,fg="darkgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
       g1_txt=Entry(F3,width=10,textvariable=self.rice,font=(" calibri",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

       g2_lbl=Label(F3,text="Food oil",font=(" calibri",16,"bold"),bg=bg_color,fg="darkgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
       g2_txt=Entry(F3,width=10,textvariable=self.food_oil,font=(" calibri",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

       g3_lbl=Label(F3,text="Pulse",font=(" calibri",16,"bold"),bg=bg_color,fg="darkgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
       g3_txt=Entry(F3,width=10,textvariable=self.daal,font=(" calibri",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

       g4_lbl=Label(F3,text="Wheat",font=(" calibri",16,"bold"),bg=bg_color,fg="darkgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
       g4_txt=Entry(F3,width=10,textvariable=self.wheat,font=(" calibri",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

       g5_lbl=Label(F3,text="Sugar",font=(" calibri",16,"bold"),bg=bg_color,fg="darkgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
       g5_txt=Entry(F3,width=10,textvariable=self.sugar,font=(" calibri",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

       g6_lbl=Label(F3,text="Tea",font=(" calibri",16,"bold"),bg=bg_color,fg="darkgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
       g6_txt=Entry(F3,width=10,textvariable=self.tea,font=(" calibri",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)





       #cold drink////////////////////////////////////////////////////
       F4=LabelFrame(self.root,bd=5,relief=GROOVE,text="Cold drink",font=("calibri",15,"bold"),fg="gold",bg=bg_color)
       F4.place(x=340,y=180,width=325,height=380)

       c1_lbl=Label(F4,text="Pepsi",font=(" calibri",16,"bold"),bg=bg_color,fg="darkgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
       c1_txt=Entry(F4,width=10,textvariable=self.Pepsi,font=(" calibri",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

       c2_lbl=Label(F4,text="Fanta",font=(" calibri",16,"bold"),bg=bg_color,fg="darkgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
       c2_txt=Entry(F4,width=10,textvariable=self.Fanta,font=(" calibri",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

       c3_lbl=Label(F4,text="Frooti",font=(" calibri",16,"bold"),bg=bg_color,fg="darkgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
       c3_txt=Entry(F4,width=10,textvariable=self.frooti,font=(" calibri",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

       c4_lbl=Label(F4,text="Thumbs up",font=(" calibri",16,"bold"),bg=bg_color,fg="darkgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
       c4_txt=Entry(F4,width=10,textvariable=self.thumbsup,font=(" calibri",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

       c5_lbl=Label(F4,text="Limca",font=(" calibri",16,"bold"),bg=bg_color,fg="darkgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
       c5_txt=Entry(F4,width=10,textvariable=self.limca,font=(" calibri",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

       c6_lbl=Label(F4,text="Sprite",font=(" calibri",16,"bold"),bg=bg_color,fg="darkgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
       c6_txt=Entry(F4,width=10,textvariable=self.sprite,font=(" calibri",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)






       #bill area/////////////////////////////////////////////////////////
       F5=Frame(self.root,bd=10,relief=GROOVE)
       F5.place(x=1010,y=180,width=340,height=380)
       bill_title=Label(F5,text="Invoice area",font="arial 15 bold",bd=3,relief=GROOVE).pack(fill=X)
       scrol_y=Scrollbar(F5,orient=VERTICAL)
       self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
       scrol_y.pack(side=RIGHT,fill=Y)
       scrol_y.config(command=self.txtarea.yview)
       self.txtarea.pack(fill=BOTH,expand=1)





       #button frame////////////////////////////////////////////////////////
       F6=LabelFrame(self.root,bd=5,relief=GROOVE,text="Invoice menu",font=(" calibri",15,"bold"),fg="gold",bg=bg_color)
       F6.place(x=0,y=560,relwidth=1,height=140)
       m1_lbl=Label(F6,text="total cosmetic price",bg=bg_color,fg="white",font=(" calibri",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
       m1_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=3,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

       m2_lbl=Label(F6,text="total grocery price",bg=bg_color,fg="white",font=(" calibri",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
       m2_txt=Entry(F6,width=18,font="arial 10 bold",textvariable=self.grocery_price,bd=3,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

       m3_lbl=Label(F6,text="total cold drink price",bg=bg_color,fg="white",font=(" calibri",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
       m3_txt=Entry(F6,width=18,font="arial 10 bold",textvariable=self.cold_drink_price,bd=3,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

       c1_lbl=Label(F6,text="cosmetic tax",bg=bg_color,fg="white",font=(" calibri",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
       c1_txt=Entry(F6,width=18,font="arial 10 bold",textvariable=self.cosmetic_tax,bd=3,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

       c2_lbl=Label(F6,text="grocery tax",bg=bg_color,fg="white",font=(" calibri",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
       c2_txt=Entry(F6,width=18,font="arial 10 bold",textvariable=self.grocery_tax,bd=3,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

       c3_lbl=Label(F6,text="cold drink tax",bg=bg_color,fg="white",font=(" calibri",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
       c3_txt=Entry(F6,width=18,font="arial 10 bold",textvariable=self.cold_drink_tax,bd=3,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

       btn_F=Frame(F6,bd=3,relief=GROOVE)
       btn_F.place(x=710,width=600,height=105)

       total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
       GBill_btn=Button(btn_F,text="Generate Bill",command=self.bill_area,bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)
       clear_btn=Button(btn_F,text="Clear",command=self.clear,bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)
       exit_btn=Button(btn_F,text="Exit",command=self.ask_exit,bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)
       self.welcome_bill()
       self.root.resizable(False, False)

   def total(self):
      

       self.g_r_p=self.rice.get()*50
       self.g_f_p=self.food_oil.get()*210
       self.g_d_p=self.daal.get()*90
       self.g_w_p=self.wheat.get()*200
       self.g_s_p=self.sugar.get()*70
       self.g_t_p=self.tea.get()*100
       self.total_grocery_price=float(self.g_r_p+self.g_f_p+self.g_d_p+self.g_w_p+self.g_s_p+self.g_t_p)   
       self.grocery_price.set("Rs. "+str(self.total_grocery_price))
       self.g_tax=round((self.total_grocery_price*0.1),2)
       self.grocery_tax.set("Rs. "+str(self.g_tax))


       self.c_s_p=self.soap.get()*70
       self.c_fc_p=self.face_cream.get()*90
       self.c_fw_p=self.face_wash.get()*50
       self.c_hs_p=self.spray.get()*250
       self.c_hg_p=self.moisturizer.get()*250
       self.c_bl_p=self.hair_oil.get()*150
       self.total_cosmetic_price=float(self.c_s_p+self.c_fc_p+self.c_fw_p+self.c_hs_p+self.c_hg_p+self.c_bl_p)   
       self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
       self.c_tax=round((self.total_cosmetic_price*0.05),2)
       self.cosmetic_tax.set("Rs. "+str(self.c_tax))

       self.d_m_p=self.Pepsi.get()*50
       self.d_c_p=self.Fanta.get()*50
       self.d_f_p=self.frooti.get()*30
       self.d_t_p=self.thumbsup.get()*55
       self.d_l_p=self.limca.get()*50
       self.d_s_p=self.sprite.get()*40
       self.total_drinks_price=float(self.d_m_p+self.d_c_p+self.d_f_p+self.d_t_p+self.d_l_p+self.d_s_p)   
       self.cold_drink_price.set("Rs. "+str(self.total_drinks_price))
       self.d_tax=round((self.total_drinks_price*0.05),2)
       self.cold_drink_tax.set("Rs. "+str(self.d_tax))

       self.Total_bill=float(self.total_cosmetic_price+self.total_grocery_price+self.total_drinks_price+self.c_tax+self.g_tax+self.d_tax)

   def welcome_bill(self):
       self.txtarea.delete('1.0',END)
       self.txtarea.insert(END,"\tBigM Super Market")   
       self.txtarea.insert(END,f"\n Invoice no : {self.bill_no.get()}") 
       self.txtarea.insert(END,f"\n Customer name : {self.c_name.get()}") 
       self.txtarea.insert(END,f"\n Phone no : {self.c_phone.get()}")
       self.txtarea.insert(END,f"\n=====================================")
       self.txtarea.insert(END,f"\n Products\t\tQTY\t\tprice") 
       self.txtarea.insert(END,f"\n=====================================") 
  
 

   def bill_area(self):
       if self.c_name.get()=="" or self.c_phone.get()=="":
           messagebox.showerror("error","Customer details are must")
       elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0"  and self.cold_drink_price.get()=="Rs. 0.0":
            messagebox.showerror("error","No Product Purchased")
       else:
           self.welcome_bill()
           
           if self.rice.get()!=0:
              self.txtarea.insert(END,f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}") 
           if self.food_oil.get()!=0:
              self.txtarea.insert(END,f"\n Food oil\t\t{self.food_oil.get()}\t\t{self.g_f_p}") 
           if self.daal.get()!=0:
              self.txtarea.insert(END,f"\n Daal\t\t{self.daal.get()}\t\t{self.g_d_p}") 
           if self.wheat.get()!=0:
              self.txtarea.insert(END,f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
           if self.sugar.get()!=0:
              self.txtarea.insert(END,f"\n Sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")
           if self.tea.get()!=0:
              self.txtarea.insert(END,f"\n Body hair_oil\t\t{self.tea.get()}\t\t{self.g_t_p}")

           if self.soap.get()!=0:
               self.txtarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}") 
           if self.face_cream.get()!=0:
              self.txtarea.insert(END,f"\n Face cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}") 
           if self.face_wash.get()!=0:
              self.txtarea.insert(END,f"\n Face wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}") 
           if self.spray.get()!=0:
              self.txtarea.insert(END,f"\n Spray\t\t{self.spray.get()}\t\t{self.c_hs_p}")
           if self.moisturizer.get()!=0:
              self.txtarea.insert(END,f"\n Hair moisturizer\t\t{self.moisturizer.get()}\t\t{self.c_hg_p}")
           if self.hair_oil.get()!=0:
              self.txtarea.insert(END,f"\n Body hair_oil\t\t{self.hair_oil.get()}\t\t{self.c_bl_p}") 

            
           if self.Pepsi.get()!=0:
              self.txtarea.insert(END,f"\n Pepsi\t\t{self.Pepsi.get()}\t\t{self.d_m_p}") 
           if self.Fanta.get()!=0:
              self.txtarea.insert(END,f"\n Fanta\t\t{self.Fanta.get()}\t\t{self.d_c_p}") 
           if self.frooti.get()!=0:
              self.txtarea.insert(END,f"\n Frooti\t\t{self.frooti.get()}\t\t{self.d_f_p}") 
           if self.thumbsup.get()!=0:
              self.txtarea.insert(END,f"\n Thumbs up\t\t{self.thumbsup.get()}\t\t{self.d_t_p}")
           if self.limca.get()!=0:
              self.txtarea.insert(END,f"\n Limca\t\t{self.limca.get()}\t\t{self.d_l_p}")
           if self.sprite.get()!=0:
              self.txtarea.insert(END,f"\n Sprite\t\t{self.sprite.get()}\t\t{self.d_s_p}")       

           self.txtarea.insert(END,f"\n------------------------------------")
           if self.cosmetic_tax.get()!="Rs. 0.0":
              self.txtarea.insert(END,f"\n Cosmetic Tax\t\t\t{self.cosmetic_tax.get()}") 
           if self.grocery_tax.get()!="Rs. 0.0":
              self.txtarea.insert(END,f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")
           if self.cold_drink_tax.get()!="Rs. 0.0":
              self.txtarea.insert(END,f"\n Cold Drink Tax\t\t\t{self.cold_drink_tax.get()}")

           self.txtarea.insert(END,f"\n Total  : \t\t\t Rs. {str(self.Total_bill)}")            
           self.txtarea.insert(END,f"\n------------------------------------")  
           self.save_bill()
                 
   def clear(self):
      self.search_bill.set("")
      self.cosmetic_price.set("")
      self.grocery_price.set("")
      self.cold_drink_price.set("")

      self.cosmetic_tax.set("")
      self.grocery_tax.set("")
      self.cold_drink_tax.set("")
         
      self.thumbsup.set(0)
      self.limca.set(0)
      self.sprite.set(0)
      self.Pepsi.set(0)
      self.Fanta.set(0)
         
      self.wheat.set(0)
      self.sugar.set(0)
      self.tea.set(0)
      self.rice.set(0)
      self.food_oil.set(0)
      self.daal.set(0)

      self.soap.set(0)
      self.face_cream.set(0)
      self.face_wash.set(0)
      self.spray.set(0)
      self.moisturizer.set(0)
      self.hair_oil.set(0)

      self.c_name.set("")
      self.c_phone.set("")
      self.bill_no.set("")
      x=random.randint(1000,9999)
      self.bill_no.set(str(x))
          

         
      self.welcome_bill()




      
                                                                               
   def save_bill(self):
       op=messagebox.askyesno("Save Bill","Do You Want to save the bill?")
       if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("memo/" + str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("saved",f"bill number: {self.bill_no.get()}saved successfully")
       else:
          return

   def s_bill(self):
      av="neg"
      for l in os.listdir("memo/"):
         if l.split('.')[0]==self.search_bill.get():
            f1=open(f"memo/{l}","r")
            self.txtarea.delete('1.0',END)
            for d in f1:
               self.txtarea.insert(END,d)
            
            f1.close()
            av="pos"
      if av=="neg":
         messagebox.showerror("Error","invalid invoice no.")

   def ask_exit(self):
      self.root.destroy()


root=Tk()
obj=Billing_System(root)
root.mainloop()




#////////////////////////////////////////////////////////////////////////End\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
