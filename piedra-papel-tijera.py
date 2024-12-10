nombre1=input("Como se llama el jugador 1?: ")
nombre2=input("Como se llama el jugador 2?: ")

jugador1 = input(f"Hola {nombre1}, ¿qué eliges? Piedra, Papel o Tijeras: ").lower()
while jugador1 not in ["piedra", "papel", "tijeras"]:
    print("Entrada inválida. Por favor, elige entre Piedra, Papel o Tijeras.")
    jugador1 = input(f"{nombre1}, ¿qué eliges? Piedra, Papel o Tijeras: ").lower()

jugador2 = input(f"Hola {nombre2}, ¿qué eliges? Piedra, Papel o Tijeras: ").lower()
while jugador2 != ["piedra", "papel", "tijeras"]:
    print("Entrada inválida. Por favor, elige entre Piedra, Papel o Tijeras.")
    jugador2 = input(f"{nombre2}, ¿qué eliges? Piedra, Papel o Tijeras: ").lower()

condicion1 = jugador1=="piedra" and jugador2=="tijeras"
condicion2 = jugador1=="papel" and jugador2=="piedra"
condicion3 = jugador1=="tijeras" and jugador2=="papel"

if jugador1 == jugador2:
    print("Empate entre",nombre1 +" y",nombre2)
elif condicion1 or condicion2 or condicion3:
    print("Gana", nombre1 + "!")
else:
    print("Gano", nombre2 + "!")