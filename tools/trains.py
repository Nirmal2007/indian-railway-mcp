"""Get details based on trains."""

from api.railradar import make_request


def all_trains():
    """Fetch all available trains."""

    endpoint = "/api/v1/trains/all-kvs"

    return make_request(endpoint)


def trains_between(from_station: str, to_station: str):
    """Fetch trains between two stations."""

    endpoint = (
        f"/api/v1/trains/between"
        f"?from={from_station}"
        f"&to={to_station}"
    )

    return make_request(endpoint)


def train_list(
    page: int = 1,
    limit: int = 50,
    train_type: str = "",
    zone: str = "",
    search: str = "",
):
    """Fetch paginated train list."""

    endpoint = (
        f"/api/v1/trains/list"
        f"?page={page}"
        f"&limit={limit}"
        f"&type={train_type}"
        f"&zone={zone}"
        f"&search={search}"
    )

    return make_request(endpoint)


def live_map():
    """Fetch live train map."""

    endpoint = "/api/v1/trains/live-map"

    return make_request(endpoint)


def train_data(
    train_number: str,
    journey_date: str = "",
    data_type: str = "full",
    data_provider: str = "railradar",
):
    """Fetch detailed train data."""

    endpoint = (
        f"/api/v1/trains/{train_number}"
        f"?journeyDate={journey_date}"
        f"&dataType={data_type}"
        f"&dataProvider={data_provider}"
    )

    return make_request(endpoint)


def average_delay(train_number: str):
    """Fetch average delay for a train."""

    endpoint = (
        f"/api/v1/trains/"
        f"{train_number}/average-delay"
    )

    return make_request(endpoint)


def train_instances(
    train_number: str,
    data_provider: str = "railradar"
):
    """Fetch train instances."""

    endpoint = (
        f"/api/v1/trains/"
        f"{train_number}/instances"
        f"?dataProvider={data_provider}"
    )

    return make_request(endpoint)


def train_schedule(
    train_number: str,
    journey_date: str
):
    """Fetch train schedule."""

    endpoint = (
        f"/api/v1/trains/"
        f"{train_number}/schedule"
        f"?journeyDate={journey_date}"
    )

    return make_request(endpoint)
