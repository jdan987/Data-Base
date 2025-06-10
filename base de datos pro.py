import sqlite3 as s3

conexion = s3.connect("base_de_datos.db")
cursor = conexion.cursor() #Es nuestro asistente

def tabla_existente(nombre_tabla):
    cursor.execute(f'''SELECT COUNT(name) FROM sqlite_master WHERE type='table' AND name='{nombre_tabla}' ''')#Este texto no es cualquier texto, sino que es un comando SQL válido. El motor de la base de datos sabe interpretar instrucciones de este tipo.
    if cursor.fetchone()[0] == 1: #sirve para saber cuantas ha contado y encontrar la tabla
        return True #Si encuentra la tabla devuelve True, demostrando que existe.
    else:
        cursor.execute('''CREATE TABLE PRODUCTO (CODIGO INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE TEXT, PRECIO REAL)''') #Si no la encuentra, la crea.
    return False #Devuelve False si no existe la tabla.

tabla_existente("PRODUCTO") #Llama a la función para comprobar si la tabla existe.

#C CREATE INSETAR
def insertar_producto(nombre, precio):
    cursor.execute(f'''INSERT INTO PRODUCTO (NOMBRE, PRECIO) VALUES ('{nombre}', {precio})''') #Inserta un producto en la tabla.
    conexion.commit() #Guarda los cambios en la base de datos.

#insertar_producto('Detergente', 2300) #Llama a la función para insertar un producto.
#insertar_producto('Jabón', 1000) #Llama a la función para insertar otro producto.
#insertar_producto('Suavizante', 1100)
# ...existing code...

def tabla_vacia():
    cursor.execute("SELECT COUNT(*) FROM PRODUCTO")
    return cursor.fetchone()[0] == 0

if tabla_vacia():
    insertar_producto('Detergente', 2300)
    insertar_producto('Jabón', 1000)
    insertar_producto('Suavizante', 1100)

# ...existing code...
#R READ OBTENER
def seleccionar_productos():
    cursor.execute('''SELECT * FROM PRODUCTO''') #Selecciona todos '*' los productos de la tabla.
    lista = [] #Crea una lista vacía para almacenar los productos.
    for fila in cursor.fetchall(): #Recorre todas las filas obtenidas de la consulta.
        lista.append(fila) #Añade cada fila a la lista.
    return lista #Devuelve la lista de productos.

#U UPDATE ACTUALIZAR:
#Se necesita un código para identificar el producto a actualizar y un diccionario con los campos a actualizar.
def actualizar_producto(codigo, diccionario):
    valoresValidos = ['NOMBRE', 'PRECIO'] #Lista de campos válidos que se pueden actualizar.
    for key in diccionario.keys(): #En diccionario.keys() se obtienen las claves del diccionario.
        if key not in valoresValidos:
            raise Exception('El campo no es válido') #Si la clave no está en la lista de valores válidos, se lanza una excepción. literal esto Levanta una excepción.
        else:
            query = '''UPDATE PRODUCTO SET {} ='{}' WHERE CODIGO = {}'''.format(key, diccionario [key], codigo) #Crea una consulta SQL para actualizar el producto.
            cursor.execute(query) #En este caso se almacenó todo el comando en una variable query y luego se ejecuta.
    conexion.commit() #Guarda los cambios en la base de datos.
actualizar_producto(1, {'NOMBRE': 'Detergente en polvo', 'PRECIO': 2500}) #Llama a la función para actualizar el producto con código 1.


#D DELETE ELIMINAR
def eliminar_producto(codigo):
    cursor.execute(f'''DELETE FROM PRODUCTO WHERE CODIGO = {codigo}''') #Elimina el producto con el código especificado.
    conexion.commit() #Guarda los cambios en la base de datos.
borrar_producto=1 #Código del producto a eliminar.

productos = seleccionar_productos() #¿Qué hace esto? evita que los numeros de los productos incrementen al imprimir la lista varias veces.
for i, producto in enumerate(productos, start=1):
    print(f"{i}. {producto[1]} - {producto[2]}")

#cursor.execute("DELETE FROM PRODUCTO") #se usa para borrar la lista de productos.
#conexion.commit()
print(seleccionar_productos()) #Llama a la función para obtener los productos e imprime el resultado. Están enumerados porque es autoincremental como se definió en la tabla_existente
