def topscorer(players):
    """ Esta funcion retorna una tupla del maximo goleador del equipo. En la primera posicion esta el nombre
    y en la segunda posicion la cantidad de goles."""
    max = 0
    max_name = ''
    for elem in players:
        if players[elem][0] > max:
            max = players[elem][0]
            max_name = elem
    return (max_name, max)

def most_influential(players):
    """ Esta funcion retorna una tupla del jugador con mas influencias.En la primera posicion esta el nombre
      y en la segunda posicion la cantidad de influencias. """
    max = 0
    max_name = ''
    for elem in players:
        aux = ((players[elem][0]* 1.5)+(players[elem][1]* 1.25)+(players[elem][2]))
        if aux > max:
            max = aux
            max_name = elem
    return (max_name, max)

def average_goals(goals):
    """ Esta funcion retorna el promedio de goles por partido del equipo. """
    return (sum(goals)/25)

def average_goals_player(player):
    """ Esta funcion retorna el promedio de goles por partido de un jugador. """
    return (player[1]/25)