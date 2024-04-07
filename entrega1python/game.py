import random

# Lista de palabras posibles
words = ["python", "programacion", "computadora", "codigo", "desarrollo",
"inteligencia", "fortnite", "valorant"]

# Elegir una palabra al azar
secret_word = random.choice(words)
# Número máximo de fallos permitidos
max_fall_attempts = 3
# Lista para almacenar las letras adivinadas
guessed_letters = []

print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
print("Elige la dificultad con la que deseas jugar")

while True:
    option = input("1 = facil  2 = media  3 = dificil\n")
    if (option == "1") or (option == "2") or (option == "3"):
        break
    else:
        print("La opcion ingresada no es valida. Intente de nuevo.")
        continue
  
if option == "1":
    vowels = "aeiou"
    letters = []
    for letter in secret_word:
        if letter in vowels:
            # Si es una vocal la agrego a la lista letters y la agrego a la lista de letras adivinadas
            letters.append(letter)
            guessed_letters.append(letter)
        else:
             letters.append("_")
    # Le paso la cadena que arme en la lista letters a word displayed que es un string            
    word_displayed = "".join(letters)
    # Mostrarla palabra parcialmente adivinada
    print(f"Palabra: {word_displayed}")

elif option == "2":
    # Hago un string que el primer y el ultimo digito sean los de la palabra secreta
    word_displayed = secret_word[0] + "_" * (len(secret_word)-2) + secret_word [len(secret_word)-1]

    # Mostrarla palabra parcialmente adivinada
    print(f"Palabra: {word_displayed}")

elif option == "3":
    word_displayed = "_" * len(secret_word)
    # Mostrarla palabra parcialmente adivinada
    print(f"Palabra: {word_displayed}")


# Variable para contar los intentos fallidos, cada intento fallido suma 1, si acierta, no suma
attempts = 0

while (attempts < max_fall_attempts ):
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()

    #Verifica/soluciona si la letra es un string vacio
    if (letter == ""):
        print("Error. No ha ingresado ninguna letra. Intente de nuevo. ")
        continue
    else:
        # Verificar si la letra ya ha sido adivinada
        if letter in guessed_letters:
            print("Ya has intentado con esa letra. Intenta con otra.")
            continue

        # Agregar la letra a la lista de letras adivinadas
        guessed_letters.append(letter)

        # Verificar si la letra está en la palabra secreta
        if letter in secret_word:
            print("¡Bien hecho! La letra está en la palabra.")    
        else:
            print("Lo siento, la letra no está en la palabra.")
            # Sumo uno para que el intento cuente como fallido
            attempts = (attempts + 1)
    
        # Mostrar la palabra parcialmente adivinada
        letters = []
        for letter in secret_word:
            if letter in guessed_letters:
                letters.append(letter)
            else:
                letters.append("_")
        
        # Si es la opcion 2 siempre debo mostrar el primer y el ultimo caracter
        if option == "2":
            letters[0] = secret_word[0]
            letters[-1] = secret_word[-1]
        word_displayed = "".join(letters)

        word_displayed = "".join(letters)
        
        print(f"Palabra: {word_displayed}")
        # Verificar si se ha adivinado la palabra completa
        if word_displayed == secret_word:
            print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
            break
else:
    print(f"¡Oh no! Has agotado tus {max_fall_attempts} intentos fallidos.")
    print(f"La palabra secreta era: {secret_word}")
