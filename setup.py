"""Setup script for Indian Railway MCP."""

# ===============================================
#             Indian Railway MCP v1.0
#                Created By Nirmal
#  Github Profile: https://github.com/Nirmal2007
#                Copyright © 2026
# ===============================================


print("""
====================================================
            Indian Railway MCP v1.0 Setup
     Github Profile : https://github.com/Nirmal2007
=====================================================
""")

api_key = input(
    "Enter your RailRadar API Key: "
).strip()

with open(
    ".env",
    "w",
    encoding="utf-8"
) as env_file:
    env_file.write(
        f"RAILRADAR_API_KEY={api_key}"
    )

print("\n✅ Setup completed successfully.")