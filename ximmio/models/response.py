from pydantic import BaseModel, Field


class Response(BaseModel):
    """The response structure of the Waste API.

    This model is missing a lot of fields that are returned by the API.
    """

    data_list: list[dict] = Field(alias="dataList")
    status: bool
    message_code: int = Field(alias="messageCode")
