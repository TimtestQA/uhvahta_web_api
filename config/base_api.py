import os
from client.api_client import RequestClient
from helper.helper import Helper

class BaseAPI:

    client = RequestClient(base_url=os.getenv("HOST_URL"))
    helper = Helper()


