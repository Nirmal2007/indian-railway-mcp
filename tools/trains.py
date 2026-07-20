"""Get details based on trains."""

from api.railradar import make_request


def all_trains():
    """Fetch all available trains with name and train numbers."""

    endpoint = "/app/v1/lookup/trains"

    return make_request(endpoint)


def trains_between(from_station: str, to_station: str , date: str):
    """Fetch trains between two stations on a date."""

    endpoint = (
        f"/app/v1/trains/between"
        f"/{from_station}"
        f"/{to_station}"
    )

    if date:
        endpoint += f"?date={date}"

    return make_request(endpoint)

def trains_between_type(
    from_station: str,
    to_station: str,
    date: str = None,
    train_type: str = None,
    category: str = None,
):
    """
    Fetch trains between two stations.

    Optional filters:
    - date (YYYY-MM-DD)
    - train_type (vande-bharat, rajdhani, express, local)
    - category (Local, Express, Premium, Special)
    """

    endpoint = f"/app/v1/trains/between/{from_station}/{to_station}"

    params = []

    if date:
        params.append(f"date={date}")

    if train_type:
        params.append(f"type={train_type}")

    if category:
        params.append(f"category={category}")

    if params:
        endpoint += "?" + "&".join(params)

    return make_request(endpoint)


def train_data(
    train_number: str,
):
    """Fetch detailed train data."""

    endpoint = (
        f"/app/v1/trains/{train_number}"
    )

    return make_request(endpoint)


def average_delay(train_number: str):
    """Fetch average delay for a train."""

    endpoint = (
        f"/app/v1/legacy/trains"
        f"/{train_number}"
    )

    return make_request(endpoint)


def train_live_status(
    train_number: str,
):
    """Fetch live train status and locations."""

    endpoint = (
        f"/app/v1/trains/"
        f"{train_number}/live"
    )

    return make_request(endpoint)


def train_schedule(
    train_number: str,
    journey_date: str
):
    """Fetch train schedule on a particular date."""

    endpoint = (
        f"/app/v1/trains/{train_number}?journeyDate={journey_date}"
    )

    return make_request(endpoint)
