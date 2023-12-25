class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 29098103
    API_HASH = "06baef4020832888ccf3ebf4e746d52b"

    CASH_API_KEY = "U3I5J9MFS0Z9Y110"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://anime_uploader_user:E1B0Zwl9VhHVFng4j1sGNx3yhWDJdeLf@dpg-cm18s4gcmk4c73d6u2dg-a/anime_uploader"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1001999755155)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://godgamer9434:MNzSiu8pw2ZBcc3X@cluster0.yx21dk8.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/988ef3d1d8512e5eee3ba.jpg"

    SUPPORT_CHAT = "Grab_Your_WH_Group"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6536934928:AAGz2-ARFY6CkU8MD1kcWccbu7TWAV9TZLw"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "QFCVM2YL0XWZ"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 5332414680  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = [6260714402, 5191699870]  # User id of sudo users
    DEV_USERS = [5332414680]  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
