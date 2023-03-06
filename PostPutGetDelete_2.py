"""Вариант #2"""

import requests
import json

base_url = 'https://petstore.swagger.io/v2/pet/'
headers = {'accept': 'application/json', 'Content-Type': 'application/json'}


def add_modify(id_pet, info_pet):
    """Функция добавления нового животного / изменения информации о новом животном:"""
    data = json.dumps(info_pet)
    if id_pet == 0:
        info_mess = "Создано новое животное   : "
        res = requests.post(base_url, headers=headers, data=data)
    else:
        info_mess = "Изменено новое животное  : "
        res = requests.put(base_url, headers=headers, data=data)
    try:
        result = res.json()
        id_new_pet = result.get('id')
    except:
        result = res.text
        id_new_pet = int(result.split(':')[1].split(',')[0])
    finally:
        print(f"{info_mess} {result}\nСтатус код: {res.status_code}\n" + '-' * 200)

    return id_new_pet


def get_delete(id_pet, get_del_message):
    """Функция просмотра / удаления нового животного:"""
    if get_del_message == "Удаление животного: ":
        res = requests.delete(f"https://petstore.swagger.io/v2/pet/{id_pet}")
    else:
        res = requests.get(f"https://petstore.swagger.io/v2/pet/{id_pet}")

    print(f"{get_del_message} {res.json()}\nСтатус код: {res.status_code}\n" + '-' * 200)


# POST-request, Add a new pet to the store:
#
new_pet = {
  "id": 0,
  "category": {"id": 0, "name": "cat"},
  "name": "Murzik",
  "photoUrls": ["cat_foto"],
  "tags": [{"id": 0, "name": "cat"}],
  "status": "available"
}

id_new_pet = add_modify(0, new_pet)


# PUT-request, Modify information about new pet:
#
modified_pet = {
  "id": id_new_pet,
  "category": {"id": 0, "name": "кошка"},
  "name": "Мурзик",
  "photoUrls": ["https://prnt.sc/6Eiz5jBK456u"],
  "tags": [{"id": 0, "name": "кот"}],
  "status": "sold"
}

id_new_pet = add_modify(id_new_pet, modified_pet)


# GET-request, Find pet by ID:
#
get_delete(id_new_pet, "Просмотр нового животного: ")


# DELETE-request, Delete a pet by ID:
#
get_delete(id_new_pet, "Удаление нового животного: ")
