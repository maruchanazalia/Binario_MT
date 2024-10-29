import tkinter as tk
from tkinter import ttk

def validar_y_sumar(input_binario):
    # Verificar que la entrada comience con "10"
    if not input_binario.startswith("10"):
        return "Error: La entrada debe comenzar con '10'."
    
    valor_inicial = 2
    
    resto_binario = input_binario[2:]
    
    if resto_binario:
        valor_resto = int(resto_binario, 2)
    else:
        valor_resto = 0
    
    resultado = valor_inicial + valor_resto
    return resultado

def ejecutar_maquina():
    entrada_binaria = entrada.get()
    resultado = validar_y_sumar(entrada_binaria)
    
    # Mostrar el resultado en la tabla o un mensaje de error
    if isinstance(resultado, int): 
        tabla_resultados.insert("", "end", values=(entrada_binaria, resultado))
        mensaje_resultado.config(text="")
    else: 
        mensaje_resultado.config(text=resultado, fg="red")

root = tk.Tk()
root.title("Máquina de Turing - Suma de binarios con prefijo '10'")

etiqueta_entrada = tk.Label(root, text="Ingrese un número binario que comience con '10':")
etiqueta_entrada.pack()

entrada = tk.Entry(root)
entrada.pack()
boton_ejecutar = tk.Button(root, text="Calcular", command=ejecutar_maquina)
boton_ejecutar.pack()

tabla_resultados = ttk.Treeview(root, columns=("Entrada", "Resultado"), show="headings")
tabla_resultados.heading("Entrada", text="Entrada")
tabla_resultados.heading("Resultado", text="Resultado")
tabla_resultados.pack()

mensaje_resultado = tk.Label(root, text="")
mensaje_resultado.pack()

root.mainloop()
