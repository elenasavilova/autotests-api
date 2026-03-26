from httpx import Response
from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from clients.exercises.exercises_schema import (GetExercisesRequestSchema, CreateExerciseRequestSchema,
                                                UpdateExerciseRequestSchema, GetExercisesResponseSchema,
                                                CreateExerciseResponseSchema, UpdateExerciseResponseSchema)


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesRequestSchema) -> Response:
        """
        Метод для получения списка упражнений для конкретного курса
        :param query: словарь с courseId
        :return: ответ от сервера в виде httpx.Response
        """
        return self.get("/api/v1/exercises", params=query.model_dump(by_alias=True))

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения информации об упражнении
        :param exercise_id: идентификатор упражнения
        :return: ответ от сервера в виде httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Метод создания упражнения
        :param request: словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: ответ от сервера в виде httpx.Response
        """
        return self.post("/api/v1/exercises", json=request.model_dump(by_alias=True))

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """
        Метод обновления упражнения
        :param exercise_id: идентификатор упражнения
        :param request: словарь с title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: ответ от сервера в виде httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request.model_dump(by_alias=True))

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения
        :param exercise_id: идентификатор упражнения
        :return: ответ от сервера в виде httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercises(self, query: GetExercisesRequestSchema) -> GetExercisesResponseSchema:
        """
        Метод, инициализирующий получение всех упражнений курса
        :return: ответ от сервера со списком всех упражнений
        """
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def get_exercise(self, exercise_id: str):
        """
        Метод, инициализирующий получение упражнения
        :return: запрос от сервера в виде
        """
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        """
        Метод, инициализирующий создание упражнения
        :return: ответ от сервера в виде CreateExerciseResponseDict
        """
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> UpdateExerciseResponseSchema:
        """
        Метод, инициализирующий обновление упражнения
        :return: ответ от сервера в виде UpdateExerciseResponseDict
        """
        response = self.update_exercise_api(exercise_id, request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)

    # Не совсем поняла, нужно ли что-то делать с методом delete
    # def delete_exercise(self, exercise_id: str) -> Response:
    #     response = self.delete_exercise_api(exercise_id)
    #     return response.json()

def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
