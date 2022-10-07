players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}


def get_new_dict_players_1(dict_players):
    return [last_first_name + points for last_first_name, points in dict_players.items()]
