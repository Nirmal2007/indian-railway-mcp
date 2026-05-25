"""Get API key from user"""

"""
===============================================
            Indian Railway MCP v1.0
               Created By Nirmal
 Github Profile: https://github.com/Nirmal2007
               Copyright © 2026
================================================
"""


print("""
====================================================
            Indian Railway MCP v1.0 Setup
     Github Profile : https://github.com/Nirmal2007
=====================================================
""")

api_key = input("Enter your RailRadar API Key: ")

with open(".env", "w", encoding="utf-8") as f:
    f.write(f"RAILRADAR_API_KEY={api_key}")

print("\n✅ Setup completed successfully.")
