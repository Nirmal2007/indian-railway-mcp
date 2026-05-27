# 🚆 Indian Railway MCP

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![FastMCP](https://img.shields.io/badge/FastMCP-AI%20Tools-green?style=for-the-badge)
![Claude](https://img.shields.io/badge/Claude-MCP-orange?style=for-the-badge)
![RailRadar](https://img.shields.io/badge/RailRadar-Live%20API-red?style=for-the-badge)


### AI-Powered Indian Railway MCP Server

Real-time railway intelligence for Claude Desktop using MCP + RailRadar API.

https://github.com/user-attachments/assets/438be1cd-d07d-4d93-8a9f-34a0118e46c5
</div>

---

# ✨ Features

✅ Live train tracking  
✅ Station search  
✅ Train schedules  
✅ Trains between stations  
✅ Journey instance tracking  
✅ Average delay analytics  
✅ Real-time train map support  
✅ Claude Desktop MCP integration  

---

# 🧠 What Is This?

Indian Railway MCP transforms Claude into a real-time Indian Railway assistant using the MCP (Model Context Protocol).

Instead of static web answers, Claude can:

- fetch live train data
- monitor delays
- track train journeys
- search stations instantly
- analyze schedules dynamically

---

# 🏗️ Architecture

```text
Claude Desktop
       ↓
Indian Railway MCP
       ↓
RailRadar API
       ↓
Live Indian Railway Data
```

---

# 📂 Project Structure

```text
indian-railway-mcp/
│
├── api/
│   └── railradar.py
│
├── tools/
│   ├── stations.py
│   ├── trains.py
│   └── live.py
│
├── server.py
├── setup.py
├── requirements.txt
├── README.md
├── LICENCE
└── .gitignore
```

---

# ⚡ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Nirmal2007/indian-railway-mcp.git
```

---

## 2️⃣ Enter Project

```bash
cd indian-railway-mcp
```

---

## 3️⃣ Create Virtual Environment

```bash
python -m venv venv
```

---

## 4️⃣ Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 API Key Setup

Get your API key from RailRadar.

Go through [Rail Radar API Guide ](Documentation/RailRadarGuide.md) for getting your api key easily 


Then run:

```bash
python setup.py
```

Enter your API key when prompted.


# 🖥️ Claude Desktop Integration

## Automatic Method (Recommended)

Run:

```bash
python setup.py
```

The setup script will automatically:

- Create `.env`
- Save your API key
- Configure Claude Desktop
- Register the MCP server

After setup:

1. Completely close Claude Desktop
2. Open Task Manager
3. End all Claude processes
4. Reopen Claude Desktop

Your MCP should now appear automatically.

---

## ⚠️ If You See This Error

```text
❌ Failed to configure Claude Desktop
```

or

```text
❌ Claude Desktop config directory not found
```

Please follow the manual setup guide: [Claude Desktop Setup Guide](Documentation/ClaudeDesktopSetup.md)

```text
Documentation/ClaudeDesktopSetup.md
```

---

## Manual Method (Only If Automatic Setup Fails)

If the automatic configuration does not work on your system, manually configure Claude Desktop.

### Windows

Edit:

```text
%APPDATA%\Claude\claude_desktop_config.json
```

### macOS

Edit:

```text
~/Library/Application Support/Claude/claude_desktop_config.json
```

### Linux

Edit:

```text
~/.config/Claude/claude_desktop_config.json
```

Add:

```json
{
  "mcpServers": {
    "indian-railway": {
      "command": "FILE_LOCATION/indian-railway-mcp/venv/Scripts/python.exe",
      "args": [
        "FILE_LOCATION/indian-railway-mcp/server.py"
      ]
    }
  }
}
```

Replace:

```text
FILE_LOCATION
```

with your actual project location.

Example:

```text
D:/My_MCP/indian-railway-mcp
```
Here Replace FILE_LOCATION by 
```text
D:/My_MCP
```
Please follow the manual setup guide: [Claude Desktop Setup Guide](Documentation/ClaudeDesktopSetup.md)
for detailed Assistant

Then:

1. Save the file
2. Close Claude Desktop completely
3. End all Claude processes in Task Manager
4. Reopen Claude Desktop
---

# 🚀 Run MCP Server

```bash
python server.py
```
#### Output Should be:

```bash
(venv) PS D:\indian-railway-mcp> python server.py

===============================================
            Indian Railway MCP v1.0
    Created By https://github.com/Nirmal2007
               Copyright © 2026
================================================



                    ╭──────────────────────────────────────────────────────────────────────────────╮
                    │                                                                              │
                    │                                                                              │
                    │                         ▄▀▀ ▄▀█ █▀▀ ▀█▀ █▀▄▀█ █▀▀ █▀█                        │
                    │                         █▀  █▀█ ▄▄█  █  █ ▀ █ █▄▄ █▀▀                        │
                    │                                                                              │
                    │                                                                              │
                    │                                                                              │
                    │                                FastMCP 3.3.1                                 │
                    │                            https://gofastmcp.com                             │
                    │                                                                              │
                    │    🖥  Server:      Indian Railway MCP | Github Profile:                      │
                    │                    https://github.com/Nirmal2007, 3.3.1                      │
                    │    🚀 Deploy free: https://horizon.prefect.io                                │
                    │                                                                              │
                    ╰──────────────────────────────────────────────────────────────────────────────╯


[05/27/26 16:25:51] INFO     Starting MCP server 'Indian Railway MCP | Github Profile:                  transport.py:209
                             https://github.com/Nirmal2007' with transport 'stdio'
                      https://github.com/Nirmal2007' with transport 'stdio'

```

---


---

# 💬 Example Prompts

```text
Search Trains at Madurai Junction
```

```text
Find trains between Dindigul to Tenkasi
```

```text
Where is the Vaigai SF express now?
```

```text
Based on my Calender tell me trains for Chennai 
```

---

# 🛠️ Technologies Used

- Python
- FastMCP
- RailRadar API
- Claude Desktop MCP
- JSON APIs
- REST Architecture

---

# 🌟 Future Plans

- Platform prediction
- Delay prediction AI
- Voice assistant
- WhatsApp integration
- Live train map UI
- Smart travel planner

---

# 👨‍💻 Created By

## Nirmal Rajasekaran
 Github Profile: https://github.com/Nirmal2007


AI & Backend Developer



---

# 📜 License

[MIT License](LICENCE)

---

<div align="center">

### ⭐ Star this repository if you like the project!

</div>

*Copyright © 2026*