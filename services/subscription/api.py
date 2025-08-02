import allure
from config.headers import Headers
from helper.helper import Helper
from services.subscription.endpoints import Endpoints
from services.subscription.payloads import Payloads
from services.subscription.models.model_tariff import TariffResponseModel
from services.subscription.models.model_payment import PaymentResponseModel
from config.base_api import BaseAPI
from typing import List

class SubscriptionAPI(BaseAPI):
    def __init__(self, token, auth_type):
        self.token = token
        self.auth_type = auth_type
        self.headers = Headers(self.token, self.auth_type)
        self.endpoints = Endpoints()
        self.payloads = Payloads()

    @allure.step("Get tariffs")
    @allure.description("This method retrieves available tariffs.")
    def get_tariffs(self, success: bool = True) -> TariffResponseModel:
        response = self.client.get(
            model=TariffResponseModel,
            endpoint=self.endpoints.tariff(),
            headers=self.headers.get(),
            success=success
        )
        return response

    @allure.step("Create recurrent payment")
    @allure.description("This method creates a recurrent payment for a tariff.")
    def create_recurrent(self, tariff_id: int, success: bool = True) -> PaymentResponseModel:
        response = self.client.post(
            model=PaymentResponseModel,
            endpoint=self.endpoints.create_recurrent(),
            params={"tariff_id": tariff_id},
            headers=self.headers.get(),
            success=success
        )
        return response 