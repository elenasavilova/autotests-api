from typing import Any
from jsonschema import validate
from jsonschema.validators import Draft202012Validator

def validate_json_schema(instance: Any, schema: dict) -> None:
    """
    Проверяет, соответствует ли json-объект (instance) заданной json схеме (schema)
    :param instance: JSON-данные, которые нужно проверить
    :param schema: ожидаемая JSON-schema
    :raises jsonschema.exceptions.ValidationError: если instance не соответствует schema.
    """
    validate(
        instance=instance,
        schema=schema,
        format_checker=Draft202012Validator.FORMAT_CHECKER # валидирует форматы полей
    )