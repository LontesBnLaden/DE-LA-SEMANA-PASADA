import datetime

class Alumno:
    def __init__(self, nombre, direccion, nota1, nota2, fecha):
        self.nombre = nombre
        self.direccion = direccion
        self.nota1 = nota1
        self.nota2 = nota2
        self.fecha = fecha

    def suma_notas(self):
        return self.nota1 + self.nota2

    def resta_notas(self):
        return self.nota1 - self.nota2

    def convertir_nombre_mayusculas(self):
        self.nombre = self.nombre.upper()

    def obtener_ano(self):
        # Obtener el año de la fecha (suponiendo que la fecha está en formato 'YYYY-MM-DD')
        return self.fecha.year

    def guardar_en_archivo(self):
        # Abrir el archivo alumno.txt en modo escritura
        with open("C:/Users/Alumno.F10KLAB103PC18/Downloads/Juandiego.txt", "w") as archivo:
            archivo.write(f"Nombre: {self.nombre}\n")
            archivo.write(f"Dirección: {self.direccion}\n")
            archivo.write(f"Nota 1: {self.nota1}\n")
            archivo.write(f"Nota 2: {self.nota2}\n")
            archivo.write(f"Suma de notas: {self.suma_notas()}\n")
            archivo.write(f"Año de la fecha: {self.obtener_ano()}\n")


# Ejemplo de uso:
alumno1 = Alumno("Juandiego Garcia", "Los portales 567", 7.5, 8.5, datetime.date(2000, 5, 12))

# Convertir el nombre a mayúsculas
alumno1.convertir_nombre_mayusculas()

# Guardar la información en un archivo
alumno1.guardar_en_archivo()