"""Make connection to RailRadar API."""

import http.client
import json


# ===============================================
#             Indian Railway MCP v1.0
#  GitHub Profile: https://github.com/Nirmal2007
#                Copyright © 2026
# ===============================================


BASE_URL = "api.railradar.in"


def make_request(
    endpoint: str,
    params: str | None = None
):
    """Send GET request to RailRadar."""

    conn = http.client.HTTPSConnection(
        BASE_URL
    )

    url = endpoint

    if params:
        url += f"?{params}"

    conn.request(
        "GET",
        url
    )

    response = conn.getresponse()

    data = response.read().decode(
        "utf-8"
    )

    conn.close()

    try:
        return json.loads(data)

    except json.JSONDecodeError:
        return {
            "success": False,
            "error": "Invalid JSON response",
            "raw": data
        }
