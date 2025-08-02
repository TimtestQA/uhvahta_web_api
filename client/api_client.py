import json
import requests
import allure
from utils.logger import logger
from pydantic import BaseModel
from config.headers import Headers
from helper.helper import Helper


class RequestClient(Helper):

    def __init__(self, base_url, headers=None):
        self.helper = Helper()
        self.base_url = base_url  # https://example.com/api/v1
        self.session = requests.Session()

        # Устанавливаем базовые headers по умолчанию
        default_headers = Headers().get()
        self.session.headers.update(default_headers)

        # Если переданы дополнительные headers, объединяем их с дефолтными
        if headers:
            self.session.headers.update(headers)

    def _log_request(self, method, url, **kwargs):
        logger.info(f"➡️ {method.upper()} - {url}")

        if "json" in kwargs and kwargs["json"]:
            self.helper.attach("request (json)", kwargs["json"])

        elif "data" in kwargs and kwargs["data"]:
            data = kwargs["data"]
            # Попробуем превратить строку в словарь, если это JSON-строка
            if isinstance(data, str):
                try:
                    parsed_data = json.loads(data)
                    self.helper.attach("request (data)", parsed_data)
                except json.JSONDecodeError:
                    logger.warning("⚠️ 'data' is a non-JSON string — not attaching")
            elif isinstance(data, dict):
                self.helper.attach("request (data)", data)
            else:
                logger.warning(f"⚠️ 'data' is of unsupported type: {type(data)} — not attaching")

    def _log_response(self, response: requests.Response):
        logger.info(f"⬅️ Status: {response.status_code}")
        try:
            if response.status_code == 204:
                logger.info("Response: No Content (204)")
            else:
                logger.info(f"Response: {response.json()}")
        except json.JSONDecodeError:
            logger.info(f"Response: {response.text}")

    def _request(self, method, endpoint, headers=None, success=None, **kwargs) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        self._log_request(method, url, **kwargs)

        response = self.session.request(method=method, url=url, headers=headers, **kwargs)
        
        if success is not None:
            if success:
                assert 200 <= response.status_code < 400, f"Expected success status, got {response.status_code}: {response.text}"
            else:
                assert response.status_code >= 400, f"Expected error status, got {response.status_code}: {response.text}"
        
        self._log_response(response)
        return response

    def _validate_response(self, response: requests.Response, model: type[BaseModel] = None, status_code: int = 200):
        # Если статус 204 (No Content), не пытаемся парсить JSON
        if response.status_code == 204:
            self.helper.attach("response", {"status": "No Content"})
            # Для 204 не проверяем status_code, так как это валидный ответ
            return None
        
        # Если модель не передана, просто возвращаем response
        if model is None:
            return response
            
        try:
            response_json = response.json()
            self.helper.attach("response", response_json)
            # Проверяем статус только если он не 204
            if response.status_code != 204:
                assert response.status_code == status_code, f"Expected status {status_code}, got {response.status_code}: {response.text}"
            
            if isinstance(response_json, dict):
                return model(**response_json)
            elif isinstance(response_json, list):
                return [model(**item) for item in response_json]
        except json.JSONDecodeError:
            logger.warning(f"Could not parse JSON response: {response.text}")
            return response

    def get(self, model=None, endpoint=None, params=None, headers=None, success=None) -> None | BaseModel | list[BaseModel] | requests.Response:
        response = self._request("get", endpoint, params=params, headers=headers, success=success)
        if success and model:
            return self._validate_response(response=response, model=model)
        return response

    def post(self, model=None, endpoint=None, json=None, files=None, data=None, headers=None, success=None) -> None | BaseModel | list[BaseModel] | requests.Response:
        response = self._request("post", endpoint, json=json, data=data, headers=headers, files=files, success=success)
        if success and model:
            return self._validate_response(response=response, model=model)
        return response

    def patch(self, model=None, endpoint=None, json=None, headers=None, success=None) -> None | BaseModel | list[BaseModel] | requests.Response:
        response = self._request("patch", endpoint, json=json, headers=headers, success=success)
        if success and model:
            return self._validate_response(response=response, model=model)
        return response

    def delete(self, model=None, endpoint=None, headers=None, success=None) -> requests.Response:
        response = self._request("delete", endpoint, headers=headers, success=success)
        if success and model:
            return self._validate_response(response=response, model=model)
        return response










