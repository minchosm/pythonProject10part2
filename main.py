from tkinter import ttk, Tk
import tkinter

ventana = tkinter.Tk()
ventana.config(width=600, height=600)
ventana.title = "Lista desplegable"
texto = tkinter.StringVar(value="")
lista = ttk.Combobox(state="readonly", values=["Valor 1", "Valor 2", "Valor3"])
lista.grid(column=0, row=0)
etiqueta = ttk.Label(text="Selecciona un valor")
etiqueta.grid(column=0, row=1)
ventana.mainloop()
