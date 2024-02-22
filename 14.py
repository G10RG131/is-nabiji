chess_players = [
    {'id': 19, 'name': 'Jobava', 'country': 'Georgia', 'rating': 2588, 'age': 41},
    {'id': 28, 'name': 'Caruana', 'country': 'USA', 'rating': 2781, 'age': 32},
    {'id': 35, 'name': 'Giri', 'country': 'Netherlands', 'rating': 2771, 'age': 30},
    {'id': 84, 'name': 'Carlsen', 'country': 'Norway', 'rating': 2864, 'age': 34},
    {'id': 118, 'name': 'Ding', 'country': 'China', 'rating': 2799, 'age': 32},
    {'id': 139, 'name': 'Karjakin', 'country': 'Russia', 'rating': 2747, 'age': 35},
    {'id': 258, 'name': 'Duda', 'country': 'Poland', 'rating': 2731, 'age': 31},
    {'id': 301, 'name': 'Vachier-Lagrave', 'country': 'France', 'rating': 2737, 'age': 34},
    {'id': 403, 'name': 'Nakamura', 'country': 'USA', 'rating': 2768, 'age': 36},
]


def create(players, path):
    file = open(path, 'w')
    for i in players:
        file.write(str(i) + '\n')
    file.close()


def read(path):
    file = open(path, 'r')
    for i in file:
        print(i)
    file.close()


def update(path, updated_row):
    file = open(path, 'r')
    file2 = open('players2.txt', 'w')
    for i in file:
        if eval(i)['id'] == updated_row["id"]:
            file2.write(str(updated_row))
            continue
        file2.write(i)
    file.close()
    file2.close()


def appened(path, new_row):
    file = open(path, 'a')
    file.write(str(new_row) + '\n')
    file.close()


new_mem = [
    {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
    {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
]

create(chess_players, 'players.txt')
read('players.txt')
update('players.txt', {'id': 19, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59})
for i in new_mem:
    appened('players.txt', i)
