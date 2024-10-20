from customtkinter import *

class Gato():
    juego = (False,"")
    turno = False
    casillas = [
        #usable,valor
        (True,0),(True,0),(True,0),
        (True,0),(True,0),(True,0),
        (True,0),(True,0),(True,0)
        ]


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
        
        self.Bt1=CTkButton(master=self.almacenador,width=138,height=50,text="1",font=("Poppins",30,"bold"),command=lambda:self.tirar("11"))
        self.Bt1.place(x=0,y=0)
        
        self.Bt2=CTkButton(master=self.almacenador,width=138,height=50,text="2",font=("Poppins",30,"bold"),command=lambda:self.tirar("12"))
        self.Bt2.place(x=138,y=0)
        
        self.Bt3=CTkButton(master=self.almacenador,width=138,height=50,text="3",font=("Poppins",30,"bold"),command=lambda:self.tirar("13"))
        self.Bt3.place(x=276,y=0)
        
        self.Bt4=CTkButton(master=self.almacenador,width=138,height=50,text="4",font=("Poppins",30,"bold"),command=lambda:self.tirar("21"))
        self.Bt4.place(x=0,y=150)
        
        self.Bt5=CTkButton(master=self.almacenador,width=138,height=50,text="5",font=("Poppins",30,"bold"),command=lambda:self.tirar("22"))
        self.Bt5.place(x=138,y=150)
        
        self.Bt6=CTkButton(master=self.almacenador,width=138,height=50,text="6",font=("Poppins",30,"bold"),command=lambda:self.tirar("23"))
        self.Bt6.place(x=276,y=150)
        
        self.Bt7=CTkButton(master=self.almacenador,width=138,height=50,text="7",font=("Poppins",30,"bold"),command=lambda:self.tirar("31"))
        self.Bt7.place(x=0,y=300)
        
        self.Bt8=CTkButton(master=self.almacenador,width=138,height=50,text="8",font=("Poppins",30,"bold"),command=lambda:self.tirar("32"))
        self.Bt8.place(x=136,y=300)
        
        self.Bt9=CTkButton(master=self.almacenador,width=138,height=50,text="9",font=("Poppins",30,"bold"),command=lambda:self.tirar("33"))
        self.Bt9.place(x=276,y=300)
        
        self.ventana.mainloop()
        
    def tirar(self,Casilla):
        NC = ((int(Casilla[0])-1)*3 + int(Casilla[1])-1)
        print(self.casillas[NC])
        print(f"NC={NC}")
        self.casillas[NC] = (False, 1)

        self.ActualizarBTN()
    def ActualizarBTN(self):
        if self.juego[1]:
            print("ganador")
            print(f"juego {self.juego[1]}")
        else:
            self.Bt1.configure(text=self.casillas[0][1])
            self.Bt2.configure(text=self.casillas[1][1])
            self.Bt3.configure(text=self.casillas[2][1])
            self.Bt4.configure(text=self.casillas[3][1])
            self.Bt5.configure(text=self.casillas[4][1])
            self.Bt6.configure(text=self.casillas[5][1])
            self.Bt7.configure(text=self.casillas[6][1])
            self.Bt8.configure(text=self.casillas[7][1])
            self.Bt9.configure(text=self.casillas[8][1])
            
        
        
        print("Actualizado")



Gato()