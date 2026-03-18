import json
from xml.etree.ElementTree import indent

json_data = """
{
  "name": "Lena",
  "age": 33,
  "is_student": false,
  "courses": ["Python", "QA automation", "API testing",{
    "course_name": "NewCourse"
  }],
  "address": {
    "city": "Voronezh",
    "zip": "369016"
  }
}
"""
parsed_data = json.loads(json_data) # Преобразуем JSON-строку в Python-объект (dict)

print(parsed_data['is_student'])

data = {
    'name': 'Sasha',
    'age': 33,
    'is_student': True
}
json_string = json.dumps(data, indent=4) # Преобразуем Python-объект в JSON-строку, indent добавляет отступы
print(json_string, type(json_string))


with open("json_example.json", "r", encoding="utf-8") as file:
    read_data = json.load(file) # Загружаем JSON из файла
    print(read_data)

with open("json_user.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False) # Сохраняем JSON в файл, ensure_ascii записывает кириллицу в нормальной кодировке

