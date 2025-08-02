import allure
import pytest
from config.base_test import BaseTest
from services.subscription.payloads import Payloads

@allure.epic("Subscription")
@allure.story("Subscription Management")
class TestSubscription(BaseTest):

    @allure.title("Get tariffs")
    @pytest.mark.parametrize("expected", [
        pytest.param(True, id="valid request"),
    ])
    @pytest.mark.smoke
    @pytest.mark.subscription
    def test_get_tariffs(self, expected):
        """Test get tariffs endpoint."""
        response = self.subscription_api.get_tariffs(success=expected)
        if expected:
            assert response is not None
            assert isinstance(response, list) or hasattr(response, 'items')

    @allure.title("Create recurrent payment")
    @pytest.mark.parametrize("tariff_id, expected", [
        pytest.param(1, True, id="valid tariff"),
        pytest.param(999, False, id="invalid tariff"),
    ])
    @pytest.mark.subscription
    def test_create_recurrent(self, tariff_id, expected):
        """Test create recurrent payment endpoint."""
        response = self.subscription_api.create_recurrent(tariff_id=tariff_id, success=expected)
        if expected:
            assert response is not None
            assert hasattr(response, 'widget_url')

