from pydantic import BaseModel, Field


class CompanyInfo(BaseModel):
    main_color: str = Field(alias="mainColor")
    """The company's primary color.

    The color is formatted as a hexadecimal number, and includes a
    leading hash, e.g. '#ffffff'.
    """
    color_1: str = Field(alias="color1")
    """The company's first color.

    The color is formatted as a hexadecimal number, and includes a
    leading hash, e.g. '#ffffff'.
    """
    color_2: str = Field(alias="color1")
    """The company's second color.

    The color is formatted as a hexadecimal number, and includes a
    leading hash, e.g. '#ffffff'.
    """
    color_3: str = Field(alias="color1")
    """The company's third color.

    The color is formatted as a hexadecimal number, and includes a
    leading hash, e.g. '#ffffff'.
    """
    code: str = Field(alias="companyCode")
    name: str = Field(alias="companyName")
    short_name: str = Field(alias="companyShortName")
    logo: str = Field(alias="logo")
