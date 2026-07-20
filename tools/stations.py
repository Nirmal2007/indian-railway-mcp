"""Get details based on stations."""

from api.railradar import make_request

def get_all_station_kvs():
    """Fetch all station key value pairs."""

    endpoint = (
        f"/v1/legacy/stations/all-kvs"
    )

    return make_request(endpoint)

def get_live_station_board(
    station_code: str,
    hours: int | None = None,
    isIntermediate: bool | None = None,
):
    """
    Fetch the live station board.

    Parameters
    ----------
    station_code : Railway station code
    hours : Number of hours ahead to include.
    isIntermediate : Include pass-through (non-halting) trains.
    """

    endpoint = f"/app/v1/stations/{station_code}/live"

    params = []

    if hours is not None:
        params.append(f"hours={hours}")

    if isIntermediate is not None:
        params.append(
            f"includeIntermediate={str(isIntermediate).lower()}"
        )

    if params:
        endpoint += "?" + "&".join(params)

    return make_request(endpoint)

def get_station_board(
    station_code: str,
    to_station_code: str | None = None
):
    """Fetch station board.All trains that stop at a station with scheduled times. Use `includeIntermediate=true` to also include pass-through trains."""

    endpoint = (
        f"/app/v1/stations/"
        f"{station_code}/trains"
    )

    if to_station_code:
        endpoint += (
            f"&toStationCode={to_station_code}"
        )

    return make_request(endpoint)
