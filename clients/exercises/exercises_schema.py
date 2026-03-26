from pydantic import BaseModel, Field, ConfigDict

class ExerciseSchema(BaseModel):
    """
    Описание структуры упражнения
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class GetExercisesRequestSchema(BaseModel):
    """
    Структура запроса на получение списка упражнений
    """
    model_config = ConfigDict(populate_by_name=True)

    course_id: str = Field(alias="courseId")

class GetExercisesResponseSchema(BaseModel):
    """
    Структура ответа получения всех упражнений курса
    """
    model_config = ConfigDict(populate_by_name=True)

    exercises: list[ExerciseSchema]

class GetExerciseResponseSchema(BaseModel):
    """
    Структура ответа получения упражнения
    """
    model_config = ConfigDict(populate_by_name=True)

    exercises: ExerciseSchema

class CreateExerciseRequestSchema(BaseModel):
    """
    Структура запроса на создание упражнения
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")

class CreateExerciseResponseSchema(BaseModel):
    """
    Структура ответа создания задания
    """
    model_config = ConfigDict(populate_by_name=True)

    exercise: ExerciseSchema

class UpdateExerciseRequestSchema(BaseModel):
    """
    Структура запроса на обновление упражнения
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int | None = Field(alias="orderIndex")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")

class UpdateExerciseResponseSchema(BaseModel):
    """
    Структура ответа обновления задания
    """
    model_config = ConfigDict(populate_by_name=True)

    exercise: ExerciseSchema

