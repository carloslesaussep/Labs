import tkinter as tk
from tkinter import ttk

def mostrar_tabla(datos):
    # Crear ventana emergente para la tabla
    ventana_tabla = tk.Toplevel(root)
    ventana_tabla.title("Resultados en Tabla")
    ventana_tabla.geometry("400x250")
    
    # Definir columnas de la tabla
    columnas = ("Variable", "Valor")
    tree = ttk.Treeview(ventana_tabla, columns=columnas, show="headings")
    
    # Configurar encabezados
    for col in columnas:
        tree.heading(col, text=col)
        tree.column(col, width=180, anchor="center")
        
    # Insertar los datos en la tabla
    for clave, valor in datos.items():
        tree.insert("", "end", values=(clave, valor))
        
    # Mostrar la tabla en la ventana
    tree.pack(fill="both", expand=True, padx=10, pady=10)

def procesar_datos():
    # Recoger la información introducida en los inputs
    datos = {
        "Nombre": entry_nombre.get(),
        "Edad": entry_edad.get(),
        "Ciudad": entry_ciudad.get(),
        "Ocupación": entry_ocupacion.get()
    }
    
    # Llamar a la función que crea la ventana emergente con la tabla
    mostrar_tabla(datos)

# 
root = tk.Tk()
root.title("Formulario de Datos")
root.geometry("320x280")

# 
tk.Label(root, text="Nombre:").pack(anchor="w", padx=20, pady=(10, 0))
entry_nombre = tk.Entry(root, width=30)
entry_nombre.pack(padx=20, pady=2)

tk.Label(root, text="Edad:").pack(anchor="w", padx=20)
entry_edad = tk.Entry(root, width=30)
entry_edad.pack(padx=20, pady=2)

tk.Label(root, text="Ciudad:").pack(anchor="w", padx=20)
entry_ciudad = tk.Entry(root, width=30)
entry_ciudad.pack(padx=20, pady=2)

tk.Label(root, text="Ocupación:").pack(anchor="w", padx=20)
entry_ocupacion = tk.Entry(root, width=30)
entry_ocupacion.pack(padx=20, pady=2)

# 
btn_enviar = tk.Button(root, text="Generar Tabla", command=procesar_datos, bg="#4CAF50", fg="white")
btn_enviar.pack(pady=15)

root.mainloop()