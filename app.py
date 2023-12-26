import tkinter as tk
from tkinter import simpledialog
import random
from time import sleep
from PIL import Image, ImageTk

class Tamagotchi:
    def __init__(self, nombre, root):
        #random.seed(42)
        self.nombre = nombre
        self.hambre = 0
        self.aburrimiento = 0
        self.cansancio = 0
        self.suciedad = 0
        self.tipo_comida = "Maíz"
        self.comida = 0
        self.dormido = False
        self.vivo = True
        self.nivel_dificultad = 0

    def comer(self):
        self.comida -= self.comida_encontrada
        self.hambre -= self.comida_encontrada
        if self.hambre < 0:
            self.hambre = 0
        if self.comida < 0:
            self.comida = 0
        self.suciedad += 1

    def jugar(self,n):
        num_aleatorio = random.randint(0, 2)
        if n == num_aleatorio:
            self.aburrimiento -= random.randint(1, self.nivel_dificultad)
            if self.aburrimiento < 0:
                self.aburrimiento = 0
            self.cansancio += random.randint(1, self.nivel_dificultad)
            self.hambre += random.randint(1, self.nivel_dificultad)
            self.suciedad += random.randint(1, self.nivel_dificultad)
            return True
        else:
            self.aburrimiento -= 1
            if self.aburrimiento < 0:
                self.aburrimiento = 0
            self.cansancio += 1
            self.hambre += 1
            self.suciedad += 1
            return False   

    def dormir(self):
        self.dormido = True
        self.cansancio -= 1
        if self.cansancio < 0:
            self.cansancio = 0

    def estar_dormido(self, func=False):
        sleep(3)
        if self.dormido == True:
            self.cansancio -= random.randint(2, 4)
            if self.cansancio < 0:
                self.cansancio = 0
            self.hambre +=1
            self.suciedad +=1

            if self.aburrimiento < 0:
                self.aburrimiento = 0
            if self.cansancio < 0:
                self.cansancio = 0
            if func:
                func()
        else :
            printe = f"{self.nombre} se ha despertado!"
            return printe

    def despertar(self, func=False):
        self.dormido = False
        #self.aburrimiento += 1
        if func:
            func()

    def duchar(self):
        self.suciedad -= random.randint(1, 4)
        if self.suciedad < 0:
            self.suciedad = 0
        self.cansancio += 1
        self.aburrimiento += 1

    def comprar(self):
        dificultad = random.randint(0, int(self.nivel_dificultad/2))
        self.comida_encontrada = random.randint(1, 5 - dificultad)
        self.comida += self.comida_encontrada
        if self.comida > 10:
            self.comida = 10
        self.suciedad += 1
        self.aburrimiento += 1
        self.cansancio += 1
        return self.comida_encontrada

    def mostrar_valores(self):
        if self.vivo == True:
            estado = "VIVO"
        else: 
            estado = "MUERTO"
        diccionario = {"Nombre": self.nombre,
                       "Aburrimiento": self.aburrimiento,
                       "Cansancio": self.cansancio,
                       "Comida": self.comida,
                       "¿Dormido?": self.dormido,
                       "Hambre": self.hambre,
                       "Suciedad": self.suciedad,
                       "Estado": estado,
                       "Nivel": self.nivel_dificultad}
        return diccionario

    def dificultad(self, nivel_dificultad):
        self.hambre += self.nivel_dificultad
        self.suciedad += self.nivel_dificultad
        self.aburrimiento += self.nivel_dificultad

    def morir(self):
        if self.hambre >= (15 - self.nivel_dificultad):
            printe = f"{self.nombre} murió de hambre... TT"
            self.vivo = False
            return printe
        elif self.suciedad >= (15 - self.nivel_dificultad):
            printe = f"{self.nombre} murió de guarro... TT"
            self.vivo = False
            return printe
        elif self.cansancio >= (15 - self.nivel_dificultad):
            printe = f"{self.nombre} murió de agotado... TT"
            self.vivo = False
            return printe
        elif self.aburrimiento > (15 - self.nivel_dificultad):
            printe = f"{self.nombre} murió del aburrimiento... TT"
            self.vivo = False
            return printe
        else:
            self.vivo = True
            printe = ""
            return printe

class TamagotchiApp:
    def __init__(self):
        self.tamagotchi = None

        self.root = tk.Tk()
        self.root.title("Tamagotchi App")
        self.root.configure(bg="pink")
        self.root.geometry("800x800")
        
        self.container = tk.Frame(self.root, bg="lightblue")
        self.container.pack(side= "top", pady=30)
    
        
        self.etiqueta = tk.Label(self.container, text="""Bienvenido\n al\n Juego del Tamagotchi""", font=("Arial", 50), bg=("lightblue"))
        self.etiqueta.pack(side ="top", pady=30)

        self.boton_iniciar = tk.Button(self.container, text="Iniciar", command=self.iniciar_juego, font=("Arial", 50))
        self.boton_iniciar.pack(side="top", pady=30)

        self.boton_continuar = tk.Button(self.container, text="Continuar", command=self.crear_tamagotchi, font=("Arial", 30))
        self.boton_continuar.pack(side="top", pady=30)
        self.boton_continuar.pack_forget()

        self.label_gif = tk.Label(self.container)
        self.label_gif.pack(side="top")

        self.ronda = 0

    def mostrar_gif(self, ruta, ancho, alto):

        imagen = Image.open(ruta).convert("RGBA")
        imagen = imagen.resize((ancho, alto), Image.LANCZOS)
        gif = ImageTk.PhotoImage(imagen)

        # Mostrar la imagen en la etiqueta
        self.label_gif.config(image=gif)
        
        self.label_gif.image = gif 
        self.label_gif.imagen_git =gif
        self.label_gif.pack()
        return gif

    def iniciar_juego(self):
        self.label_gif = tk.Label(self.container)
        self.label_gif.pack(side="top")

        ruta_imagen="./images/giphy.gif"
        self.mostrar_gif(ruta_imagen, 200, 200)

        self.etiqueta.config(text="Introduce un nivel de dificultad entre 1 y el 5:", font=("Arial", 30), bg=("lightblue"))
        self.etiqueta.pack(side="top", pady= 10)

        self.boton_iniciar.pack_forget()

        self.entry_dificultad = tk.Entry(self.container, font=("Arial", 30))
        self.entry_dificultad.pack(side="top", pady = 10)

        self.boton_continuar.config(text="Continuar", command=self.elegir_dificultad, font=("Arial", 30))
        self.boton_continuar.pack(side= "top",pady=10)
        
    
    def elegir_dificultad(self):
        try:
            entrada_dificultad = int(self.entry_dificultad.get())
            
            if 1 <= entrada_dificultad <= 5:
                self.tamagotchi = Tamagotchi("", self.container)
                self.tamagotchi.nivel_dificultad = int(self.entry_dificultad.get())
                self.tamagotchi.dificultad(self.tamagotchi.nivel_dificultad)

                self.etiqueta.config(text="Introduce un nombre para tu Tamagotchi:", font=("Arial", 30))
                self.etiqueta.pack(side="top", pady=10)

                self.entry_dificultad.pack_forget()

                self.entry_nombre = tk.Entry(self.container,font=("Arial", 30))
                self.entry_nombre.pack(side="top", pady=10)

                self.boton_continuar.config(text="Continuar", command=self.crear_tamagotchi, font=("Arial", 30))
                self.boton_continuar.pack(side= "top", pady=10)
            
            else:
                self.etiqueta.config(text="Ingrese un nivel\n de dificultad válido (entre 1 y 5).", font=("Arial", 30))
                self.etiqueta.pack(side="top", pady = 10)
                
        except ValueError:
            self.etiqueta.config(text="Ingrese un número entero entre 1 y 5.", font=("Arial", 30))
            self.etiqueta.pack(side="top", pady = 10)

    def crear_tamagotchi(self):
        nombre = self.entry_nombre.get()
        if nombre:
            self.tamagotchi.nombre = nombre
            self.mostrar_atributos_botones(side= "top", padx= 0, pady=3)
            self.label_gif = tk.Label(self.container_atributo)
            self.label_gif.pack(side="top", padx=20, pady=20)
            ruta_imagen="./images/14606916-coloridos-corazones-rojos-ilustración-inconsútil-en-fondo-rosado.jpg"
            self.mostrar_gif(ruta_imagen, 100, 100)
            

    def mostrar_atributos_solamente(self, side, padx, pady):
        diccionario = self.tamagotchi.mostrar_valores()
        
        for widget in self.root.winfo_children():
            #widget.destroy()
            widget.pack_forget()

        self.container = tk.Frame(self.root) # Un frame para contener las opciones del menú
        self.container.configure(bg="lightblue")
        self.container.pack(side= "top", padx= 0, pady=3)

        self.container_atributo = tk.Frame(self.container)
        self.container_atributo.config(bg="lightblue")
        self.container_atributo.pack(side = "left")

        self.etiqueta_ronda = tk.Label(self.container, text = f"Ronda {self.ronda}", font= ("Arial", 20, "bold"), bg="lightblue")
        self.etiqueta_ronda.pack(side= "top", padx= 0, pady=3)
        
        
        for key, value in diccionario.items():
            label_atributo = tk.Label(self.container_atributo, text=f"{key}: {value}\n", font= ("Arial", 20, "bold"), bg="lightblue")
            label_atributo.pack(side= "top", padx= 0, pady=3)
        
    def mostrar_atributos_botones(self, side,padx, pady):
        self.mostrar_atributos_solamente(side= side,padx=padx, pady=pady)
        opciones = ["Comer", "Jugar", "Dormir", "Duchar", "Comprar"]
        self.container_atributo = tk.Frame(self.container)
        self.container_atributo.config(bg="lightblue")
        self.container_atributo.pack(side = "left")
        
        for opcion in opciones:
            boton_opcion = tk.Button(self.container_atributo, text=opcion, command=lambda o=opcion.lower(): self.ejecutar_opcion(o), font=("Arial", 25), bg="pink")
            boton_opcion.pack(side= side,padx=padx, pady=pady)
        
       
    def ejecutar_opcion(self, opcion):
        printe = self.tamagotchi.morir()
    
        if self.tamagotchi.vivo == False:
            
            for widget in self.root.winfo_children():
                    widget.destroy()
                    widget.pack_forget()

            self.game_over = tk.Label(self.root, text=f"GAME OVER", font=("Arial", 50, "bold"), fg=("red"), bg=("pink"))
            self.game_over.pack(side= "top",pady= 30)
            
            self.causa_muerte = tk.Label(self.root, text=printe, font=("Arial", 30, "bold"), fg=("red"), bg=("pink"))
            self.causa_muerte.pack(side= "top",pady=30)

            def reiniciar():
                self.tamagotchi = None
                self.root.destroy()
                self.__init__()
                self.run()

            self.label_gif = tk.Label(self.root)
            self.label_gif.pack(side="top", padx=20, pady=20)
            ruta_imagen="./images/5a2d8dcab3c4622cbe359791.png"
            self.mostrar_gif(ruta_imagen, 250, 250)

            self.boton_reinicio = tk.Button(self.root, text="Reiniciar", command= reiniciar, bg=("red"), font=("Arial", 50, "bold"))
            self.boton_reinicio.pack(side= "top",pady=30)
       
        else:

            if opcion.lower() == "comer":

                if self.tamagotchi.hambre >0 and self.tamagotchi.comida > 0:
                    self.ronda += 1
                    getattr(self.tamagotchi, opcion.lower())()
                    self.mostrar_atributos_botones(side= "top",padx=20, pady=20)

                    self.opcion = tk.Label(self.container_atributo, text=f"Mmm {self.tamagotchi.tipo_comida}\n ¡¡Ñam Ñam!!", font=("Arial", 20, "bold"), fg="purple", bg= "lightblue")
                    self.opcion.pack(side="left")

                    self.label_gif = tk.Label(self.container_atributo)
                    self.label_gif.pack(side="left", padx=20, pady=20)
                    ruta_imagen="./images/5a2d8ddab3c4622cbe359792.png"
                    self.mostrar_gif(ruta_imagen, 100, 100)

                elif self.tamagotchi.comida == 0:
                    self.mostrar_atributos_botones(side= "top",padx=20, pady=20)
                    self.opcion = tk.Label(self.container_atributo, text="¡¡NO HAY COMIDA!!", font=("Arial", 20, "bold"), fg="red", bg= "lightblue")
                    self.opcion.pack(side="left")

                    self.label_gif = tk.Label(self.container_atributo)
                    self.label_gif.pack(side="left", padx=20, pady=20)
                    ruta_imagen="./images/38549218-alerta-alerta-de-la-compra-icono-del-carrito-de-la-imagen-del-vector-también-se-puede-utilizar.jpg"
                    self.mostrar_gif(ruta_imagen, 100, 100)

                else:
                    self.mostrar_atributos_botones(side= "top",padx=20, pady=20)
                    self.opcion = tk.Label(self.container_atributo, text="¡¡NO TENGO HAMBRE!!", font=("Arial", 20, "bold"), fg="purple", bg= "lightblue")
                    self.opcion.pack(side="left")

                    self.label_gif = tk.Label(self.container_atributo)
                    self.label_gif.pack(side="left", padx=20, pady=20)
                    ruta_imagen="./images/corazon.png"
                    self.mostrar_gif(ruta_imagen, 100, 100)
                    
                
            if opcion.lower() == "jugar":

                self.mostrar_atributos_solamente(side= "top",padx=20, pady=20)
                
                self.label_gif = tk.Label(self.container)
                self.label_gif.pack(side="top", padx=20, pady=20)
                ruta_imagen="./images/ruleta.png"
                self.mostrar_gif(ruta_imagen, 100, 100)
                
                self.opcion = tk.Label(self.container, text=f"{self.tamagotchi.nombre} quiere jugar...\n Elige un número entre 0 y 2:", font=("Arial", 14, "bold"), fg=("purple"), bg="lightblue")
                self.opcion.pack(side="top",padx=50, pady=50)

                self.numero = tk.Entry(self.container, font=("Arial", 20))
                self.numero.pack(side="top",padx=50, pady=50)

                self.boton_call = tk.Button(self.container, text="Continuar", command= lambda: continuar_callback(), font=("Arial", 20))
                self.boton_call.pack(side="top",padx=50, pady=50)

                def continuar_callback():

                    self.ronda += 1

                    n = int(self.numero.get())
                    resultado = getattr(self.tamagotchi, opcion.lower())(n)

                    self.mostrar_atributos_botones(side= "top",padx=10, pady=10)

                    if resultado == True:
                        self.opcion = tk.Label(self.container_atributo, text="¡CORRECTO!", font=("Arial", 20, "bold"), fg=("green"), bg="lightblue")
                        self.opcion.pack(side="left", padx=20, pady=50)
                        self.label_gif = tk.Label(self.container_atributo)
                        self.label_gif.pack(side="left", padx=20, pady=20)
                        ruta_imagen="./images/1490820803-4_82402.png"
                        self.mostrar_gif(ruta_imagen, 100, 100)
                    else:
                        self.opcion = tk.Label(self.container_atributo, text="¡INCORRECTO!", font=("Arial", 20, "bold"), fg=("red"), bg="lightblue")
                        self.opcion.pack(side="left", padx=20, pady=50)
                        self.label_gif = tk.Label(self.container_atributo)
                        self.label_gif.pack(side="left", padx=20, pady=20)
                        ruta_imagen="./images/perdedor.png"
                        self.mostrar_gif(ruta_imagen, 100, 100)

            if opcion.lower() == "duchar":
                if self.tamagotchi.suciedad != 0:
                    self.ronda += 1
                    getattr(self.tamagotchi, opcion.lower())()
                    self.mostrar_atributos_botones(side= "top",padx=20, pady=20)
                    self.opcion = tk.Label(self.container_atributo, text=f"{self.tamagotchi.nombre}\n está nikelao :P", font=("Arial", 20, "bold"), fg="purple", bg= "lightblue")
                    self.opcion.pack(side="left")
                    self.label_gif = tk.Label(self.container_atributo)
                    self.label_gif.pack(side="left", padx=20, pady=20)
                    ruta_imagen="./images/ducha.png"
                    self.mostrar_gif(ruta_imagen, 100, 100)
                else:
                    self.mostrar_atributos_botones(side= "top",padx=20, pady=20)
                    self.opcion = tk.Label(self.container_atributo, text=f"{self.tamagotchi.nombre}\n está limpio..", font=("Arial", 20, "bold"), fg="purple", bg= "lightblue")
                    self.opcion.pack(side="left")
                    self.label_gif = tk.Label(self.container_atributo)
                    self.label_gif.pack(side="left", padx=20, pady=20)
                    ruta_imagen="./images/corazon.png"
                    self.mostrar_gif(ruta_imagen, 100, 100)
            
            if opcion.lower() == "comprar":

                if self.tamagotchi.comida >= 10:
                    self.mostrar_atributos_botones(side= "top",padx=20, pady=20)

                    self.opcion = tk.Label(self.container, text = f"No hay dinero\n {self.tamagotchi.nombre}\n pa tanta compra.", font=("Arial", 20, "bold"), fg=("purple"), bg="lightblue")
                    self.opcion.pack(side="top",padx=50, pady=50)
                    self.label_gif = tk.Label(self.container)
                    self.label_gif.pack(side="top", padx=50, pady=50)
                    ruta_imagen="./images/corazon.png"
                    self.mostrar_gif(ruta_imagen, 100, 100)
                else:

                    self.mostrar_atributos_botones(side= "top",padx=20, pady=20) 

                    self.label_gif = tk.Label(self.container)
                    self.label_gif.pack(side="top", padx=20, pady=20)
                    ruta_imagen="./images/shopping-list_4797227.png"
                    self.mostrar_gif(ruta_imagen, 100, 100)
                           
                    self.opcion = tk.Label(self.container, text = f"¿Qué te apetece comprar\n {self.tamagotchi.nombre}?", font=("Arial", 20, "bold"), fg=("purple"), bg="lightblue")
                    self.opcion.pack(side="top",padx=50, pady=50)

                    self.entrada_comida = tk.Entry(self.container, font=("Arial", 20))
                    self.entrada_comida.pack(side="top", pady=10)

                    def callback():

                        self.ronda += 1
                    
                        self.tamagotchi.tipo_comida =  self.entrada_comida.get() 
                        cantidad = getattr(self.tamagotchi, opcion.lower())()
                        comida = self.entrada_comida.get()
                        if comida:
                            self.mostrar_atributos_botones(side= "top",padx=10, pady=10)
                            self.opcion = tk.Label(self.container_atributo, text=f"{self.tamagotchi.nombre}\n ha comprado {cantidad} de\n {self.tamagotchi.tipo_comida}", font=("Arial", 20, "bold"), fg=("purple"), bg="lightblue")
                            self.opcion.pack(side="left", padx=20, pady=50)
                            self.label_gif = tk.Label(self.container_atributo)
                            self.label_gif.pack(side="left", padx=20, pady=20)
                            ruta_imagen="./images/bolsa-de-la-compra.png"
                            self.mostrar_gif(ruta_imagen, 100, 100)

                    self.boton_call = tk.Button(self.container, text="Continuar", command= callback, font=("Arial", 20))
                    self.boton_call.pack(side="top",padx=50, pady=50)

            if opcion.lower() == "dormir":
                
                getattr(self.tamagotchi, opcion.lower())()

                self.mostrar_atributos_solamente(side= "top",padx=10, pady=10)

                def call_estar_dormido():
                    self.ronda += 1
                    
                    if self.tamagotchi.dormido == True:
                        self.mostrar_atributos_solamente(side= "top",padx=10, pady=10)

                        self.opcion = tk.Label(self.container, text=f"{self.tamagotchi.nombre} está dormido...zZz", font=("Arial", 20, "bold"), fg=("purple"), bg=("lightblue"))
                        self.opcion.pack(side="top",padx=50, pady=50)
                        self.label_gif = tk.Label(self.container)
                        self.label_gif.pack(side="top", padx=20, pady=20)
                        ruta_imagen="./images/5a2d8debb3c4622cbe359794.png"
                        self.mostrar_gif(ruta_imagen, 100, 100)

                        self.boton_despertar = tk.Button(self.container, text="Despertar", command= lambda: self.tamagotchi.despertar(func=call_estar_dormido), font=("Arial", 20), bg=("lightblue"))
                        self.boton_despertar.pack(side="bottom",padx=50, pady=50)

                        self.boton_dormir = tk.Button(self.container, text="Continuar durmiendo", command= lambda: self.tamagotchi.estar_dormido(func=call_estar_dormido), font=("Arial", 20), bg=("lightblue"))
                        self.boton_dormir.pack(side="bottom",padx=50, pady=50)
                        
                    else:
                        self.mostrar_atributos_botones(side= "top",padx=10, pady=10)
                        self.label_gif = tk.Label(self.container_atributo)
                        self.label_gif.pack(side="left", padx=20, pady=20)
                        ruta_imagen="./images/5a2d8de3b3c4622cbe359793.png"
                        self.mostrar_gif(ruta_imagen, 100, 100)

                call_estar_dormido()
        
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = TamagotchiApp()
    app.run()