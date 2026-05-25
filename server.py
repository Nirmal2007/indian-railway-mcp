"""Indian Railway MCP Server using RailRadar API."""

from fastmcp import FastMCP

from tools.stations import (
    get_live_station_board,
    get_station_info,
    search_stations,
)

from tools.trains import (
    all_trains,
    average_delay,
    live_map,
    train_data,
    train_instances,
    train_list,
    train_schedule,
    trains_between,
)

mcp = FastMCP(
    "Indian Railway MCP | "
    "Github Profile: https://github.com/Nirmal2007"
)

print(r"""
===============================================
            Indian Railway MCP v1.0
               Created By Nirmal
 Github Profile: https://github.com/Nirmal2007
               Copyright © 2026
================================================
""")


# Station Based MCP Tools
mcp.tool()(search_stations)
mcp.tool()(get_station_info)
mcp.tool()(get_live_station_board)

# Train Based MCP Tools
mcp.tool()(all_trains)
mcp.tool()(trains_between)
mcp.tool()(train_list)
mcp.tool()(live_map)
mcp.tool()(train_data)
mcp.tool()(average_delay)
mcp.tool()(train_instances)
mcp.tool()(train_schedule)


@mcp.tool()
def about():
    """Return information about this MCP server."""

    return {
        "name": "Indian Railway MCP",
        "creator": "Nirmal Rajasekaran",
        "version": "1.0",
        "github": "https://github.com/Nirmal2007",
        "language": "Python",
        "created_date": "25/05/2026",
    }


if __name__ == "__main__":
    mcp.run()
