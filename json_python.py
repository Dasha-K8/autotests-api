import json

json_data = '{"name": "Иван", "age": 30, "is_student": false}'
parsed_data = json.loads(json_data) # прееобразование с json на питон
print(parsed_data, type(parsed_data)) # класс dict структура словаря


data = {
"name": "Мария",
  "age": 25,
  "is_student": True,
}
json_string = json.dumps(data, indent=4) # обратно + отступ
print(json_string, type(json_string)) # класс строка

# читаем из json файла
with open("json_example.json", "r", encoding="utf-8") as file: # r для чтения, Encoding="utf-8" означает, что текст на странице кодируется в формате UTF-8
    read_data = json.load(file) # загружаем из файла json
    print(read_data)

with open  ("json_user.json", "w", encoding="utf-8") as file: # записываем в файл json_user данные
    json.dump(data, file, indent=2, ensure_ascii=False) # отображает вместо кодировки имя
