# classShowRecord.py
import tkinter as tk
from classGetRecord import GetRecord

class ShowRecord:
    @staticmethod
    def configurar_interfaz(root):
        # Configuración de la ventana principal
        root.title("Último Registro Estudiante")
        root.geometry("300x200")

        # Botón para obtener el último registro
        boton = tk.Button(root, text="Obtener Último Registro", command=ShowRecord.obtener_y_mostrar)
        boton.pack(pady=10)

        # Label para mostrar los resultados
        ShowRecord.resultado_label = tk.Label(root, text="", justify="left")
        ShowRecord.resultado_label.pack(pady=10)

    @staticmethod
    def obtener_y_mostrar():
        # Obtiene el último registro de la API
        registro = GetRecord.obtener_ultimo_registro()
        # Muestra los datos obtenidos
        ShowRecord.mostrar_datos(registro)

    @staticmethod
    def mostrar_datos(registro):
        if "error" in registro:
            texto = registro["error"]
        else:
            texto = (
                f"ID: {registro['id']}\n"
                f"Nombre: {registro['nombre']}\n"
                f"Apellido: {registro['apellido']}\n"
                f"Ciudad: {registro['ciudad']}\n"
                f"Calle: {registro['calle']}"
            )
        ShowRecord.resultado_label.config(text=texto)
