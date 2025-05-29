from datetime import datetime

from pydantic import BaseModel, Field


class Calendar(BaseModel):
    """A list of pickup dates for a specific waste type."""

    pickup_dates: list[datetime] = Field(alias="pickupDates")
    pickup_type: int = Field(alias="pickupType")
    pickup_type_text: str = Field(alias="_pickupTypeText")
    description: str
