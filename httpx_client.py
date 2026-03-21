import httpx

login_payload = {
    "email": "test.1774099145.4306011@example.com",
    "password": "string"
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print(f"Login data: {login_response_data}")
print(f"Login status code: {login_response.status_code}")

client = httpx.Client(
    base_url="http://localhost:8000",
    timeout=100,
    headers={"Authorization": f"Bearer {login_response_data["token"]['accessToken']}"},
)

get_user_me_response = client.get("/api/v1/users/me")
get_user_me_respons_data = get_user_me_response.json()
print("Get user me data: ", get_user_me_respons_data)
