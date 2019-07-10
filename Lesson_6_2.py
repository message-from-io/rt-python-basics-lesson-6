
'''
2: Создать модуль music_deserialize.py. В этом модуле открыть файлы group.json и group.pickle, прочитать из них информацию. Получить объект — словарь из предыдущего задания.
'''

from music_deserialize import read_json_file
from music_deserialize import read_pickle_file

json_file_data = read_json_file()
print('Словарь, полученный из файла group.json:')
print(json_file_data)
print(type(json_file_data))

pickle_file_data = read_pickle_file()
print('\nСловарь, полученный из файла group.pickle:')
print(pickle_file_data)
print(type(pickle_file_data))

# Результат:
#
# Словарь, полученный из файла group.json:
# {'name': 'Digital Machine', 'tracks': ['Расскажи', 'Гагарин'], 'albums': [{'name': 'Если ты со мной', 'year': 2013}, {'name': 'Не время умирать', 'year': 2006}]}
# <class 'dict'>
#
# Словарь, полученный из файла group.pickle:
# {'name': 'Digital Machine', 'tracks': ['Расскажи', 'Гагарин'], 'albums': [{'name': 'Если ты со мной', 'year': 2013}, {'name': 'Не время умирать', 'year': 2006}]}
# <class 'dict'>
