import httpx  # Импортируем библиотеку HTTPX

# 1. Данные для входа в систему
login_payload = {
    "email": "user@example.com",   # замени на своего пользователя
    "password": "string"           # замени на свой пароль
}

# 2. Выполняем POST-запрос для аутентификации
login_response = httpx.post(
    "http://localhost:8000/api/v1/authentication/login",
    json=login_payload
)

print("=== Login Response ===")
print("Status code:", login_response.status_code)
print("Body:", login_response.json())

# 3. Достаём accessToken из ответа
access_token = login_response.json()["token"]["accessToken"]

# 4. Формируем заголовки с токеном
headers = {"Authorization": f"Bearer {access_token}"}

# 5. Выполняем GET-запрос к эндпоинту /users/me
user_response = httpx.get(
    "http://localhost:8000/api/v1/users/me",
    headers=headers
)

print("\n=== User Info Response ===")
print("Status code:", user_response.status_code)
print("Body:", user_response.json())

#ответ преподователя
import httpx

login_payload = {
    "email": "user@example.com",
    "password": "string"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

get_user_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}
get_user_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=get_user_headers)
get_user_response_data = get_user_response.json()

# Выводим обновленные токены
print("Get user response:", get_user_response_data)
print("Get user status code:", get_user_response.status_code)

