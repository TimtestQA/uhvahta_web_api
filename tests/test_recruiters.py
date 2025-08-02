import allure
import pytest
import requests

from config.base_test import BaseTest
from helper.helper import logger
from services.recruiters.payloads import Payloads

@allure.epic("Recruiters")
@allure.story("Recruiter Management")
class TestRecruiters(BaseTest):

    @allure.title("Get recruiter profile")
    @pytest.mark.parametrize("offset, limit, expected", [
        pytest.param(0, 10, True, id="valid params"),
        pytest.param(-1, 0, False, id="invalid params"),
    ])
    @pytest.mark.smoke
    @pytest.mark.recruiters
    def test_get_recruiter_profile(self, offset, limit, expected):
        """Test to check the retrieval of recruiter profile information."""
        response = self.recruiters_api.get_recruiter(offset=offset, limit=limit, success=expected)
        if expected:
            assert response is not None

    @allure.title("Register recruiter")
    @pytest.mark.parametrize("payload, expected", [
        pytest.param(Payloads.recruiter_register_params(), True, id="valid payload"),
        pytest.param({}, False, id="empty payload"),
    ])
    @pytest.mark.registration
    @pytest.mark.recruiters
    def test_register_recruiter(self, payload, expected):
        """Test to check the registration of a new recruiter."""
        response = self.recruiters_api.register_recruiter(payload=payload, success=expected)
        if expected:
            assert response is not None
            assert hasattr(response, 'access_token')

    @allure.title("Check GUID")
    @pytest.mark.parametrize("guid, expected", [
        pytest.param("valid-guid-123", True, id="valid guid"),
        pytest.param("invalid-guid", False, id="invalid guid"),
    ])
    @pytest.mark.recruiters
    def test_check_guid(self, guid, expected):
        """Test to check GUID validation."""
        response = self.recruiters_api.check_guid(guid=guid, success=expected)
        if expected:
            assert response is not None