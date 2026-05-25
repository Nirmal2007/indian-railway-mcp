"""
===============================================
            Indian Railway MCP v1.0
               Created By Nirmal
 Github Profile: https://github.com/Nirmal2007
               Copyright © 2026
================================================
"""


from api.railradar import make_request
from dotenv import load_dotenv


load_dotenv()


def search_stations(query:str):
    endpoint = f"/api/v1/search/stations?query={query}"
    return make_request(endpoint)


def get_station_info(stationcode:str):
    endpoint = f"/api/v1/stations/{stationcode}/info"
    return make_request(endpoint)


def get_live_station_board(stationcode:str, hours:int , tosationcode:str = None):
    endpoint = (
        f"/api/v1/stations/"
        f"{stationcode}/live"
        f"?hours={hours}"
    )

    if tosationcode:
        endpoint += f"&toStationCode={tosationcode}"

    return make_request(endpoint)
