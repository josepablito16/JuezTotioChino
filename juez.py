DIMENSION=3
tablero=[]
puntosJugador1=0
puntosJugador2=0

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
	return ((tablero[x1][y1]==0) and (tablero[x2][y2]==0))

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
			tablero[x1][y1]=1
			tablero[x2][y2]=1
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
	registrarTurno(turno%2)
	turno+=1
	print()
	printTablero()