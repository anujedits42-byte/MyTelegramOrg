import os
from translation import Translation


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
    URL = os.environ.get("URL", "")
    PORT = int(os.environ.get("PORT", 5000))
    CHUNK_SIZE = 10280
    APP_TITLE = os.environ.get(
        "APP_TITLE",
        "api_id_api_hash_ak_bot"
    )
    APP_SHORT_NAME = os.environ.get(
        "APP_SHORT_NAME",
        "api_id_api_hash_ak_bot"
    )
    APP_URL = os.environ.get(
        "APP_URL",
        "https://telegram.dog/api_id_api_hash_ak_bot"
    )

    APP_PLATFORM = [
        "android",
        "ios",
        "wp",
        "bb",
        "desktop",
        "web",
        "ubp",
        "other"
    ]

    APP_DESCRIPTION = os.environ.get(
        "APP_DESCRIPTION",
        "created using https://telegram.org/api_id_api_hash_ak_bot"
    )

    FOOTER_TEXT = os.environ.get(
        "FTEXT",
        "Please Subscribe ❤️ @anujedits76"
    )

    START_TEXT = os.environ.get(
        "START_TEXT",
        Translation.START_TEXT
    )

    AFTER_RECVD_CODE_TEXT = os.environ.get(
        "AFTER_RECVD_CODE_TEXT",
        Translation.AFTER_RECVD_CODE_TEXT
    )

    BEFORE_SUCC_LOGIN = os.environ.get(
        "BEFORE_SUCC_LOGIN",
        Translation.BEFORE_SUCC_LOGIN
    )

    ERRED_PAGE = os.environ.get(
        "ERRED_PAGE",
        Translation.ERRED_PAGE
    )

    CANCELLED_MESG = os.environ.get(
        "CANCELLED_MESG",
        Translation.CANCELLED_MESG
    )

    IN_VALID_CODE_PVDED = os.environ.get(
        "IN_VALID_CODE_PVDED",
        Translation.IN_VALID_CODE_PVDED
    )

    IN_VALID_PHNO_PVDED = os.environ.get(
        "IN_VALID_PHNO_PVDED",
        Translation.IN_VALID_PHNO_PVDED
    )


class Development(Config):
    pass


    # ✅ FIXED: STATUS TEXT ADDED
    STATUS_TEXT = os.environ.get(
        "STATUS_TEXT",
        Translation.STATUS_TEXT
    )
