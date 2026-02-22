import os
from typing import List, Optional
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        # Anytype
        self.anytype_api_url = os.getenv("ANYTYPE_API_URL", "http://anytype-server:31012/api/v1")
        self.anytype_api_key = os.getenv("ANYTYPE_API_KEY")
        self.anytype_space_id = os.getenv("ANYTYPE_SPACE_ID")
        
        # Telegram
        self.tg_bot_token = os.getenv("TG_BOT_TOKEN", "")
        self.tg_bot_webhook_url = os.getenv("TG_BOT_WEBHOOK_URL")
        self.tg_bot_webhook_port = int(os.getenv("TG_BOT_WEBHOOK_PORT", "8080"))
        
        # Parse allowed user IDs
        allowed_ids = os.getenv("ALLOWED_USER_IDS", "")
        self.allowed_user_ids = [int(id.strip()) for id in allowed_ids.split(",") if id.strip()]
        
        # OpenAI
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.openai_model = os.getenv("OPENAI_MODEL", "gpt-4")
        
        # Bot settings
        self.log_level = os.getenv("LOG_LEVEL", "INFO")
        self.bot_mode = os.getenv("BOT_MODE", "polling")

config = Config()

