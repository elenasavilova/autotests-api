from httpx import Response
from typing import TypedDict

from clients.api_client import APIClient


class GetExercisesRequest(TypedDict):
    """
    Структура запроса на получение списка упражнений
    """
    courseId: str


class CreateExerciseRequest(TypedDict):
    """
    Структура запроса на создание упражнения
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExerciseRequest(TypedDict):
    """
    Структура запроса на обновление упражнения
    """
    title: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesRequest) -> Response:
        """
        Метод для получения списка упражнений для конкретного курса
        :param query: словарь с courseId
        :return: ответ от сервера в виде httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения информации об упражнении
        :param exercise_id: идентификатор упражнения
        :return: ответ от сервера в виде httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequest) -> Response:
        """
        Метод создания упражнения
        :param request: словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: ответ от сервера в виде httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequest) -> Response:
        """
        Метод обновления упражнения
        :param exercise_id: идентификатор упражнения
        :param request: словарь с title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: ответ от сервера в виде httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения
        :param exercise_id: идентификатор упражнения
        :return: ответ от сервера в виде httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")
