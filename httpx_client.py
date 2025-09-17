import httpx

# Инициализируем клиент
client = httpx.Client()

# Выполняем GET-запрос, используя клиент
response = client.get("http://localhost:8000/api/v1/users/me")

# Выводим ответ в консоль
print(response.text)

