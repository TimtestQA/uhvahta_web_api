import allure
from pydantic_core.core_schema import model_field
from config.headers import Headers
from helper.helper import Helper
from services.recruiters.endpoints import Endpoints
from services.recruiters.models.model_create import RecruiterDataModel, CreateRecruiterResponseModel
from services.recruiters.payloads import Payloads
from services.recruiters.models.model_check_guid import CheckGuidResponseModel
from services.recruiters.models.model_profile_recruiter import RecruiterProfileModel
import requests
import json
from config.base_api import BaseAPI

class RecruitersAPI(BaseAPI):
    def __init__(self, token, auth_type):
        self.token = token
        self.auth_type = auth_type
        self.headers = Headers(self.token, self.auth_type)
        self.endpoints = Endpoints()
        self.payloads = Payloads()

    @allure.step("Get recruiter profile")
    @allure.description("This method retrieves the profile of the recruiter.")
    def get_recruiter(self, offset: int = 0, limit: int = 10, success: bool = True) -> RecruiterProfileModel:
        response = self.client.get(
            model=RecruiterProfileModel,
            endpoint=self.endpoints.get_recruiter_profile,
            params={"offset": offset, "limit": limit},
            headers=self.headers.get(),
            success=success
        )
        return response

    @allure.step("Registration recruiter")
    @allure.description("This method registers a new recruiter.")
    def register_recruiter(self, payload=None, success: bool = True) -> CreateRecruiterResponseModel:
        if payload is None:
            payload = self.payloads.recruiter_register_params()
        
        response = self.client.post(
            model=CreateRecruiterResponseModel,
            endpoint=self.endpoints.register_recruiter,
            data=payload,
            files=[
                ("files", ("test_api.png", open("test_api_file.png", "rb"), "image/png"))
            ],
            headers=self.headers.get(),
            success=success
        )
        return response

    @allure.step("Check GUID")
    @allure.description("This method checks if GUID is valid.")
    def check_guid(self, guid: str, success: bool = True) -> CheckGuidResponseModel:
        response = self.client.get(
            model=CheckGuidResponseModel,
            endpoint=self.endpoints.check_guid.format(guid=guid),
            success=success
        )
        return response




