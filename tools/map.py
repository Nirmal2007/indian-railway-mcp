"Gives a live Indian-Railway train map."

from api.railradar import make_request


def live_map():
    """Fetch live train map."""

    endpoint = "/api/v1/trains/live-map"

    return make_request(endpoint)
