"""
===============================================
            Indian Railway MCP v1.0
               Created By Nirmal
 Github Profile: https://github.com/Nirmal2007
               Copyright © 2026
================================================
"""

from api.railradar import make_request


def all_trains():


    endpoint = "/api/v1/trains/all-kvs"

    return make_request(endpoint)


def trains_between(from_station: str, to_station: str):


    endpoint = (
        f"/api/v1/trains/between"
        f"?from={from_station}"
        f"&to={to_station}"
    )

    return make_request(endpoint)


def train_list(
    page: int = 1,
    limit: int = 50,
    train_type: str = "",
    zone: str = "",
    search: str = ""
):

    endpoint = (
        f"/api/v1/trains/list"
        f"?page={page}"
        f"&limit={limit}"
        f"&type={train_type}"
        f"&zone={zone}"
        f"&search={search}"
    )

    return make_request(endpoint)


def live_map():

    endpoint = "/api/v1/trains/live-map"

    return make_request(endpoint)


def train_data(
    train_number: str,
    journey_date: str = "",
    data_type: str = "full",
    data_provider: str = "railradar"
):


    endpoint = (
        f"/api/v1/trains/{train_number}"
        f"?journeyDate={journey_date}"
        f"&dataType={data_type}"
        f"&dataProvider={data_provider}"
    )

    return make_request(endpoint)


def average_delay(train_number: str):

    endpoint = (
        f"/api/v1/trains/"
        f"{train_number}/average-delay"
    )

    return make_request(endpoint)


def train_instances(
    train_number: str,
    data_provider: str = "railradar"
):


    endpoint = (
        f"/api/v1/trains/"
        f"{train_number}/instances"
        f"?dataProvider={data_provider}"
    )

    return make_request(endpoint)


def train_schedule(
    train_number: str,
    journey_date: str
):

    endpoint = (
        f"/api/v1/trains/"
        f"{train_number}/schedule"
        f"?journeyDate={journey_date}"
    )

    return make_request(endpoint)