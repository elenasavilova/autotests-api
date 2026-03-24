from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

from clients.files.files_client import File
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client
from clients.users.public_users_client import User


class Course(TypedDict):
    """
    Описание структуры курса
    """
    id: str
    title: str
    maxScore: int
    minScore: int
    description: str
    previewFile: File
    estimatedTime: str
    createdByUser: User


class GetCoursesQueryDict(TypedDict):
    """
    Структура запроса на получение списка курсов
    """
    userId: str

class CreateCourseRequestDict(TypedDict):
    """
    Структура запроса на создание курса
    """
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str


class CreateCourseResponseDict(TypedDict):
    """
    Описание структуры ответа создания курса
    """
    course: Course

class UpdateCourseRequestDict(TypedDict):
    """
    Структура запроса на обновление курса
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None

class CoursesClient(APIClient):
    """
    Клиент для работы с /api/v1/courses
    """
    def get_courses_api(self, query: GetCoursesQueryDict) -> Response:
        """
        Метод получения списка курсов
        :param query: словарь с userId
        :return: ответ от сервера в виде httpx.Response
        """
        return self.get("/api/v1/courses", params=query)

    def get_course_api(self, course_id: str) -> Response:
        """
        Метод получения курса
        :param course_id: идентификатор курса
        :return: ответ от сервера в виде httpx.Response
        """
        return self.get(f"/api/v1/courses/{course_id}")

    def create_course_api(self, request: CreateCourseRequestDict) -> Response:
        """
        Метод создания курса
        :param request: словарь с title, maxScore, minScore, description, estimatedTime, previewFileId, createdByUserId
        :return: ответ от сервера в виде httpx.Response
        """
        return self.post(f"/api/v1/courses", json=request)

    def update_course_api(self, course_id: str, request: UpdateCourseRequestDict) -> Response:
        """
        Метод обновления курса
        :param course_id: идентификатор курса
        :param request: словарь с title, maxScore, minScore, description, estimatedTime
        :return: ответ от сервера в виде httpx.Response
        """
        return self.patch(f"/api/v1/courses/{course_id}", json=request)

    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод удаления курса
        :param course_id: идентификатор курса
        :return: ответ от сервера в виде httpx.Response
        """
        return self.delete(f"/api/v1/courses/{course_id}")

    def create_course(self, request: CreateCourseRequestDict) -> CreateCourseResponseDict:
        """
        Метод, инициализирующий создание курса
        :return: ответ от сервера в формате CreateCourseResponseDict
        """
        response = self.create_course_api(request)
        return response.json()

def get_courses_client(user: AuthenticationUserDict) -> CoursesClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию CoursesClient.
    """
    return CoursesClient(client=get_private_http_client(user))