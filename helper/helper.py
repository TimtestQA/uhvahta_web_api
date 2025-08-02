import json
import logging
import allure
import requests
from pydantic import BaseModel
from utils.logger import logger




class Helper:

    # def attach(self, response, name: str):
    #     result = json.dumps(response, ensure_ascii=False, indent=4)
    #     allure.attach(
    #         body=result.encode("utf-8"),
    #         name="API Response",
    #         attachment_type=allure.attachment_type.JSON
    #     )
    #
    def attach(self, name: str, body):
        result = json.dumps(body, ensure_ascii=False, indent=4)
        allure.attach(
            body=result.encode("utf-8"),
            name=name,
            attachment_type=allure.attachment_type.JSON
        )

