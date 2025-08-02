from services.recruiters.api import RecruitersAPI
from services.auth.api import AuthAPI
from services.responds.api import RespondsAPI
from services.subscription.api import SubscriptionAPI
from config.tokens import TOKENS

class BaseTest:
    def setup_method(self):
        # Создаем API клиенты с дефолтными токенами
        self._recruiters_api = RecruitersAPI(token=TOKENS["recruiter"], auth_type="Bearer")
        self._auth_api = AuthAPI(token=TOKENS["recruiter"], auth_type="Bearer")
        self._responds_api = RespondsAPI(token=TOKENS["recruiter"], auth_type="Bearer")
        self._subscription_api = SubscriptionAPI(token=TOKENS["recruiter"], auth_type="Bearer")

    @property
    def recruiters_api(self):
        return self._recruiters_api

    @property
    def auth_api(self):
        return self._auth_api

    @property
    def responds_api(self):
        return self._responds_api

    @property
    def subscription_api(self):
        return self._subscription_api

    # Методы для создания API с кастомными токенами
    def recruiters_api_with_token(self, token: str):
        return RecruitersAPI(token=token, auth_type="Bearer")

    def auth_api_with_token(self, token: str):
        return AuthAPI(token=token, auth_type="Bearer")

    def responds_api_with_token(self, token: str):
        return RespondsAPI(token=token, auth_type="Bearer")

    def subscription_api_with_token(self, token: str):
        return SubscriptionAPI(token=token, auth_type="Bearer")