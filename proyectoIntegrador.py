#integradorFinal.py

import sqlite3

#%--------------------------------------
def menuOpciones():
	
	menuPrincipal	=	['\n\n#################################################\n'
						'|\t\t\t\t\t\t|\n'
						'|Seleccione una de las siguientes opciones:	|\n'
						'|\t\t\t\t\t\t|\n'
						'|1> Ver inventario.\t\t\t\t|',
						'|2> Añadir producto al inventario.\t\t|',
						'|3> Actualizar producto del inventario.\t\t|',
						'|4> Eliminar producto del inventario.\t\t|',
						'|5> Buscar producto en el inventario.\t\t|',
						'|6> Ayuda / FAQ\t\t\t\t\t|',
						'|7> Salir.\t\t\t\t\t|\n'
						'|\t\t\t\t\t\t|\n'
						'#################################################'			]
#solo las opciones suman a la cantidad de elementos en lista, que se emplea en controlOpciones()
	
	for i in menuPrincipal:
		print(i)
		
	opcion = controlOpciones(menuPrincipal)
	return(opcion)
#-------------------
def controlOpciones(menuActual):	
	#control de ingreso válido
	
	while True:		#bucle para reiteración por error
		
		try:
			opcion = int(input())
			if 0 < opcion < len(menuActual):
				return(opcion)
				break
			else:
				print('\nLa opción seleccionada no es válida, por favor, ingrese el dígito correspondiente a la opción escogida: \n')
				continue
		
		except ValueError:
			print('\nDebe ingresar una opción válida: \n')
			continue
			
#-------------------			
def crearTabla():
	
	conexion = sqlite3.connect("INVENTARIO.db")		#toda variable y comando de interacción con la base de datos implementará mayúsculas
	cursor = conexion.cursor()
	
	cursor.execute("""CREATE TABLE IF NOT EXISTS PRODUCTOS (
	'ID' NOT NULL UNIQUE,
	'MARCA' TEXT NOT NULL,
	'DESCRIPCION' TEXT NOT NULL,
	'PRECIO' REAL,
	'STOCK' INTEGER NOT NULL,
	'UBICACION' INTEGER,
	'PROVEEDOR' TEXT,
	PRIMARY KEY("ID" AUTOINCREMENT))
	""")
	
	conexion.close()
	
#-------------------
def mostrarProductos():
	
	#menù
	mostrarSubMenu =	['\n1> Mostrar inventario completo.\n',
						 '2> Mostar productos fuera de stock.\n',
						 '3> Mostar productos sin ubicar.\n',
						 '4> Mostrar productos sin proveedores.\n',
						 '5> Mostar productos sin precio.'			]
	
	for i in mostrarSubMenu:
		print(i)
	
	conexion = sqlite3.connect("INVENTARIO.db")
	cursor = conexion.cursor()
	
	#opciones de flujo
	opcionSubMenu = controlOpciones(mostrarSubMenu)
	if opcionSubMenu == 1:
		query = "SELECT * FROM PRODUCTOS"
		cursor.execute(query)
		inventario = cursor.fetchall()
	
	elif opcionSubMenu == 2:
		query = "SELECT * FROM PRODUCTOS WHERE STOCK = 0"
		cursor.execute(query)
		inventario = cursor.fetchall()
		
	elif opcionSubMenu == 3:
		query = "SELECT * FROM PRODUCTOS WHERE UBICACION = NULL"
		cursor.execute(query)
		inventario = cursor.fetchall()
		
	elif opcionSubMenu == 4:
		query = "SELECT * FROM PRODUCTOS WHERE PROVEEDOR = NULL"
		cursor.execute(query)
		inventario = cursor.fetchall()
		
	elif opcionSubMenu == 5:
		query = "SELECT * FROM PRODUCTOS WHERE PRECIO = NULL"
		cursor.execute(query)
		inventario = cursor.fetchall(5)
		
	#impresión de datos en egreso
	if len(inventario) == 0:
		print('\nNo hay productos que mostrar.\n')
	
	else:
		print('\n%------------------------------------------------%\n')
		for n in range(len(inventario)):
			print(	'ID: ' + str(inventario[n][0]),
					'\nMarca: ' + str(inventario[n][1]),
					'\nDescripción: ' + str(inventario[n][2]),
					'\nPrecio: ' + str(inventario[n][3]),
					'\nStock: ' + str(inventario[n][4]),
					'\nUbicación: ' + str(inventario[n][5]),
					'\nProveedor: ' + str(inventario[n][6]),	
					'\n'										)
		print('%------------------------------------------------%')
	
	conexion.close()

#-------------------
def añadirProductos():
	conexion = sqlite3.connect("INVENTARIO.db")
	cursor = conexion.cursor()
	
	query = ("""INSERT INTO PRODUCTOS ('MARCA', 'DESCRIPCION', 'PRECIO', 'STOCK', 'UBICACION', 'PROVEEDORES'),
	VALUES ()""")
	
#%--------------------------------------
#inicio
crearTabla()

while True:
	opcion = menuOpciones()

	#flujo
	if opcion == 1:
		mostrarProductos()
		continue
