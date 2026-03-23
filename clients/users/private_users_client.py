from httpx import Response
from clients.api_client import APIClient


class PrivateUsersClient(APIClient):
    def get_user_me_api(self) -> Response:
        return self.get

