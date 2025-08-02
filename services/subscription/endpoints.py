import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv("HOST")

class Endpoints:
    create_recurrent = lambda self: f"{HOST}/api/v1/subscription/create-recurrent"
    tariff = lambda self: f"{HOST}/api/v1/subscription/tariff"