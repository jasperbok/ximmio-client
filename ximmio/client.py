import httpx

from .models import Address, Category, Response


API_BASE_URL = "https://wasteapi.ximmio.com/api"


class Client:
    """The Ximmio Waste API client."""

    company_code: str
    address: Address | None = None

    def __init__(self, company_code: str, house_number: int, postal_code: str) -> None:
        self.company_code = company_code
        self.address = self.get_address(house_number, postal_code)

    def get_address(self, house_number: int, postal_code: str) -> Address:
        """Return the full address that belongs to the postal code and house number."""
        resp = httpx.post(
            f"{API_BASE_URL}/GetAddress",
            json={
                "companyCode": self.company_code,
                "houseNumber": house_number,
                "postCode": postal_code,
            },
        )
        resp.raise_for_status()

        response = Response.model_validate(resp.json())

        return Address.model_validate(response.data_list[0])

    def get_categories(self) -> list[Category]:
        resp = httpx.post(
            f"{API_BASE_URL}/ListCategories",
            json={
                "community": self.address.community,
                "companyCode": self.company_code,
                "reportType": "WASTEABC",
            },
        )
        resp.raise_for_status()

        response = Response.model_validate(resp.json())

        return [Category.model_validate(d) for d in response.data_list]
