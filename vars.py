#𓆰𝐑𝐀𝐍𝐀 𝐉𝐈𝐈 𓆪
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "23557588"))
API_HASH = environ.get("API_HASH", "7ed52f38f74fe85ebc2e5e285051c3b6")
BOT_TOKEN = environ.get("BOT_TOKEN", "8282609988:AAEUXHOxBzGgRS28JjdT7KOV66HvL79OqUI")
OWNER = int(environ.get("OWNER", "2084001270"))
CREDIT = "𓆰𝐑𝐀𝐍𝐀 𝐉𝐈𝐈 𓆪"
AUTH_USER = os.environ.get('AUTH_USERS', '5302639580,6187058869').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
