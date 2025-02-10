#integradorFinal.py

import sqlite3

#%--------------------------------------
def menuOpciones():
	menuPrincipal	=	['#################################################\n|'
						'|Seleccione una de las siguientes opciones:	|\n'
						'|\t\t\t\t\t\t|\n'
						'|1> Ver inventario.\t\t\t\t|',
						'|2> Añadir producto al inventario.\t\t|',
						'|3> Actualizar producto del inventario.\t\t|',
						'|4> Eliminar producto del inventario.\t\t|',
						'|5> Buscar producto en el inventario.\t\t|',
						'|6> Ayuda / FAQ\t\t\t\t\t|',
						'|7> Salir.\t\t\t\t\t|\n'
						'#################################################\n']
#solo las opciones suman a la cantidad de elementos en lista, que se emplea en controlOpciones()

	for i in menuPrincipal:
		print(i)

#-------------------
def controlOpciones(opcion, menuActual):	
	#control de ingreso válido
	while True:		#bucle para reiteración por error
		
		try:
			opcion = int(input())
			if 0 < opcion < len(menuActual):
				return(opcion)
				break
			else:
				print('La opción seleccionada no es válida, por favor, ingrese el dígito correspondiente a la opción escogida: ')
				continue
		
		except ValueError:
			print('Debe ingresar una opción válida: ')
			continue
			
#-------------------			
def crearTabla():
	conexion = sqlite3.connect("INVENTARIO.db")		#toda variable y comando de interacción con la base de datos implementará mayúsculas
	cursor = conexion.cursor()
	
	cursor.execute("""CREATE TABLE IF NOT EXISTS PRODUCTOS (
	'ID' PRIMARY KEY NOT NULL UNIQUE AUTOINCREMENT,
	'MARCA' TEXT NOT NULL,
	'DESCRIPCION' TEXT NOT NULL,
	'PRECIO' REAL,
	'STOCK' INTEGER NOT NULL,
	'UBICACION' INTEGER,
	'PROVEEDOR' TEXT)
	""")
	
	conexion.close()
	
#-------------------
def mostrarInventario():
	conexion = sqlite3.connect("INVENTARIO.db")
	cursor = conexion.cursor()
	
	query = "SELECT * FROM PRODUCTOS"
	cursor.execute(query)
	
	inventario = cursor.fetchall()
	
	if len(inventario) == 0:
		print('El inventario se encuentra vacío.')
	else:
		return(inventario)
	
	conexion.close()

#-------------------
def añadirInventario():
	conexion = sqlite3.connect('INVENTARIO.db')
	cursor = conexion.cursor()
	
	query = "INSERT "

#-------------------
def buscarInventario():
	conexion = sqlite3.connect('INVENTARIO.db')
	cursor = conexion.cursor()
	
	query = "SELECT "
#%--------------------------------------


opcion = menuOpciones()


