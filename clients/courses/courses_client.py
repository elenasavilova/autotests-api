from clients.api_client import APIClient
from httpx import Response
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from clients.courses.courses_schema import (GetCoursesQuerySchema, CreateCourseRequestSchema, CreateCourseResponseSchema,
                                            UpdateCourseRequestSchema)


class CoursesClient(APIClient):
    """
    Клиент для работы с /api/v1/courses
    """
    def get_courses_api(self, query: GetCoursesQuerySchema) -> Response:
        """
        Метод получения списка курсов
        :param query: словарь с userId
        :return: ответ от сервера в виде httpx.Response
        """
        return self.get("/api/v1/courses", params=query.model_dump(by_alias=True))

    def get_course_api(self, course_id: str) -> Response:
        """
        Метод получения курса
        :param course_id: идентификатор курса
        :return: ответ от сервера в виде httpx.Response
        """
        return self.get(f"/api/v1/courses/{course_id}")

    def create_course_api(self, request: CreateCourseRequestSchema) -> Response:
        """
        Метод создания курса
        :param request: словарь с title, maxScore, minScore, description, estimatedTime, previewFileId, createdByUserId
        :return: ответ от сервера в виде httpx.Response
        """
        return self.post(f"/api/v1/courses", json=request.model_dump(by_alias=True))

    def update_course_api(self, course_id: str, request: UpdateCourseRequestSchema) -> Response:
        """
        Метод обновления курса
        :param course_id: идентификатор курса
        :param request: словарь с title, maxScore, minScore, description, estimatedTime
        :return: ответ от сервера в виде httpx.Response
        """
        return self.patch(f"/api/v1/courses/{course_id}", json=request.model_dump(by_alias=True)) # превращает
        # модель в обычный dict

    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод удаления курса
        :param course_id: идентификатор курса
        :return: ответ от сервера в виде httpx.Response
        """
        return self.delete(f"/api/v1/courses/{course_id}")

    def create_course(self, request: CreateCourseRequestSchema) -> CreateCourseResponseSchema:
        """
        Метод, инициализирующий создание курса
        :return: ответ от сервера в формате CreateCourseResponseSchema
        """
        response = self.create_course_api(request)
        return CreateCourseResponseSchema.model_validate_json(response.text)

def get_courses_client(user: AuthenticationUserSchema) -> CoursesClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию CoursesClient.
    """
    return CoursesClient(client=get_private_http_client(user))