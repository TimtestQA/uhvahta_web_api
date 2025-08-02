import allure
from config.headers import Headers
from helper.helper import Helper
from services.responds.endpoints import Endpoints
from services.responds.payloads import Payloads
from services.responds.models.model_responds import RespondsResponseModel
from config.base_api import BaseAPI

class RespondsAPI(BaseAPI):
    def __init__(self, token, auth_type):
        self.token = token
        self.auth_type = auth_type
        self.headers = Headers(self.token, self.auth_type)
        self.endpoints = Endpoints()
        self.payloads = Payloads()

    @allure.step("Get responds free")
    @allure.description("This method retrieves free responds.")
    def get_responds_free(self, params: dict = None, success: bool = True) -> RespondsResponseModel:
        response = self.client.get(
            model=RespondsResponseModel,
            endpoint=self.endpoints.responds_free,
            params=params,
            success=success
        )
        return response

    @allure.step("Get responds")
    @allure.description("This method retrieves responds for authenticated user.")
    def get_responds(self, params: dict = None, success: bool = True) -> RespondsResponseModel:
        response = self.client.get(
            model=RespondsResponseModel,
            endpoint=self.endpoints.responds,
            params=params,
            headers=self.headers.get(),
            success=success
        )
        return response 