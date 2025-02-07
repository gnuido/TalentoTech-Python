#integradorFinal.py

import sqlite3

#%--------------------------------------
def menuOpciones():
	print(	' ################################################\n',
			'|Seleccione una de las siguientes opciones:	|\n',
			'|\t\t\t\t\t\t|\n',
			'|1> Ver inventario completo.\t\t\t|\n',
			'|2> Añadir producto al inventario.\t\t|\n',
			'|3> Actualizar producto del inventario.\t\t|\n',
			'|4> Eliminar producto del inventario.\t\t|\n',
			'|5> Buscar producto en el inventario.\t\t|\n',
			'|6> Ayuda / FAQ\t\t\t\t|\n',
			'|7> Salir.\t\t\t\t\t|\n',
			'################################################\n'	)
	
	#control de ingreso válido
	while True:		#bucle para reiteración por error
		
		try:
			opcion = int(input())
			if 0 < opcion < 8:
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
	
	query = "CREATE TABLE IF NOT EXISTS PRODUCTOS (",
			"'ID' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE",
			"'MARCA' TEXT NOT NULL",
			"'DESCRIPCION' TEXT",
			"'PRECIO' REAL",
			"'STOCK' INTEGER NOT NULL",
			"'ESTANTE' INTEGER",
			"'PROVEEDOR' TEXT "
#-------------------
def mostrarInventario():
	conexion = sqlite3.connect("INVENTARIO.db")
	cursor = conexion.cursor()
	
	query = "SELECT * FROM PRODUCTOS"	
	
	
#%--------------------------------------
opcion = menuOpciones()

if opcion == 1:
