# CP Means:- Cost Price
# SP Means:- Selling Price



from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox
import profit
import loss
class Main:
    def __init__(self, root):
        self.root = root
        
        self.root.geometry("400x200+500+200")
        self.root.resizable(False,False)
        self.root.title("Profit & Loss Finder | Developed By:-A.Ali")
        # self.root.config(bg='black')


       
        

        # Entry fields for CP and SP
        self.CP=Entry(self.root,bg='lightblue')
        self.CP.place(x=120 , y=20)

        self.SP=Entry(self.root,bg='lightblue')
        self.SP.place(x=120 , y=60)


        
        # Labels for entry fileds
        font="times new roman"
        CPlabel=Label(self.root,text="Enter C.P. " ,font=(font,15),)
        CPlabel.place(x=10,y=20)


        SPlabel=Label(self.root,text="Enter S.P.",font=(font,15))
        SPlabel.place(x=10,y=60)

        # Buttons 
     
        Button2=Button(self.root,text="Calculate",command=self.calculate)
        Button2.place(x=150,y=100)

  

    def calculate(self):
        # Taking input from entrtfields
        Cp=self.CP.get()
        Sp=self.SP.get()
      
            

        # Computing
        if int(Sp)>int(Cp):

            Result=profit.profit(Sp,Cp)
           

        elif int(Sp)<int(Cp):
            Result=loss.loss(Cp,Sp)
           
        
        elif int(Sp)==int(Cp)or int(Cp)==int(Sp):
            Result=("Nothing has gained nor loss")
        

        RessultLabel=Label(self.root,text=Result,fg="green",font=("times new roman",15,"bold")).place(x=0,y=150,relwidth=1)
        
root = Tk()
obj = Main(root)
root.mainloop()
