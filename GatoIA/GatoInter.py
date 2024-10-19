from customtkinter import *

class Gato():
    def __init__(self):
        super().__init__()
        self.ventana=CTk()
        self.ventana.title("UwU-Gato")
        ancho_pantalla = self.ventana.winfo_screenwidth()
        alto_pantalla = self.ventana.winfo_screenheight()
        ancho_ventana = 414
        alto_ventana = 511
        x_pos = (ancho_pantalla - ancho_ventana) // 2
        y_pos = (alto_pantalla - alto_ventana) // 2
        self.ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")
        self.ventana.resizable(0, 0)
        #self.ventana.propagate(0)
        #self.ventana.overrideredirect(True)
        self.ventana._set_appearance_mode("light")
        
        self.almacenador=CTkFrame(master=self.ventana,width=414,height=511)
        self.almacenador.pack_propagate(0)
        self.almacenador.pack(expand=True)
        
        self.LB1=CTkLabel(master=self.almacenador,text="X",font=("Poppins",30,"bold"))
        self.LB1.place(x=100,y=150)
        
        self.LB2=CTkLabel(master=self.almacenador,text="X",font=("Poppins",30,"bold"))
        self.LB2.place(x=160,y=150)
        
        self.LB3=CTkLabel(master=self.almacenador,text="X",font=("Poppins",30,"bold"))
        self.LB3.place(x=220,y=150)
        
        self.LB4=CTkLabel(master=self.almacenador,text="X",font=("Poppins",30,"bold"))
        self.LB4.place(x=100,y=180)
        
        self.LB5=CTkLabel(master=self.almacenador,text="X",font=("Poppins",30,"bold"))
        self.LB5.place(x=160,y=180)
        
        self.LB6=CTkLabel(master=self.almacenador,text="X",font=("Poppins",30,"bold"))
        self.LB6.place(x=220,y=180)
        
        self.LB7=CTkLabel(master=self.almacenador,text="X",font=("Poppins",30,"bold"))
        self.LB7.place(x=100,y=210)
        
        self.LB8=CTkLabel(master=self.almacenador,text="X",font=("Poppins",30,"bold"))
        self.LB8.place(x=160,y=210)
        
        self.LB9=CTkLabel(master=self.almacenador,text="X",font=("Poppins",30,"bold"))
        self.LB9.place(x=220,y=210)
        
        self.ventana.mainloop()
Gato()