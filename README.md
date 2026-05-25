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
[Screen Recording 2026-05-25 232750.mp4](Documentation/assets/Screen%20Recording%202026-05-25%20232750.mp4)
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
Nirmal Railway MCP
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
git clone https://github.com/YOUR_USERNAME/nirmal-railway-mcp.git
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

---

# 🚀 Run MCP Server

```bash
python server.py
```

---

# 🖥️ Claude Desktop Integration

For Calude Desktop Integration go through [Claude Desktop Setup Guide](Documentation/ClaudeDesktopSetup.md)

Add to:

```text
%APPDATA%\Claude\claude_desktop_config.json
```

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

Restart Claude Desktop(Open Task Manager And END TASK Claude Desktop).

---

# 💬 Example Prompts

```text
Search station Madurai
```

```text
Find trains between Dindigul to Tenkasi
```

```text
Where is the Vaigai SF express now?
```

```text
Show schedule for Chendur SF Express
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