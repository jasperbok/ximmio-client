from datetime import date

from pydantic import BaseModel, Field


class CalendarSettings(BaseModel):
    end_date: date = Field(alias="CalendarEndDate")
    web_url: str = Field(alias="CalendarPageUrl")
    main_color: str = Field(alias="MainColor")
    """The calendar's primary color.

    The color is formatted as a hexadecimal number, and includes a
    leading hash, e.g. '#ffffff'.
    """
    sub_color: str = Field(alias="SubColor")
    """The calendar's secondary color.

    The color is formatted as a hexadecimal number, and includes a
    leading hash, e.g. '#ffffff'."""
    register_server_notifications: bool = Field(alias="RegisterServerNotifications")
    show_waste_text_info: bool = Field(alias="ShowWasteTextInfo")
    weeknumbers: bool = Field(alias="WeekNumbers")
