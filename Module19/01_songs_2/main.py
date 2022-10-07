violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

my_songs = [input(f'Название {i}-й песни: ') for i in range(1, 1 + int(input('Сколько песен выбрать? ')))]
songs_duration = [violator_songs.get(my_songs[i], 0) for i in range(len(my_songs))]

print('\nОбщее время звучания песен:', round(sum(songs_duration), 2), 'минуты.')

if 0 in songs_duration:
    print(', '.join([my_songs[i] for i in range(len(my_songs)) if my_songs[i] not in violator_songs]), 'нет в наличии.')
