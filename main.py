import customtkinter as ctk
from utils import *

# set theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


# TODO Configuracion ventana
app = ctk.CTk()
app.title("Iconversor")
app.geometry("800x600")

# TODO creamos un atributo en app para almacenar el label que contendra el resultado asi tener una referencia global a este
app.resultado_label = None

# TODO creamos un atributo en app para almacenar el label que contendra el error
app.error_label = None


# TODO event handler
def handle_click(event):
    ...

def handle_select(value):
    ...

def convert():
    # TODO checkeamos si el widget existe y si es asi lo borramos
    if app.resultado_label:
        app.resultado_label.destroy()

    if app.error_label:
        app.error_label.destroy()

    # TODO obtener valor de la entry
    value = entry.get()
    # TODO obtener valor del dropdown menu
    option = dropdown_menu.get()

    # TODO crear una variable donde almacenaremos el resultado
    decimal: int = 0
    binario = None
    hexadecimal = None

    try: 
        if not value:
            raise ValueError("Este campo no puede estar vacío")
        match option:
            case "HEX":
                decimal = hexadecimal_a_decimal(value)
            case "BINARIO":
                decimal = binario_a_decimal(value)
            case "DECIMAL":
                decimal, binario, hexadecimal = convertir_todo(value)
                
            case _:
                raise Exception("FUCION INVALIDA")

        app.resultado_label = ctk.CTkLabel(
            master=frm,
            text=decimal if not hexadecimal and not binario else f"""
            Decimal -> {decimal}
            Binario -> {binario}
            Hexadecimal -> {hexadecimal}

            """ , 
            font=("Arial", 14),
            wraplength=300)
        app.resultado_label.pack(pady=10)


    except ValueError as e:
        app.error_label = ctk.CTkLabel(
            master=frm,
            text=e,
            text_color="red",
            font=("Arial", 20, "bold")
            )
        app.error_label.pack(pady=10)
    
# TODO Frame
frm = ctk.CTkFrame(
       master=app,
       corner_radius=15,
       border_width=2)
frm.pack(pady=20, padx=20, fill="both", expand=True)

# TODO Widgets del Frame

title_label = ctk.CTkLabel(
        master=frm,
        text="Conversor Unidades",
        font=("Arial", 20, "bold"))

dropdown_menu = ctk.CTkComboBox(
        master=frm,
        values=["HEX", "BINARIO", "DECIMAL"],
        command=handle_select,
        width=200,
        height=40,
        dropdown_font=("Arial", 12),
        corner_radius=10
        )

entry = ctk.CTkEntry(
        master=frm,
        placeholder_text="Ingrese un valor",
        width=200,
        height=40,
        corner_radius=10

        )
button = ctk.CTkButton(
        master=frm,
        text="Convertir",
        width=200,
        height=40,
        corner_radius=10,
        fg_color="#2E86C1",
        hover_color="#3498DB",
        command=convert)

title_label.pack(pady=20)
entry.pack(pady=10)
dropdown_menu.pack(pady=10)
button.pack(pady=10, padx=10)

# Inicializa loop de la ventana
app.mainloop()
