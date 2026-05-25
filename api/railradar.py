"""Make connection to RailRadar API."""

import http.client
import json
import os

from dotenv import load_dotenv

# ===============================================
#             Indian Railway MCP v1.0
#                Created By Nirmal
#  Github Profile: https://github.com/Nirmal2007
#                Copyright © 2026
# ===============================================

load_dotenv()

RAILRADAR_API_KEY = os.getenv("RAILRADAR_API_KEY")

if not RAILRADAR_API_KEY:
    raise ValueError(
        "Missing RailRadar API key. Run setup.py first."
    )


def make_request(endpoint):
    """Send GET request to RailRadar API."""

    conn = http.client.HTTPSConnection(
        "api.railradar.org"
    )

    headers = {
        "X-API-Key": RAILRADAR_API_KEY
    }

    conn.request(
        "GET",
        endpoint,
        headers=headers
    )

    response = conn.getresponse()

    data = response.read().decode("utf-8")

    conn.close()

    return json.loads(data)