DIMENSION=3
tablero=[]
PUNTOSJUGADOR1=0
PUNTOSJUGADOR2=0

puntosUsados=[]

'''
Se arma el tablero
'''
def armarTablero():
	for i in range(DIMENSION):
		fila=[]
		for j in range(DIMENSION):
			fila.append(0)
		tablero.append(fila)

'''
Se valida las coordenadas que 
la distancia sea de 1 y 0.
'''
def validarDistancia(x1,y1,x2,y2):
	difX=abs(x1-x2)
	difY=abs(y1-y2)

	return ((difX==1) and (difY==0)) or ((difX==0) and (difY==1))

'''
Se valida que las posiciones 
no esten usadas
'''
def validarPosiciones(x1,y1,x2,y2):

	#si las casillas son diferentes 
	condicion2=(tablero[x1][y1]!=tablero[x2][y2])

	#Valida que no se repitan puntos
	#Aqui me quedo
	if((tablero[x1][y1]==2) or (tablero[x2][y2]==2)) and condicion2:
		return ((tablero[x1][y1]==2) and (tablero[x2][y2]!=1)) or ((tablero[x1][y1]!=1) and (tablero[x2][y2]==2))

	for i in puntosUsados:
		if(i[0]==x1 and i[1]==y1 and i[2]==x2 and i[3]==y2) or (i[0]==x2 and i[1]==y2 and i[2]==x1 and i[3]==y1):
			return False
	
	return True


def validarPosiblePunto(x1,y1,x2,y2):
	if(x1==x2):
		try:
			if((tablero[x1+1][y1]==2) and (tablero[x2+1][y2]==2)):
				return True
		except Exception as e:
			pass

		try:
			if((tablero[x1-1][y1]==2) and (tablero[x2-1][y2]==2)):
				return True
		except Exception as e:
			pass

	if(y1==y2):
		try:
			if((tablero[x1][y1+1]==2) and (tablero[x2][y2+1]==2)):
				return True
		except Exception as e:
			pass

		try:
			if((tablero[x1][y1-1]==2) and (tablero[x2][y2-1]==2)):
				return True
		except Exception as e:
			pass

	return False
		



'''
Se solicitan las coordenadas y se verifica si es valido o no
'''
def registrarTurno(jugador):
	while True:

		print("Turno Jugador "+str(jugador))
		x1=int(input("Ingrese x1: "))
		y1=int(input("Ingrese y1: "))

		x2=int(input("Ingrese x2: "))
		y2=int(input("Ingrese y2: "))

		
		if(validarDistancia(x1,y1,x2,y2) and validarPosiciones(x1,y1,x2,y2)):
			puntosUsados.append([x1,y1,x2,y2])
			if(tablero[x1][y1]==1):
				tablero[x1][y1]=2
			else:
				tablero[x1][y1]=1

			if(tablero[x2][y2]==1):
				tablero[x2][y2]=2
			else:
				tablero[x2][y2]=1

			
			if(validarPosiblePunto(x1,y1,x2,y2)):
				return True

			break
		else:
			print("Posiciones malas")
			continue


'''
Se imprime el tablero
'''
def printTablero():
	for i in tablero:
		print(i)


armarTablero()
##MAIN
turno=0
while True:
	if(registrarTurno(turno%2)):
		if((turno%2)==0):
			PUNTOSJUGADOR1+=1
		else:
			PUNTOSJUGADOR2+=1
		continue
	
	turno+=1
	print()
	printTablero()
	print("puntos:")
	print("Jugador 1"+str(PUNTOSJUGADOR1))
	print("Jugador 2"+str(PUNTOSJUGADOR2))