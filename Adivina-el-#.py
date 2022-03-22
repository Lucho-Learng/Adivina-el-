import random


def run():
    num_de_la_pc = random.randint(1, 100)
    num_elegido = int(input("Escribe un numero entre 1 y 100: "))
    while num_elegido != num_de_la_pc:
        if num_elegido < num_de_la_pc:
            print("Busca un numero mas grande: ")
        else:
            print("Busca un numero mas pequeno: ")
        num_elegido = int(input("Elige otro numero: "))
    print("Ganastes!")


if __name__ == "__main__":
    run()

# Juego de escoger un # cualquiera entre 1 y 100 y adivinarle
# a la computadora cual es el # GANADOR
