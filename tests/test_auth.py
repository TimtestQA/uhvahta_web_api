import allure
import pytest
from config.base_test import BaseTest
from services.auth.payloads import Payloads

@allure.epic("Auth")
@allure.story("Authentication")
class TestAuth(BaseTest):

    @allure.title("Verify or continue - valid data")
    @pytest.mark.parametrize("payload, expected", [
        pytest.param(Payloads.valid_verify(), True, id="valid data"),
        pytest.param(Payloads.invalid_verify(), True, id="invalid data - but still 200"),  # API возвращает 200 даже для невалидных данных
    ])
    @pytest.mark.auth
    def test_verify_or_continue(self, payload, expected):
        """Test verify or continue endpoint with valid and invalid data."""
        response = self.auth_api.verify_or_continue(data=payload, success=expected)
        if expected:
            assert response is not None
            # Проверяем, что для валидных данных есть токены, для невалидных - нет
            if payload == Payloads.valid_verify():
                assert hasattr(response, 'access_token')
                assert hasattr(response, 'refresh_token')
                assert response.registered == True
            else:
                assert response.registered == False

    @allure.title("Send OTP")
    @pytest.mark.parametrize("email, expected", [
        pytest.param(Payloads.valid_email(), True, id="valid email"),
        pytest.param(Payloads.invalid_email(), False, id="invalid email"),
    ])
    @pytest.mark.auth
    def test_send_otp(self, email, expected):
        """Test send OTP endpoint."""
        response = self.auth_api.send_otp(email=email, success=expected)
        if expected:
            assert response.status_code == 204 # Для успешного запроса на отправку OTP ожидаем 204 No Content
        else:
            assert response is not None
            assert response.status_code == 422  # Ожидаем ошибку для невалидных email


    @allure.title("Refresh token")
    @pytest.mark.parametrize("refresh_token, expected", [
        pytest.param(Payloads.valid_refresh_token(), True, id="valid token"),
        pytest.param(Payloads.invalid_refresh_token(), False, id="invalid token"),
    ])
    @pytest.mark.auth
    def test_refresh_token(self, refresh_token, expected):
        """Test refresh token endpoint."""
        response = self.auth_api.refresh_token(refresh_token=refresh_token, success=expected)
        if expected:
            assert response is not None
            assert hasattr(response, 'access_token')


