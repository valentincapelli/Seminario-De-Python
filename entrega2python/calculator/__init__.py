def topscorer(players):
    max = 0
    max_name = ''
    for elem in players:
        if players[elem][0] > max:
            max = players[elem][0]
            max_name = elem
    return (max_name, max)