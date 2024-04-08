def topscorer(players):
    max = 0
    max_name = ''
    for elem in players:
        if players[elem][0] > max:
            max = players[elem][0]
            max_name = elem
    return (max_name, max)

def most_influential(players):
    max = 0
    max_name = ''
    for elem in players:
        aux = ((players[elem][0]* 1.5)+(players[elem][1]* 1.25)+(players[elem][2]))
        if aux > max:
            max = aux
            max_name = elem
    return (max_name, max)

def average_goals(players):
    total = 0
    for elem in players:
       total = total + players[elem][0]
    return (total/25)

def average_goals_player(player):
    return (player[1]/25)