from fastmcp import FastMCP
from api import railradar
from api.railradar import RAILRADAR_API_KEY

from tools.stations import (
    search_stations,
    get_station_info,
    get_live_station_board
)

from tools.trains import (
    all_trains,
    trains_between,
    train_list,
    live_map,
    train_data,
    average_delay,
    train_instances,
    train_schedule
)

mcp = FastMCP("Indian Railway MCP|Github Profile: https://github.com/Nirmal2007")


print(r"""
===============================================
            Indian Railway MCP v1.0
               Created By Nirmal
 Github Profile: https://github.com/Nirmal2007
               Copyright © 2026
================================================
""")


#Station Based MCP Tools

mcp.tool()(search_stations)
mcp.tool()(get_station_info)
mcp.tool()(get_live_station_board)

#Train Based MCP Tools

mcp.tool()(all_trains)
mcp.tool()(trains_between)
mcp.tool()(train_list)
mcp.tool()(live_map)
mcp.tool()(train_data)
mcp.tool()(average_delay)
mcp.tool()(train_instances)
mcp.tool()(train_schedule)

#About the MCP
@mcp.tool()
def about():
    """
    Information about this MCP server.
    """

    return {
        "name": "Indian Railway MCP",
        "creator": "Nirmal Rajasekaran",
        "version": "1.0",
        "github": "https://github.com/Nirmal2007",
        "used_language" : "python",
        "created_date" : "25/05/2026"
    }


if __name__ == "__main__":
    mcp.run()