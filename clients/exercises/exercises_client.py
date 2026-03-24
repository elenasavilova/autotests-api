from httpx import Response
from typing import TypedDict

from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict
from clients.users.private_users_client import get_private_users_client


class Exercise(TypedDict):
    """
    Описание структуры упражнения
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExercisesRequest(TypedDict):
    """
    Структура запроса на получение списка упражнений
    """
    courseId: str

class GetExercisesResponseDict(TypedDict):
    """
    Структура ответа получения всех упражнений курса
    """
    exercises: list[Exercise]

class GetExerciseResponseDict(TypedDict):
    """
    Структура ответа получения упражнения
    """
    exercises: Exercise

class CreateExerciseRequestDict(TypedDict):
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

class CreateExerciseResponseDict(TypedDict):
    """
    Структура ответа создания задания
    """
    exercise: Exercise

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

class UpdateExerciseResponseDict(TypedDict):
    """
    Структура ответа обновления задания
    """
    exercise: Exercise

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

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
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

    def get_exercises(self, query: GetExercisesRequest) -> GetExercisesResponseDict:
        """
        Метод, инициализирующий получение всех упражнений курса
        :return: ответ от сервера со списком всех упражнений
        """
        response = self.get_exercises_api(query)
        return response.json()

    def get_exercise(self, exercise_id: str):
        """
        Метод, инициализирующий получение упражнения
        :return: запрос от сервера в виде
        """
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExerciseResponseDict:
        """
        Метод, инициализирующий создание упражнения
        :return: ответ от сервера в виде CreateExerciseResponseDict
        """
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequest) -> UpdateExerciseResponseDict:
        """
        Метод, инициализирующий обновление упражнения
        :return: ответ от сервера в виде UpdateExerciseResponseDict
        """
        response = self.update_exercise_api(exercise_id, request)
        return response.json()

    # Не совсем поняла, нужно ли что-то делать с методом delete
    # def delete_exercise(self, exercise_id: str) -> Response:
    #     response = self.delete_exercise_api(exercise_id)
    #     return response.json()

def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_users_client(user))
