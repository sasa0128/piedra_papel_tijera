import random

usuario = 0
computer = 0
empates = 0
ronda = 0
while abs(computer - usuario) < 2:
    options=('piedra','papel','tijera')
    ronda += 1
    print(f"ronda {ronda}")
    user_option = input('ingrese piedra, papel o tijera ->' )
    user_option = user_option.lower()

    computer_option = random.choice(options)
    print(f"La opción del usuario es {user_option}")
    print(f"La opción de la computadora es {computer_option}")

    if user_option == computer_option:
        print('Empate')
        empates+=1
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('Piedra gana a tijera')
            print('Gana usuario!')
            usuario +=1
        else:
            print('Gana computer!')
            print('papel gana a piedra')
            computer +=1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('Papel gana a piedra')
            print('Gana usuario!')
            usuario +=1
        else:    
            print('Tijera gana a papel')
            print('Gana computer!')
            computer +=1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('Tijera gana a papel')
            print('Gana usuario!')
            usuario +=1
        else:    
            print('Piedra gana a tijera')
            print('Gana computer!')
            computer +=1
    print (f"El puntaje del usuario es {usuario}")
    print (f"El puntaje del computer es {computer}")
    print (f"El número de empates es {empates}")
    print("*"*10)


if usuario > computer: 
    print("El ganador es usuario") 
else:
    print("El ganador es computer") 



