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
