import os
from dotenv import load_dotenv

load_dotenv()

# def get_token(token_type):
#     """Retrieve the token for the specified type."""
#     if token_type == "recruiter":
#         os.getenv("RECRUITER_TOKEN")
#     elif token_type == "admin":
#         os.getenv("ADMIN_TOKEN")
#     elif token_type == "moderator":
#         os.getenv("MODERATOR_TOKEN")
#     return TOKENS.get(token_type, None)


TOKENS = {
    "recruiter": os.getenv("RECRUITER_TOKEN"),
    "admin": os.getenv("ADMIN_TOKEN"),
    "moderator": os.getenv("MODERATOR_TOKEN"),
    "guest": os.getenv("GUEST_TOKEN")}
