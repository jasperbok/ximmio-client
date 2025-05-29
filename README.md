# ximmio-client

A Python client for Ximmio's Waste API.

## Usage

```python
from ximmio_client import Client

# Create a Client instance.
client = Client(
    "foo",
    house_number=1,
    postal_code="1234AB",
)

# Now you can call methods on it.
calendar = client.get_calendar()
```