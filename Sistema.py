import tkinter as tk
from tkinter import ttk

# REGLAS DEL SISTEMA EXPERTO

def regla_caminar(hechos):
    if hechos["distancia"] == "corta" and hechos["clima"] == "bueno":
        return "Caminar"
    return None

def regla_autobus(hechos):
    if hechos["distancia"] == "media" and hechos["transporte_publico"]:
        return "Autobús"
    return None


def regla_automovil(hechos):
    if hechos["distancia"] == "larga":
        return "Automóvil"
    return None


REGLAS = [regla_caminar, regla_autobus, regla_automovil]

# MOTOR DE INFERENCIA

def motor_inferencia(hechos):
    for regla in REGLAS:
        resultado = regla(hechos)
        if resultado:
            return regla.__name__, resultado
    return "Ninguna", "No se pudo determinar un transporte"

# INTERFAZ GRÁFICA
def recomendar():
    hechos = {
        "distancia": distancia_var.get(),
        "clima": clima_var.get(),
        "transporte_publico": transporte_var.get()
    }

    regla, recomendacion = motor_inferencia(hechos)

    resultado_label.config(
        text=f"Regla aplicada: {regla}\nRecomendación: {recomendacion}"
    )


# Ventana principal
ventana = tk.Tk()
ventana.title("Sistema Experto de Transporte")
ventana.geometry("300x300")

# Distancia
 
tk.Label(ventana, text="Distancia del recorrido").pack(pady=5)
distancia_var = tk.StringVar(value="corta")
ttk.Combobox(
    ventana,
    textvariable=distancia_var,
    values=["corta", "media", "larga"],
    state="readonly"
).pack()

# Clima
tk.Label(ventana, text="Estado del clima").pack(pady=5)
clima_var = tk.StringVar(value="bueno")
ttk.Combobox(
    ventana,
    textvariable=clima_var,
    values=["bueno", "malo"],
    state="readonly"
).pack()

# Transporte público
tk.Label(ventana, text="Transporte publico").pack(pady=5)
transporte_var = tk.StringVar(value="Disponible")
ttk.Combobox(
    ventana,
    textvariable=transporte_var,
    values=["Disponible", "No Disponible"],
    state="readonly"
).pack()

# Botón
tk.Button(
    ventana,
    text="Recomendar transporte",
    command=recomendar
).pack(pady=10)

# Resultado
resultado_label = tk.Label(
    ventana,
    text="",
    font=("Arial", 12),
    fg="Purple",
    justify="center"
)
resultado_label.pack(pady=10)

# Ejecutar interfaz
ventana.mainloop()
