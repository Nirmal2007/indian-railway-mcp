"Gives a live Indian-Railway train map."

from api.railradar import make_request


def live_map(
    number: str,
    response_format: str | None = None,
    stops: bool | None = None,
):
    """
    Returns the route geometry for a train (map coordinates).
    """

    endpoint = f"/app/v1/trains/{number}/route"

    params = []

    if response_format:
        params.append(f"format={response_format}")

    if stops is not None:
        params.append(f"stops={str(stops).lower()}")

    if params:
        endpoint += "?" + "&".join(params)

    return make_request(endpoint)
