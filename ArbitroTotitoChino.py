
playersScore = [0, 0]
punteoActual = 0

N = 4
maximoPuntos = (N - 1) * (N - 1)
horizontales = [0] * (N * (N - 1))
verticales = [0] * (N * (N - 1))

def turno(lista, posicion, player):
    global punteoActual
    valido = False
    repetirTurno = False
    while valido == False:
        if posicion < len(horizontales) and posicion > -1 and lista <= 2 and lista > 0:
            if lista == 1:
                if  horizontales[posicion] == 0:
                    horizontales[posicion] = 1
                else:
                    print("Espacio ya utilizado")
                    repetirTurno = True
                    break 
            else:
                if  verticales[posicion] == 0:
                    verticales[posicion] = 1
                else:
                    print("Espacio ya utilizado")
                    repetirTurno = True
                    break 
            
            punteoTurno = 0
            acumulador = 0
            contador = 0
            for x in range(0, N * (N - 1)):
                if((x+1) % N) != 0:
                    if horizontales[x] == 1 and horizontales[x+1] == 1 and verticales[contador + acumulador] == 1 and verticales[contador + acumulador + 1] == 1:
                        punteoTurno = punteoTurno + 1
                    
                    acumulador = acumulador + N
                else:
                    contador = contador + 1
                    acumulador = 0
            valido = True

            if punteoActual < punteoTurno:
                playersScore[player] = playersScore[player] + (punteoTurno - punteoActual)
                punteoActual = punteoTurno
                repetirTurno = True

            print("Lista horizontal:",horizontales)
            print("Lista vertical:",verticales)
        else:
            if posicion >= len(horizontales) or posicion <= -1:
                print("Ingresa una posicion valida dentro de la lista")
                repetirTurno = True
                break
            else:
                print("Ingresa una lista valida")
                repetirTurno = True
                break

    return repetirTurno


def juego():
    turnoJugador = 0
    while True:
        if punteoActual < maximoPuntos:
            print("Turno Jugador", turnoJugador+1)
            arreglo = int(input("Ingrese 1 si su movimiento sera horizontal y 2 si sera vertical: "))
            jugada = int(input("Ingrese una posicion de su jugada: "))
            repet = turno(arreglo, jugada, turnoJugador)

            if repet == False:
                if turnoJugador == 0:
                    turnoJugador = 1
                else:
                    turnoJugador = 0

        else:
            break
        print("Punteo Player 1:",playersScore[0])
        print("Punteo Player 2:",playersScore[1])
    print("Juego terminado")
    if playersScore[0] > playersScore[1]:
        print("Gano el jugador 1")
    elif playersScore[1] > playersScore[0]:
        print("Gano el jugador 2")
    else:
        print("Empate")

#Main
juego()
    
