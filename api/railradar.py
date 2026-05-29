"""Make connection to RailRadar API."""

import httpx


# ===============================================
#             Indian Railway MCP v1.0
#  GitHub Profile: https://github.com/Nirmal2007
#                Copyright © 2026
# ===============================================


BASE_URL = "https://api.railradar.in"


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/137.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json,text/plain,*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Referer": "https://railradar.in/",
    "Origin": "https://railradar.in"
}


async def make_request(
    endpoint: str,
    params: dict | None = None
):
    """Send GET request to RailRadar."""

    url = f"{BASE_URL}{endpoint}"

    try:
        async with httpx.AsyncClient(
            headers=HEADERS,
            timeout=30,
            http2=False,
            follow_redirects=True
        ) as client:

            response = await client.get(
                url,
                params=params
            )

            response.raise_for_status()

            return response.json()

    except httpx.HTTPStatusError as error:
        return {
            "success": False,
            "error": (
                f"HTTP error: "
                f"{error.response.status_code}"
            ),
            "response": error.response.text
        }

    except httpx.RequestError as error:
        return {
            "success": False,
            "error": (
                f"Request failed: "
                f"{str(error)}"
            )
        }

    except ValueError:
        return {
            "success": False,
            "error": "Invalid JSON response"
        }
