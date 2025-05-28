from pydantic import BaseModel, Field


class Category(BaseModel):
    """A Ximmio category.

    The purpose of this model is not entirely clear to me, yet. And like
    the other models that were added up until now, this one is missing a
    lot of fields, because I haven't seen any data in them yet.
    """

    id: int = Field(alias="ID")
    company_id: int = Field(alias="companyID")
    external_id: int = Field(alias="ExternalID")
    name: str = Field(alias="categoryName")
    report_type: str = Field(alias="reportType")
    is_citizen: bool = Field(alias="IsCitizen")
