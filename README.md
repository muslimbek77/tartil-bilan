# Aiogram 3 New Template (SQLite db)

### 1. Create virtual environment and install packages
Windows
```shell
python -m venv venv && venv\Scripts\activate && pip install -r requirements.txt
```

Linux/Mac
```shell
python3 -m venv venv && source venv/bin/activate && pip3 install -r requirements.txt
```

### 2. Configure environment
- Create `.env` file and set required variables:
	- `BOT_TOKEN=123456:ABC...`
	- `ADMINS=123456789,987654321`
- If present, you can copy from `.env copy` and update values.

### 3. Run bot.py
Windows
```shell
python bot.py
```
Linux/Mac
```shell
python3 bot.py
```

### Notes
- Uses `aiogram==3.20.0.post0` with modern middleware and routers.
- Default bot parse mode is HTML (set in loader).
- Throttling and subscription middlewares are enabled in `bot.py`.
- SQLite DB is auto-initialized on startup; tables `Users` and `Channels`.
