from typing import Sequence
from pydantic import BaseModel, ValidationError, Field, field_validator


class CityModel(BaseModel):
    name: str = Field(
        alias='cityFullName', # "переименование" ключа прилетевшего json в name python переменную
    )

    @field_validator("name")
    def name_valid(self, name: str) -> str: # узнать подробнее
        """Check feild 'name'"""
        if isinstance(name, str):
            raise ValueError(f"Invalid city name: {name}")
        return name

