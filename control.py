import customtkinter as ctk
from PIL import Image
from buscador import arduino

# ----------------- Configuración inicial ------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

#---------------------------- Logica ----------------------------

def mensaje(a):
    if not arduino.is_open: return
    arduino.write(a.encode())

def cargar(a):
    if not arduino.is_open: return
    arduino.write(a.encode())

#--------------------------------- Estructura ----------------------------
#--------------------------- Crear ventana principal -------------------
app = ctk.CTk()
app.title("Control Remoto")
app.geometry("400x500")

#------------------------------------ Cargar imágenes ----------------------
ruta = "./assets/img/"
rutaLogo = "./assets/"
img_arriba = ctk.CTkImage(Image.open(ruta + "arriba.png"), size=(80, 80))
img_abajo = ctk.CTkImage(Image.open(ruta + "abajo.png"), size=(80, 80))
img_izquierda = ctk.CTkImage(Image.open(ruta + "izquierda.png"), size=(80, 80))
img_derecha = ctk.CTkImage(Image.open(ruta + "derecha.png"), size=(80, 80))
img_logo = ctk.CTkImage(Image.open(rutaLogo + "logo.png"), size=(90, 90))

# ------------------------------- Título -----------------------------------
titulo = ctk.CTkLabel(app, text="Control Remoto", font=("Arial", 20, "bold"))
titulo.pack(pady=10)

# ------------------------------- Contenedor principal ------------------------------
frame_principal = ctk.CTkFrame(app)
frame_principal.pack(pady=10, padx=10, fill="both", expand=True)

# ------------------------------- Botón arriba -----------------------------------------
btn_arriba = ctk.CTkButton(frame_principal, image=img_arriba, text="", width=60, height=60, command=lambda: mensaje("arriba"))
btn_arriba.place(x=190, y=80, anchor="center")
# ------------------------------- Botón izquierda -----------------------------------------
btn_izquierda = ctk.CTkButton(frame_principal, image=img_izquierda, text="", width=60, height=60, command=lambda: mensaje("izquierda"))
btn_izquierda.place(x=75, y=185, anchor="center")

# ------------------------------- Logo central -----------------------------------------
logo = ctk.CTkLabel(frame_principal, image=img_logo, text="")
logo.place(x=190, y=185, anchor="center")

# ------------------------------- Botón derecha -----------------------------------------
btn_derecha = ctk.CTkButton(frame_principal, image=img_derecha, text="", width=60, height=60, command=lambda: mensaje("derecha"))
btn_derecha.place(x=300, y=185, anchor="center")
# ------------------------------- Botón abajo -----------------------------------------
btn_abajo = ctk.CTkButton(frame_principal, image=img_abajo, text="", width=60, height=60, command=lambda: mensaje("abajo"))
btn_abajo.place(x=190, y=300, anchor="center")

#---------------------------------------- extra --------------------------
nombreEmpresa = ctk.CTkLabel(app, text="Soluciones Tecnologicas Bello", font=("Arial", 10, "bold"))
nombreEmpresa.place(x=15, y=430)

#--------------------------------- codigo de conexion --------------------------------
inputCode = ctk.CTkEntry(app, width=190, height=10, corner_radius=10, placeholder_text="Código de acceso")
inputCode.place(x=15, y=463)
botonCargar = ctk.CTkButton(app, width=150, height=10, text="Cargar", command=lambda: cargar(inputCode.get()), corner_radius=10)
botonCargar.place(x=220, y=463)

app.mainloop()