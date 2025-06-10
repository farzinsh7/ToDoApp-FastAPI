from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class TodoBaseSchema(BaseModel):
    title: str = Field(..., max_length=150, description="Title of the todo")
    description: Optional[str] = Field(
        None, max_length=500, description="Description of the todo"
    )
    is_completed: bool = Field(defauld=False, description="States of the todo")   
    priority: int = Field(..., description="Priority of the todo")


class TodoCreateSchema(TodoBaseSchema):
    pass


class TodoUpdateSchema(TodoBaseSchema):
    pass


class TodoResponseSchema(TodoBaseSchema):
    id: int = Field(..., description="Unique identifier of object")
    created_date: datetime = Field(
        ..., description="Creation date and time of time object"
    )
    updated_date: datetime = Field(
        ..., description="Updating date and time of time object"
    )
