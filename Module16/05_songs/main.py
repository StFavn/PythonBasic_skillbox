def found_song(songs_list, the_song):
    for song in songs_list:
        if the_song == song[0]:
            return True
    return False


def get_new_list(violator_songs_list):
    new_list = []
    num_songs = int(input('Сколько песен выбрать? '))
    for i in range(1, num_songs + 1):
        a_song = input(f'Название {i}-й песни: ')
        if found_song(violator_songs_list, a_song):
            new_list.append(a_song)
        else:
            print('У нас нет песни: ' + a_song)
    return new_list


def how_many_time(violator_songs_list, new_list):
    duration = 0
    for right_song in new_list:
        for song in violator_songs_list:
            if right_song == song[0]:
                duration += song[1]
                break
    return duration


violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

new_list_songs = get_new_list(violator_songs)
duration_songs = round(how_many_time(violator_songs, new_list_songs), 2)
print(f'\nОбщее время звучания песен: {duration_songs} минуты')
