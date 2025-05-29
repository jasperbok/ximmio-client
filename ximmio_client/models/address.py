from __future__ import annotations

from pydantic import BaseModel, Field


class Address(BaseModel):
    """An address as returned by Ximmio.

    The following fields that are returned from the API are missing on
    this model, as I haven't seen the kind of data they contain, and I
    currently don't see their usefulness.

    - ID
    - HouseNumberIndication
    - HouseNumberAddition
    - BuildingCategory
    """

    unique_id: str = Field(alias="UniqueId")
    street: str = Field(alias="Street")
    house_number: str = Field(alias="HouseNumber")
    house_letter: str | None = Field(alias="HouseLetter", default="")
    postal_code: str = Field(alias="ZipCode")
    city: str = Field(alias="City")
    community: str = Field(alias="Community")
