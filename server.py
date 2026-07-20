"""Indian Railway MCP Server using RailRadar API."""

from fastmcp import FastMCP

from tools.stations import (
    get_all_station_kvs,
    get_live_station_board,
    get_station_board,
)

from tools.trains import (
    all_trains,
    average_delay,
    train_data,
    train_live_status,
    train_schedule,
    trains_between,
    trains_between_type,
)

from tools.map import (
    live_map,
)

mcp = FastMCP(
    "Indian Railway MCP | "
    "Github Profile: https://github.com/Nirmal2007"
)

print(r"""
===============================================
            Indian Railway MCP v1.0
    Created By https://github.com/Nirmal2007
        Dont Forget to Star the repo :
https://github.com/Nirmal2007/indian-railway-mcp
               Copyright © 2026
================================================
""")

# -------------------------
# Station Based MCP Tools
# -------------------------

mcp.tool()(get_all_station_kvs)
mcp.tool()(get_live_station_board)
mcp.tool()(get_station_board)

# -------------------------
# Train Based MCP Tools
# -------------------------

mcp.tool()(all_trains)
mcp.tool()(trains_between)
mcp.tool()(trains_between_type)
mcp.tool()(train_data)
mcp.tool()(average_delay)
mcp.tool()(train_live_status)
mcp.tool()(train_schedule)

# -------------------------
# Map Based MCP Tools
# -------------------------

mcp.tool()(live_map)


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