
'''
6.1. Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой музыкальной группы, например:

music_band = {
    ‘name’: ‘Г.М.О.’,
    ‘tracks’: [‘Последний месяц осени’, ‘Шапито’],
    ‘Albums’: [{‘name’: ‘Делать панк-рок’,‘year’: 2016},
    {‘name’: ‘Шапито’,‘year’: 2014}]
}

С помощью модулей json и pickle сериализовать данный словарь в json и в байты, вывести результаты в терминал. Записать результаты в файлы group.json, group.pickle соответственно. В файле group.json указать кодировку utf-8.
'''

# В модуле music_serialize.py создан только словарь с данными. Все операции над ним производятся в текущем модуле

import pickle, json
from music_serialize import music_band

print('Исходный словарь:')
print(music_band)
print(type(music_band))

# Сериализовать словарь в формат JSON
band_json = json.dumps(music_band)
print('\nСловарь в формате JSON:')
print(band_json)
print(type(band_json))

# Сериализовать словарь в формат строк байтов
band_pickle = pickle.dumps(music_band)
print('\nСловарь в формате строк байтов:')
print(band_pickle)
print(type(band_pickle))

# Записать в файл словарь в формате JSON
with open('group.json', 'w', encoding='utf-8') as f:
    json.dump(music_band, f)

# Записать в файл словарь в формате строк байтов
with open('group.pickle', 'wb') as f:
    pickle.dump(music_band, f)

# Результат:
#
# Исходный словарь:
# {'name': 'Digital Machine', 'tracks': ['Расскажи', 'Гагарин'], 'albums': [{'name': 'Если ты со мной', 'year': 2013}, {'name': 'Не время умирать', 'year': 2006}]}
# <class 'dict'>
#
# Словарь в формате JSON:
# {"name": "Digital Machine", "tracks": ["\u0420\u0430\u0441\u0441\u043a\u0430\u0436\u0438", "\u0413\u0430\u0433\u0430\u0440\u0438\u043d"], "albums": [{"name": "\u0415\u0441\u043b\u0438 \u0442\u044b \u0441\u043e \u043c\u043d\u043e\u0439", "year": 2013}, {"name": "\u041d\u0435 \u0432\u0440\u0435\u043c\u044f \u0443\u043c\u0438\u0440\u0430\u0442\u044c", "year": 2006}]}
# <class 'str'>
#
# Словарь в формате строк байтов:
# b'\x80\x03}q\x00(X\x04\x00\x00\x00nameq\x01X\x0f\x00\x00\x00Digital Machineq\x02X\x06\x00\x00\x00tracksq\x03]q\x04(X\x10\x00\x00\x00\xd0\xa0\xd0\xb0\xd1\x81\xd1\x81\xd0\xba\xd0\xb0\xd0\xb6\xd0\xb8q\x05X\x0e\x00\x00\x00\xd0\x93\xd0\xb0\xd0\xb3\xd0\xb0\xd1\x80\xd0\xb8\xd0\xbdq\x06eX\x06\x00\x00\x00albumsq\x07]q\x08(}q\t(h\x01X\x1b\x00\x00\x00\xd0\x95\xd1\x81\xd0\xbb\xd0\xb8 \xd1\x82\xd1\x8b \xd1\x81\xd0\xbe \xd0\xbc\xd0\xbd\xd0\xbe\xd0\xb9q\nX\x04\x00\x00\x00yearq\x0bM\xdd\x07u}q\x0c(h\x01X\x1e\x00\x00\x00\xd0\x9d\xd0\xb5 \xd0\xb2\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd1\x83\xd0\xbc\xd0\xb8\xd1\x80\xd0\xb0\xd1\x82\xd1\x8cq\rh\x0bM\xd6\x07ueu.'
# <class 'bytes'>
