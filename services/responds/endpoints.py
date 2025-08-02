import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv("HOST")

class Endpoints:
    responds_free = "/web/api/v1/responds-free"
    responds = f"/web/api/v1/responds"