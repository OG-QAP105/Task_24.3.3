"""Вариант #1"""

import requests
import json

base_url = 'https://petstore.swagger.io/v2/pet/'
headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
id_new_pet = 0

# POST-request, Add a new pet to the store:
#
new_pet = {
  "id": id_new_pet,
  "category": {"id": 0, "name": "cat"},
  "name": "Murzik",
  "photoUrls": ["cat_foto"],
  "tags": [{"id": 0, "name": "cat"}],
  "status": "available"
}

data_post = json.dumps(new_pet)

res = requests.post(base_url, headers=headers, data=data_post)
try:
    result = res.json()
    id_new_pet = result.get('id')
except:
    result = res.text
    id_new_pet = int(result.split(':')[1].split(',')[0])
finally:
    print("-"*200 + f"\nСоздано новое животное: {result}\nСтатус код: {res.status_code}\n" + '-' * 200)


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

data_put = json.dumps(modified_pet)

res = requests.put(base_url, headers=headers, data=data_put)
try:
    result = res.json()
except:
    result = res.text
    id_modified_pet = int(result.split(':')[1].split(',')[0])
finally:
    print(f"Новое животное изменено: {result}\nСтатус код: {res.status_code}\n" + '-' * 200)

# GET-request, Find pet by ID:
#
res = requests.get(f"https://petstore.swagger.io/v2/pet/{id_new_pet}")
print(f"Просмотр животного: {res.json()}\nСтатус код: {res.status_code}\n" + '-'*200)

# DELETE-request, Delete a pet by ID:
#
res = requests.delete(f"https://petstore.swagger.io/v2/pet/{id_new_pet}")
print(f"Удаление животного: {res.json()}\nСтатус код: {res.status_code}\n" + '-'*200)
