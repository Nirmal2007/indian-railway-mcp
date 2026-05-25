"""
===============================================
            Indian Railway MCP v1.0
               Created By Nirmal
 Github Profile: https://github.com/Nirmal2007
               Copyright © 2026
================================================
"""


import os
import json
from dotenv import load_dotenv
import http.client

load_dotenv()

RAILRADAR_API_KEY = os.getenv("RAILRADAR_API_KEY")

if not RAILRADAR_API_KEY:
    raise Exception(
        "Missing Rail Radar API Key. Run setup.py first."
    )
def make_request(endpoint):

    conn = http.client.HTTPSConnection("api.railradar.org")

    headers = {
        "X-API-Key": RAILRADAR_API_KEY
    }

    conn.request(
        "GET",
        endpoint,
        headers=headers
    )

    response = conn.getresponse()

    data = response.read().decode()

    conn.close()

    return json.loads(data)

