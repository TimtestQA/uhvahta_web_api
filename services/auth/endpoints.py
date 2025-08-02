import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv("HOST")

class Endpoints:
    verify_or_continue = "/api/v1/auth/verify-or-continue"
    refresh_token = f"/api/v1/auth/token/refresh"
    send_otp = f"/api/v1/auth/send-otp"
    logout = f"/api/v1/auth/logout"



print(Endpoints.verify_or_continue)