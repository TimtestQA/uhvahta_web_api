
from faker import Faker

faker = Faker()

class Payloads:
    @staticmethod
    def valid_verify():
        return {
            "email": "freevoodoo@yandex.com",
            "otp_code": "123456"
        }

    @staticmethod
    def invalid_verify():
        return {
            "email": "nonregitr@nonmail.ru",
            "otp_code": "000000"
        }

    @staticmethod
    def valid_email():
        return "freevoodoo@yandex.com"

    @staticmethod
    def invalid_email():
        return "invalid-email"

    @staticmethod
    def valid_refresh_token():
        # Получаем валидный refresh token из успешной авторизации
        return "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI4OGYyNzY3Mi1mYzIwLTQ3MmUtODM1Yi0wNjZjZWQ2ZDc0NTgiLCJleHAiOjE3NTY1NjU5MjB9.1KsIp2KDeYFSDsCAGeoPzRUDpP7Lk5xw0-D345Y3mfI"

    @staticmethod
    def invalid_refresh_token():
        return "invalid_refresh_token" 