"""Get details based on stations."""

from api.railradar import make_request


def search_stations(query: str):
    """Search stations by query."""

    endpoint = (
        f"/api/v1/search/stations"
        f"?query={query}"
    )

    return make_request(endpoint)


def get_station_info(station_code: str):
    """Fetch station information."""

    endpoint = (
        f"/api/v1/stations/"
        f"{station_code}/info"
    )

    return make_request(endpoint)


def get_live_station_board(
    station_code: str,
    hours: int,
    to_station_code: str | None = None
):
    """Fetch live station board."""

    endpoint = (
        f"/api/v1/stations/"
        f"{station_code}/live"
        f"?hours={hours}"
    )

    if to_station_code:
        endpoint += (
            f"&toStationCode={to_station_code}"
        )

    return make_request(endpoint)
