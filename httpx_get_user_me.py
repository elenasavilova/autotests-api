import httpx

# Отправить POST запрос к /api/v1/authentication/login
login_payload = {
    "email": "lena@example.com",
    "password": "lena"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print(f"Login response: {login_response_data}")
print(f"Status code: {login_response.status_code}")

# Отправить GET запрос к /api/v1/users/me
get_header = f"Bearer {login_response_data['token']['accessToken']}" # формируем заголовок

me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers={"Authorization": get_header})
me_response_data = me_response.json()

print(f"Get user me response: {me_response_data}")
print(f"Status code: {me_response.status_code}")



