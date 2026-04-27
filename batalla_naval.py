# Función para mostrar el tablero en consola
def mostrar_tablero(tablero):
    print("\nTablero:")
    # Recorre cada fila de la matriz
    for fila in tablero:
        # Imprime los elementos de la fila separados por espacios
        print(" ".join(str(x) for x in fila))


# Función que procesa un disparo del jugador
def disparar(tablero, fila, columna):
    # Si hay un barco en la posición
    if tablero[fila][columna] == 1:
        print( "¡Le diste a un barco!")
        tablero[fila][columna] = "X"  # Marca como impactado
        return True
    # Si es agua
    elif tablero[fila][columna] == 0:
        print("Agua...")
        tablero[fila][columna] = "-"  # Marca como disparo fallido
        return False
    # Si ya se disparó antes en esa casilla
    else:
        print("Ya disparaste ahí")
        return None


# Función para contar cuántos barcos hay en el tablero
def contar_barcos(tablero):
    contador = 0
    # Recorre toda la matriz
    for fila in tablero:
        for casilla in fila:
            if casilla == 1:  # Cuenta solo las casillas con barcos
                contador += 1
    return contador


# MATRIZ que representa el tablero del juego
# 1 = barco, 0 = agua
tablero = [
    [0, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0]
]

# Número de intentos disponibles
intentos = 5

# Se cuentan los barcos iniciales
barcos_restantes = contar_barcos(tablero)


# BUCLE PRINCIPAL DEL JUEGO
# Se ejecuta mientras haya intentos y barcos por destruir
while intentos > 0 and barcos_restantes > 0:
    
    mostrar_tablero(tablero)  # Muestra el estado actual
    
    # Información para el jugador
    print(f"\nBarcos restantes: {barcos_restantes}")
    print(f"Intentos restantes: {intentos}")
    
    # Entrada de datos del usuario
    fila = int(input("Ingrese fila: "))
    columna = int(input("Ingrese columna: "))
    
    # Se realiza el disparo
    resultado = disparar(tablero, fila, columna)
    
    # Si acertó, se reduce el número de barcos
    if resultado == True:
        barcos_restantes -= 1
    
    # Se reduce un intento en cada jugada
    intentos -= 1


# RESULTADO FINAL DEL JUEGO
if barcos_restantes == 0:
    print("¡Ganaste!")
else:
    print("Se acabaron los intentos")
