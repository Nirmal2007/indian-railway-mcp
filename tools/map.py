"Gives a live Indian-Railway train map."

from api.railradar import make_request


def live_map(
    number: str,
    format: str | None = None,
    stops: bool | None = None,
):
    """
    Returns the route geometry for a train(Map coordinates).

    Parameters
    ----------
    number : 5-digit train number.
    format : Response format.
             Allowed values: "geojson", "polyline", "coordinates".
             Default: "geojson".
    stops : Include station stops alongside the geometry.
            Default: False.
    """

    endpoint = f"/app/v1/trains/{number}/route"

    params = []

    if format:
        params.append(f"format={format}")

    if stops is not None:
        params.append(f"stops={str(stops).lower()}")

    if params:
        endpoint += "?" + "&".join(params)

    return make_request(endpoint)
