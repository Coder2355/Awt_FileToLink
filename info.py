import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Awt_bots')
API_ID = int(environ.get('API_ID', '21740783'))
API_HASH = environ.get('API_HASH', 'a5dc7fec8302615f5b441ec5e238cd46')
BOT_TOKEN = environ.get('BOT_TOKEN', "7116266807:AAGdvkZKT4WxbE5qT1RSfJPoFh0TGxtaneg")

# Bot settings
PORT = environ.get("PORT", "8030")

# Online Stream and Download
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "")
# Admins, Channels & Users
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '0'))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6299192020').split()]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Speedwolf1:speedwolf24689@cluster0.rgfywsf.mongodb.net/")
DATABASE_NAME = environ.get('DATABASE_NAME', "Speedwolf1")

# Shortlink Info
SHORTLINK = bool(environ.get('SHORTLINK', False)) # Set True Or False
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'api.shareus.io')
SHORTLINK_API = environ.get('SHORTLINK_API', 'hRPS5vvZc0OGOEUQJMJzPiojoVK2')
