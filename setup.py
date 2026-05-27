"""Setup script for Indian Railway MCP."""

# ===============================================
#             Indian Railway MCP v1.0
#                Created By Nirmal
#  GitHub Profile: https://github.com/Nirmal2007
#                Copyright © 2026
# ===============================================

import json
import os
import platform
from pathlib import Path


def get_claude_config_path() -> Path | None:
    """Get Claude Desktop config directory."""

    system = platform.system()

    if system == "Windows":

        # Normal installer path
        normal_path = (
            Path.home()
            / "AppData"
            / "Roaming"
            / "Claude"
        )

        if normal_path.exists():
            return normal_path

        # Microsoft Store installation
        packages_dir = (
            Path.home()
            / "AppData"
            / "Local"
            / "Packages"
        )

        if packages_dir.exists():

            claude_dirs = list(
                packages_dir.glob("Claude*")
            )

            if claude_dirs:

                path = (
                    claude_dirs[0]
                    / "LocalCache"
                    / "Roaming"
                    / "Claude"
                )

                path.mkdir(
                    parents=True,
                    exist_ok=True
                )

                return path

        # Fallback
        normal_path.mkdir(
            parents=True,
            exist_ok=True
        )

        return normal_path

    if system == "Darwin":

        path = (
            Path.home()
            / "Library"
            / "Application Support"
            / "Claude"
        )

    if system == "Linux":

        path = Path(
            os.environ.get(
                "XDG_CONFIG_HOME",
                Path.home() / ".config"
            ),
            "Claude"
        )

    else:
        return None

    path.mkdir(
        parents=True,
        exist_ok=True
    )

    return path


def get_python_path() -> str:
    """Get virtual environment python path."""

    system = platform.system()

    if system == "Windows":
        return str(
            Path("venv/Scripts/python.exe").resolve()
        )

    return str(
        Path("venv/bin/python").resolve()
    )


def configure_claude():
    """Configure Claude Desktop MCP."""

    config_dir = get_claude_config_path()

    if not config_dir:
        print("❌ Unsupported operating system.")
        return

    config_file = (
        config_dir
        / "claude_desktop_config.json"
    )

    try:

        if config_file.exists():

            try:
                config = json.loads(
                    config_file.read_text(
                        encoding="utf-8"
                    )
                )

            except json.JSONDecodeError:
                print("⚠️ Invalid Claude config detected.")
                print("Creating a fresh config file.")
                config = {}

        else:
            config = {}

        if "mcpServers" not in config:
            config["mcpServers"] = {}

        config["mcpServers"]["indian-railway"] = {
            "command": get_python_path(),
            "args": [
                str(Path("server.py").resolve())
            ]
        }

        config_file.write_text(
            json.dumps(config, indent=2),
            encoding="utf-8"
        )

        print("✅ Claude Desktop configured successfully.")
        print(f"📁 Config Location: {config_file}")

    except (
        OSError,
        json.JSONDecodeError
    ) as error:
        print(f"❌ Failed to configure Claude Desktop: {error}")


print("""
====================================================
            Indian Railway MCP v1.0 Setup
             Created By Nirmal
     Github : https://github.com/Nirmal2007
====================================================
""")

api_key = input(
    "🔑 Enter your RailRadar API Key: "
).strip()

if not api_key:
    print("❌ API Key cannot be empty.")
    raise SystemExit

Path(".env").write_text(
    f"RAILRADAR_API_KEY={api_key}",
    encoding="utf-8"
)

print("✅ .env file created successfully.")

configure_claude()

print("""
====================================================
        🎉 Setup Completed Successfully
====================================================

Next Steps:

1. Completely close Claude Desktop
2. Open Task Manager
3. End all Claude processes
4. Reopen Claude Desktop
5. Your MCP should now appear automatically
6. Run python server.py
====================================================
""")
