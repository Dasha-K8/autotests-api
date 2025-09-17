# создаем пользователя
import httpx #создание пользователя с тестовы данными

from tools.fakers import get_random_email

create_user_payload = {
 "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)

# Проверяем, что пользователь успешно создан
if create_user_response.status_code == 201:  # или 200, если сервер так возвращает
    create_user_data = create_user_response.json()
    user_id = create_user_data['user']['id']

    # Теперь можно безопасно делать логин
    login_payload = {
        "email": create_user_payload["email"],
        "password": create_user_payload["password"]
    }
    login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)

    if login_response.status_code == 200:
        login_data = login_response.json()
        access_token = login_data["token"]["accessToken"]

        # Теперь можно обновлять пользователя
        update_user_payload = {
            "email": get_random_email(),
            "lastName": "string",
            "firstName": "string",
            "middleName": "string"
        }
        headers = {"Authorization": f"Bearer {access_token}"}
        update_response = httpx.patch(
            f"http://localhost:8000/api/v1/users/{user_id}",
            json=update_user_payload,
            headers=headers
        )
        print(update_response.status_code, update_response.json())

    else:
        print("Ошибка при логине")
else:
    print("Ошибка при создании пользователя")
