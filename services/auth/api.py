import allure
from config.headers import Headers
from helper.helper import Helper
from services.auth.endpoints import Endpoints
from services.auth.payloads import Payloads
from services.auth.models.model_token import TokenResponseModel
from services.auth.models.model_otp import SendOTPModel
from services.auth.models.model_verify import VerifyOrContinueModel
from config.base_api import BaseAPI

class AuthAPI(BaseAPI):
    def __init__(self, token, auth_type):
        self.token = token
        self.auth_type = auth_type
        self.headers = Headers(self.token, self.auth_type)
        self.endpoints = Endpoints()
        self.payloads = Payloads()

    @allure.step("Verify or continue")
    @allure.description("This method verifies OTP or continues authentication.")
    def verify_or_continue(self, data: dict, success: bool = True) -> TokenResponseModel:
        response = self.client.post(
            model=TokenResponseModel,
            endpoint=self.endpoints.verify_or_continue,
            json=data,
            headers=self.headers.get(),
            success=success
        )
        return response

    @allure.step("Send OTP")
    @allure.description("This method sends OTP to email.")
    def send_otp(self, email: str, success: bool = True) -> SendOTPModel:
        response = self.client.post(
            model=None,  # Для 204 не нужна модель
            endpoint=self.endpoints.send_otp,
            json={"email": email},
            success=success
        )
        return response

    @allure.step("Refresh token")
    @allure.description("This method refreshes access token.")
    def refresh_token(self, refresh_token: str, success: bool = True) -> TokenResponseModel:
        # Для refresh token нужен специальный header
        headers = self.headers.get()
        headers["Token"] = refresh_token
        
        response = self.client.post(
            model=TokenResponseModel,
            endpoint=self.endpoints.refresh_token,
            json={"refresh_token": refresh_token},
            headers=headers,
            success=success
        )
        return response

    @allure.step("Logout")
    @allure.description("This method logs out the user.")
    def logout(self, success: bool = True):
        response = self.client.post(
            model=None,  # 204 No Content
            endpoint=self.endpoints.logout,
            headers=self.headers.get(),
            success=success
        )
        return response


