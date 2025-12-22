from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = 21705136
        self.API_HASH = "78730e89d196e160b0f1992018c6cb19"

        self.BOT_TOKEN = "8228724963:AAEoltsESgo5ESfkSzZ7WnPNi--A6YtrOLk"
        self.MONGO_URL = "mongodb+srv://Krishna:pss968048@cluster0.4rfuzro.mongodb.net/?retryWrites=true&w=majority"

        self.LOGGER_ID = -1003107817392
        self.OWNER_ID = 7284147034

        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", 600000000)) * 600000000
        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", 20000000))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", 2000000))

        self.SESSION1 = "BAIrIowAMYL3GqSPIM2jJLirRwUCUVOp0aEtrYtBAqwpyG0BbXMaTXoWAr5sWE9AUrygfvDP6XESFeSNCUQl7X3MfXf-QKhtyYT-CZa5gt_Dll9q0kkMQlxbFO6uS71E7pEH-g7npn_HNIsD9BhEG_RggRxS76xCKX7lpM_KjhxX7_U4wZs2AGHNHAXEmUJYTLfgRVjGzmLjbP_LRksDe0qkltqw1yAGRTGH5_OrZ3S2w3T1SjlzXvvzI6xr15rlKV3YKuchdCTWQnVQhB68SMlMhlakfFbQftnWabUyL5Usc0NenbVzWSzwERA26CJG-oJhahLVs-y2umI00BasZuJ_PFl-6wAAAAF0Y2d0AA"
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        self.SUPPORT_CHANNEL = "https://t.me/khargyushh"
        self.SUPPORT_CHAT = "https://t.me/khargyushh"

        self.AUTO_END: bool = getenv("AUTO_END", True)
        self.AUTO_LEAVE: bool = getenv("AUTO_LEAVE", False)
        self.VIDEO_PLAY: bool = getenv("VIDEO_PLAY", True)
        self.COOKIES_URL = [
            url for url in getenv("COOKIES_URL", "").split(" ")
            if url and "batbin.me" in url
        ]
        self.DEFAULT_THUMB = "https://ar-hosting.pages.dev/1764356495482.jpg"
        self.PING_IMG = "https://ar-hosting.pages.dev/1764356495482.jpg"
        self.START_IMG = "https://ar-hosting.pages.dev/1764356495482.jpg"

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION1"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
