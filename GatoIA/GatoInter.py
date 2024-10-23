from customtkinter import *
import time 
from tkinter import messagebox
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

        self.BtnIn = CTkButton(master=self.AlmBtn, text="Iniciar", font=("Poppins", 20, "bold"), width=100, command=lambda:self.iniciar())
        self.BtnIn.pack(side=RIGHT, padx=20)
        
        
        self.almacenador = CTkFrame(master=self.ventana, width=350, height=350, border_color="white")
        self.almacenador.pack_propagate(0)
        self.almacenador.pack(expand=True, pady=10)

        self.AlmBtns = CTkFrame(master=self.almacenador, width=250, height=250, border_color="gray")
        self.AlmBtns.pack_propagate(0)
        self.AlmBtns.place(relx=0.5, rely=0.5, anchor=CENTER)  

        
        self.Btn1 = CTkButton(master=self.AlmBtns, text="x", font=("Poppins", 30, "bold"), width=70, height=70,command=lambda:self.tirar("11"))
        self.Btn1.grid(row=0, column=0, padx=10, pady=10)

        self.Btn2 = CTkButton(master=self.AlmBtns, text="x", font=("Poppins", 30, "bold"), width=70, height=70,command=lambda:self.tirar("12"))
        self.Btn2.grid(row=0, column=1, padx=10, pady=10)

        self.Btn3 = CTkButton(master=self.AlmBtns, text="x", font=("Poppins", 30, "bold"), width=70, height=70,command=lambda:self.tirar("13"))
        self.Btn3.grid(row=0, column=2, padx=10, pady=10)

        self.Btn4 = CTkButton(master=self.AlmBtns, text="x", font=("Poppins", 30, "bold"), width=70, height=70,command=lambda:self.tirar("21"))
        self.Btn4.grid(row=1, column=0, padx=10, pady=10)

        self.Btn5 = CTkButton(master=self.AlmBtns, text="x", font=("Poppins", 30, "bold"), width=70, height=70,command=lambda:self.tirar("22"))
        self.Btn5.grid(row=1, column=1, padx=10, pady=10)

        self.Btn6 = CTkButton(master=self.AlmBtns, text="x", font=("Poppins", 30, "bold"), width=70, height=70,command=lambda:self.tirar("23"))
        self.Btn6.grid(row=1, column=2, padx=10, pady=10)

        self.Btn7 = CTkButton(master=self.AlmBtns, text="x", font=("Poppins", 30, "bold"), width=70, height=70,command=lambda:self.tirar("31"))
        self.Btn7.grid(row=2, column=0, padx=10, pady=10)

        self.Btn8 = CTkButton(master=self.AlmBtns, text="x", font=("Poppins", 30, "bold"), width=70, height=70,command=lambda:self.tirar("32"))
        self.Btn8.grid(row=2, column=1, padx=10, pady=10)

        self.Btn9 = CTkButton(master=self.AlmBtns, text="x", font=("Poppins", 30, "bold"), width=70, height=70 ,command=lambda:self.tirar("33"))
        self.Btn9.grid(row=2, column=2, padx=10, pady=10)

        self.ventana.mainloop()

    def iniciar(self):
        self.juego = (False,"")
        self.turno = False
        self.casillas = [
            #usable,valor
            (True,0),(True,0),(True,0),
            (True,0),(True,0),(True,0),
            (True,0),(True,0),(True,0)
            ]
        self.ActualizarBTN()
    def tirarAI(self):
        if self.comprobaciones():
            self.ActualizarBTN()    
            self.iniciar()
            self.ActualizarBTN()
        else:
            self.turno = not self.turno
            # Estrategia básica: primero intenta ganar, luego bloquea al oponente, y si no, juega en una esquina o el centro.

            # Función para comprobar si la IA puede ganar en el siguiente movimiento
            def puedeGanar(jugador):
                for combinacion in [
                    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
                    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
                    [0, 4, 8], [2, 4, 6]              # Diagonales
                ]:
                    valores = [self.casillas[i][1] for i in combinacion]
                    if valores.count(jugador) == 2 and valores.count(0) == 1:
                        return combinacion[valores.index(0)]  # Retorna la posición para ganar
                return None

            # 1. Comprobar si la IA puede ganar
            pos = puedeGanar(2)  # 2 representa a la IA
            if pos is not None:
                self.casillas[pos] = (False, 2)
                self.ActualizarBTN()
                return

            # 2. Comprobar si el oponente puede ganar y bloquear
            pos = puedeGanar(1)  # 1 representa al jugador
            if pos is not None:
                self.casillas[pos] = (False, 2)
                self.ActualizarBTN()
                return

            # 3. Jugar en el centro si está disponible
            if self.casillas[4][0]:  # Casilla del centro
                self.casillas[4] = (False, 2)
                self.ActualizarBTN()
                return

            # 4. Jugar en una esquina si está disponible
            for esquina in [0, 2, 6, 8]:
                if self.casillas[esquina][0]:
                    self.casillas[esquina] = (False, 2)
                    self.ActualizarBTN()
                    return

            # 5. Jugar en un lado si está disponible
            for lado in [1, 3, 5, 7]:
                if self.casillas[lado][0]:
                    self.casillas[lado] = (False, 2)
                    self.ActualizarBTN()
                    return        

            # print("IA")
        if self.comprobaciones():
            # self.ActualizarBTN()    
            self.iniciar()
        self.ActualizarBTN()
        
        # self.turno = not self.turno


    def tirar(self,Casilla):
        self.turno = not self.turno
        if self.comprobaciones():
            self.iniciar()
        else:
            NC = ((int(Casilla[0])-1)*3 + int(Casilla[1])-1)
            self.casillas[NC] = (False, 1)
            self.ActualizarBTN()
            self.tirarAI()
        if self.comprobaciones():
            self.iniciar()
        self.ActualizarBTN()

    def comprobaciones(self):
        # Combinaciones ganad[oras
        combinaciones = [
            [0, 1, 2],  # Fila 1
            [3, 4, 5],  # Fila 2
            [6, 7, 8],  # Fila 3
            [0, 3, 6],  # Columna 1
            [1, 4, 7],  # Columna 2
            [2, 5, 8],  # Columna 3
            [0, 4, 8],  # Diagonal
            [2, 4, 6],  # Diagonal
        ]

        # Comprobar cada combinación
        for combinacion in combinaciones:
            valores = [self.casillas[i][1] for i in combinacion]
            # print(f"valores:{valores}")
            if valores[0] == valores[1] == valores[2] != 0:
                nombre = self.Nombre()
                messagebox.showinfo("Ganó", f"Ganador {nombre}")
                # self.iniciar()
                return True

        return False

    def Nombre(self):
        r = ""
        if self.turno:
            r = "Jugador"
            return r
        else:
            r = "AI"
            return r
            # print("nombre:IA")
        



    def ActualizarBTN(self):
        # print(self.juego[0])
        # if self.juego[0]:
        #     print("ganador")
        #     print(f"juego {self.juego[1]}")
        #     self.DisAll()
        # else:
            self.Btn1.configure(text=self.nombrar(self.casillas[0][1]))
            self.Btn2.configure(text=self.nombrar(self.casillas[1][1]))
            self.Btn3.configure(text=self.nombrar(self.casillas[2][1]))
            self.Btn4.configure(text=self.nombrar(self.casillas[3][1]))
            self.Btn5.configure(text=self.nombrar(self.casillas[4][1]))
            self.Btn6.configure(text=self.nombrar(self.casillas[5][1]))
            self.Btn7.configure(text=self.nombrar(self.casillas[6][1]))
            self.Btn8.configure(text=self.nombrar(self.casillas[7][1]))
            self.Btn9.configure(text=self.nombrar(self.casillas[8][1]))
            #disabilisar         
            self.Btn1.configure(state=self.nombrar(self.casillas[0][0]))
            self.Btn2.configure(state=self.nombrar(self.casillas[1][0]))
            self.Btn3.configure(state=self.nombrar(self.casillas[2][0]))
            self.Btn4.configure(state=self.nombrar(self.casillas[3][0]))
            self.Btn5.configure(state=self.nombrar(self.casillas[4][0]))
            self.Btn6.configure(state=self.nombrar(self.casillas[5][0]))
            self.Btn7.configure(state=self.nombrar(self.casillas[6][0]))
            self.Btn8.configure(state=self.nombrar(self.casillas[7][0]))
            self.Btn9.configure(state=self.nombrar(self.casillas[8][0]))
            
    def DisAll(self):
        self.Btn1.configure(state="disabled")
        self.Btn2.configure(state="disabled")
        self.Btn3.configure(state="disabled")
        self.Btn4.configure(state="disabled")
        self.Btn5.configure(state="disabled")
        self.Btn6.configure(state="disabled")
        self.Btn7.configure(state="disabled")
        self.Btn8.configure(state="disabled")
        self.Btn9.configure(state="disabled")

        # print("Actualizado")
    
    def nombrar(self,dato):
        if isinstance(dato, bool):
            if dato:
                r = "normal"
            else:
                r = "disabled"
        elif isinstance(dato, int):
            if dato == 1:
                r = "X"
            elif dato == 2:
                r = "O"
            else: 
                r = ""
        return r



Gato()
