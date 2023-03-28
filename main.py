import os
import pandas as pd
import time
from csv import writer

# os.system("clear")
data = pd.read_csv('books.csv')


MAGENTA = '\033[35m'
CYAN = '\033[36m'
YELLOW = '\033[33m'
GREEN = '\033[32m'
RED = '\033[31m'
RESET = '\033[39m'

class Book:
    def __init__(self, id, titulo,isbn, genero, editorial, autor):
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.isbn = isbn
        self.editorial = editorial
        self.autor = autor

    def load_books():
        #"\n" salto de línea luego de mostrar la data
        return print(data.head(3).to_string(index=False),"\n")

    def list_books():
        #Imprime el csv ocultando el index, todos los campos se muestran al mismo nivel
        return print(data.to_string(index=False),"\n")

    def add_book(): 
        num_books = int(input("Ingrese la cantidad de libros a agregar: "))

        # Leer el archivo csv existente en un DataFrame.
        current_books = pd.read_csv('books.csv', index_col=0)

        # Obtener el último ID registrado.
        last_id = current_books.index.max()
        
        for i in range(num_books):
            titulo = input("\nIngrese el título: ")
            genero = input("Ingrese el género: ")
            isbn = input("Ingrese el ISBN: ")
            editorial = input("Ingrese la editorial: ")
            autor = input("Ingrese el autor (para dos o más, ingrese separados por comas): ")

            # Incrementar el ID del nuevo libro
            last_id += 1
            id = last_id
                  
            #Crear un nuevo DataFrame con los datos ingresados por el usuario.
            new_book = pd.DataFrame({
                "Título": [titulo], 
                "Género": [genero], 
                "ISBN": [isbn], 
                "Editorial": [editorial], 
                "Autor(es)": [autor]},
                index=[id]) 

            # Concatenar los dos DataFrames (el nuevo y el existente).
            current_books = pd.concat([current_books, new_book])

            print(f"\nSe ha agregado el libro con ID: {id}\n")
            print(new_book.to_string(index=False))
    
        # Escribir el DataFrame concatenado en el archivo csv.
        current_books.to_csv('books.csv', index_label='ID')
 
        print(f"\nSe agregó {num_books} libro(s) en total\n")


#Menu Interactivo

print(YELLOW+"\n📚 Bienvenido a Program Library 📚 "+ RESET,GREEN + "\nColoque el número correspondiente a su solicitud"+ RESET)
options = [ "Opción 1: Leer archivo csv y cargar 3 libros", 
            "Opción 2: Listar libros", 
            "Opción 3: Agregar libros", 
            "Opción 4: Eliminar libros",  
            "Opción 5: Buscar libro por ISBN o título",
            "Opción 6: Ordenar libros por título",
            "Opcion 7: Buscar libros por autor, editorial o género ",
            "Opcion 9: Editar o actualizar datos de un libro ",
            "Opcion 10: Guardar libros en archivo",
            "Opción 11: Salir del programa"]

print("\nPor favor, elige una opción: \n")
for i, option in enumerate(options):
    print(CYAN+f"{option}"+RESET)

option_number = str(input(GREEN +"\nIngrese el número: "+RESET))
while option_number not in ["1","2","3","5","6","7","8","9","10","11"]:
  option_number = input(RED+"Debes colocar números del 1 al 11."+RESET+GREEN +" Ingresa nuevamente tu respuesta: "+RESET)
  
print(GREEN+f"\nHas escogido la Opción {option_number}"+RESET)

#Opcion 1
if option_number == "1":   
    print("Leyendo archivo csv y cargando los tres primeros libros...\n")
    time.sleep(1)
    Book.load_books()

#Opcion 2
elif option_number == "2":
    print("Listando libros...\n")
    time.sleep(1)
    Book.list_books()

#Opcion 3
elif option_number == "3":
    print("Inicializando módulo de registro...\n")
    time.sleep(1)
    Book.add_book()