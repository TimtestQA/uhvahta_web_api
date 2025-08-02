import allure
import pytest
from config.base_test import BaseTest
from services.responds.payloads import Payloads

@allure.epic("Responds")
@allure.story("Responds Management")
class TestResponds(BaseTest):

    @allure.title("Get responds free")
    @pytest.mark.parametrize("params, expected", [
        pytest.param(Payloads.valid_responds_params(), True, id="valid params"),
        pytest.param(Payloads.invalid_responds_params(), False, id="invalid params"),
    ])
    @pytest.mark.responds
    def test_get_responds_free(self, params, expected):
        """Test get responds free endpoint."""
        response = self.responds_api.get_responds_free(params=params, success=expected)
        if expected:
            assert response is not None
            assert hasattr(response, 'items')

    @allure.title("Get responds")
    @pytest.mark.parametrize("params, expected", [
        pytest.param(Payloads.valid_responds_params(), True, id="valid params"),
        pytest.param(Payloads.invalid_responds_params(), False, id="invalid params"),
    ])
    @pytest.mark.responds
    def test_get_responds(self, params, expected):
        """Test get responds endpoint for authenticated user."""
        response = self.responds_api.get_responds(params=params, success=expected)
        if expected:
            assert response is not None
            assert hasattr(response, 'items') 