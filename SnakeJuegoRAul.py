import random

def main():
    alto = 15
    ancho = 20
    max_tamano = 100

    colaX = [0] * (max_tamano + 1)
    colaY = [0] * (max_tamano + 1)

    cabezaX = 10
    cabezaY = 7
    tamano = 1

    colaX[1] = cabezaX
    colaY[1] = cabezaY

    direccion = "d"
    gameOver = False

    manzanaX = random.randint(2, ancho - 2)
    manzanaY = random.randint(2, alto - 2)

    while not gameOver:
        for i in range(1, alto + 1):
            for j in range(1, ancho + 1):
                dibujado = False

                if i == 1 or i == alto or j == 1 or j == ancho:
                    print("#", end="")
                    dibujado = True
                else:
                    if i == cabezaY and j == cabezaX:
                        print("O", end="")
                        dibujado = True
                    elif i == manzanaY and j == manzanaX:
                        print("@", end="")
                        dibujado = True
                    else:
                        for k in range(2, tamano + 1):
                            if colaX[k] == j and colaY[k] == i:
                                print("o", end="")
                                dibujado = True
                                break
                        if not dibujado:
                            print(" ", end="")
            print()

        print("Puntuacion:", tamano - 1)
        print("Ingresa una letra (W, A, S, D) y presiona ENTER.")
        print("Para seguir derecho, teclea X y da ENTER.")

        tecla = input().lower()

        if tecla in ["w", "a", "s", "d"]:
            if not (tecla == "w" and direccion == "s") and \
               not (tecla == "s" and direccion == "w") and \
               not (tecla == "a" and direccion == "d") and \
               not (tecla == "d" and direccion == "a"):
                direccion = tecla

        if tamano > 1:
            for k in range(tamano, 1, -1):
                colaX[k] = colaX[k - 1]
                colaY[k] = colaY[k - 1]

        if direccion == "w":
            cabezaY -= 1
        elif direccion == "s":
            cabezaY += 1
        elif direccion == "a":
            cabezaX -= 1
        elif direccion == "d":
            cabezaX += 1

        colaX[1] = cabezaX
        colaY[1] = cabezaY

        if cabezaX == 1 or cabezaX == ancho or cabezaY == 1 or cabezaY == alto:
            gameOver = True

        if tamano > 1:
            for k in range(2, tamano + 1):
                if cabezaX == colaX[k] and cabezaY == colaY[k]:
                    gameOver = True
                    break

        if cabezaX == manzanaX and cabezaY == manzanaY:
            if tamano < max_tamano:
                tamano += 1
                colaX[tamano] = colaX[tamano - 1]
                colaY[tamano] = colaY[tamano - 1]
            manzanaX = random.randint(2, ancho - 2)
            manzanaY = random.randint(2, alto - 2)

    print("=======================")
    print("      FIN DEL JUEGO    ")
    print("   Puntuacion:", tamano - 1)
    print("=======================")

if __name__ == "__main__":
    main()
