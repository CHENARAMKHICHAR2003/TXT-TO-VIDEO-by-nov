

from os import environ

API_ID = int(environ.get("API_ID", "28389286"))
API_HASH = environ.get("API_HASH", "b88da5f4f338cca30f8ea5fb53cb083b")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Force Subscribe Configuration
FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "force_subscribe")  # Channel username without @, 
FORCE_SUB_CHANNEL_LINK = environ.get("FORCE_SUB_CHANNEL_LINK","https://t.me/force_subscribe")  # Channel link

# Admin Configuration
ADMINS = list(map(int, environ.get("ADMINS", "7693352537").split()))

# Optional: Bot Owner ID
OWNER_ID = int(environ.get("OWNER_ID", "7693352537"))

# Database URL (if you want to add database support later)
DATABASE_URL = environ.get("DATABASE_URL", "mongodb+srv://divyanshshukla5375_db_user:1kZ2dsVTktdMljpr@cluster0.lo5qk5v.mongodb.net/?appName=Cluster0")












