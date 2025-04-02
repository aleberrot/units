from tkinter import *
from tkinter import ttk


# Crea una ventana sobre la cual vamos a trabajar
root = Tk()

# Cambia el título de la ventana
root.title("Conversor unidades informáticas")
# Cambia el tamaño de la ventana
root.geometry("400x300")
# Cambia el color de fondo de la ventana
root.configure(bg="lightblue")
# Cambia el icono de la ventana
# root.iconbitmap("icono.ico") # Descomentar y poner el path del icono
# Cambia el color del borde de la ventana
root.wm_attributes("-topmost", True)
# Cambia el color del borde de la ventana
root.wm_attributes("-alpha", 0.9)

# Crea un widget
frm = ttk.Frame(root, padding=10)
frm.grid()




# Inicializa loop de la ventana
root.mainloop()
