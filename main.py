# -*- coding: utf-8 -*-

# @author: Matheus Felipe
# @github: github.com/matheusfelipeog

# Builtin
import tkinter as tk

# Módulo próprio
# Own Module
from app.calculadora import Calculadora

if __name__ == '__main__':
    master = tk.Tk()
    main = Calculadora(master)
    main.start()
