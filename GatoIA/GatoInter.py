from customtkinter import *

class Gato():
    def __init__(self):
        super().__init__()
        self.ventana = CTk()
        self.ventana.title("UwU-Gato")
        ancho_pantalla = self.ventana.winfo_screenwidth()
        alto_pantalla = self.ventana.winfo_screenheight()
        ancho_ventana = 414
        alto_ventana = 511
        x_pos = (ancho_pantalla - ancho_ventana) // 2
        y_pos = (alto_pantalla - alto_ventana) // 2
        self.ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")
        self.ventana.resizable(0, 0)
        self.ventana._set_appearance_mode("black")
        
        self.almacenador2 = CTkFrame(master=self.ventana, width=350, height=100, border_color="white")
        self.almacenador2.pack_propagate(0)
        self.almacenador2.pack(side=TOP, pady=10)

        
        self.LBNomb = CTkLabel(master=self.almacenador2, text="UwU Gato IA", font=("Poppins",20,"bold"))
        self.LBNomb.pack(pady=5)

        self.AlmBtn = CTkFrame(master=self.almacenador2, width=350, height=50)
        self.AlmBtn.pack_propagate(0)
        self.AlmBtn.pack(pady=10)

        self.BtnSalir = CTkButton(master=self.AlmBtn, text="Salir", font=("Poppins", 20, "bold"), width=100)
        self.BtnSalir.pack(side=LEFT, padx=20)

        self.BtnIn = CTkButton(master=self.AlmBtn, text="Iniciar", font=("Poppins", 20, "bold"), width=100)
        self.BtnIn.pack(side=RIGHT, padx=20)
        
        
        self.almacenador = CTkFrame(master=self.ventana, width=350, height=350, border_color="white")
        self.almacenador.pack_propagate(0)
        self.almacenador.pack(expand=True, pady=10)

        self.AlmBtns = CTkFrame(master=self.almacenador, width=250, height=250, border_color="gray")
        self.AlmBtns.pack_propagate(0)
        self.AlmBtns.place(relx=0.5, rely=0.5, anchor=CENTER)  

        
        self.Btn1 = CTkButton(master=self.AlmBtns, text="x", font=("Poppins", 30, "bold"), width=70, height=70)
        self.Btn1.grid(row=0, column=0, padx=10, pady=10)

        self.Btn2 = CTkButton(master=self.AlmBtns, text="x", font=("Poppins", 30, "bold"), width=70, height=70)
        self.Btn2.grid(row=0, column=1, padx=10, pady=10)

        self.Btn3 = CTkButton(master=self.AlmBtns, text="x", font=("Poppins", 30, "bold"), width=70, height=70)
        self.Btn3.grid(row=0, column=2, padx=10, pady=10)

        self.Btn4 = CTkButton(master=self.AlmBtns, text="x", font=("Poppins", 30, "bold"), width=70, height=70)
        self.Btn4.grid(row=1, column=0, padx=10, pady=10)

        self.Btn5 = CTkButton(master=self.AlmBtns, text="x", font=("Poppins", 30, "bold"), width=70, height=70)
        self.Btn5.grid(row=1, column=1, padx=10, pady=10)

        self.Btn6 = CTkButton(master=self.AlmBtns, text="x", font=("Poppins", 30, "bold"), width=70, height=70)
        self.Btn6.grid(row=1, column=2, padx=10, pady=10)

        self.Btn7 = CTkButton(master=self.AlmBtns, text="x", font=("Poppins", 30, "bold"), width=70, height=70)
        self.Btn7.grid(row=2, column=0, padx=10, pady=10)

        self.Btn8 = CTkButton(master=self.AlmBtns, text="x", font=("Poppins", 30, "bold"), width=70, height=70)
        self.Btn8.grid(row=2, column=1, padx=10, pady=10)

        self.Btn9 = CTkButton(master=self.AlmBtns, text="x", font=("Poppins", 30, "bold"), width=70, height=70)
        self.Btn9.grid(row=2, column=2, padx=10, pady=10)

        self.ventana.mainloop()

Gato()
