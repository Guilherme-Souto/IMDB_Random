from imdb import Cinemagoer
import random

ia = Cinemagoer()
numbers_list = []


for i in range(5):
    random_number = random.randint(1, 622384)
    numbers_list.append(random_number)

x = 1
for i in range(5):
    pick_movie = ia.get_movie(numbers_list[x-1])
    print("Nome do filme: ", pick_movie)
    year = pick_movie['year']
    print("Ano de lançamento: ", year)
    try:
        for director in pick_movie['directors']:
            print("Diretor: ", director['name'])
    except:
        print("Diretor: Não encontrado")
    print("*****")
    x += 1
