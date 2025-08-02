from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.getenv("HOST_URL")


class Endpoints:

    check_guid = "/recruiters/check-guid/{guid}"
    get_recruiter_profile = "/api/v1/recruiter/profile"
    register_recruiter = "/api/v1/recruiter/register"


print(Endpoints().get_recruiter_profile)  # Example usage, will print the endpoint for checking a GUID