"""
Клиент для работы с API курьеров.

Класс CourierAPIClient заменяет процедурные функции из helpers.py:
конфигурация (base_url, auth_token) передаётся один раз через конструктор,
а не читается из глобальных переменных окружения.
"""
import requests


class CourierAPIClient:
    """Клиент API курьеров: получение, создание и удаление курьеров."""

    def __init__(self, base_url, auth_token):
        self.base_url = base_url
        self.auth_token = auth_token

    def _get_auth_header(self):
        """Возвращает заголовок авторизации (для внутреннего использования)."""
        if not self.auth_token:
            raise ValueError("AUTH_TOKEN не задан")
        return {"Authorization": f"Bearer {self.auth_token}"}

    def get_courier_by_id(self, courier_id):
        """Получает данные курьера по ID."""
        url = f"{self.base_url}/couriers/{courier_id}"
        headers = self._get_auth_header()
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def create_courier(self, data):
        """Создаёт нового курьера."""
        url = f"{self.base_url}/couriers"
        headers = self._get_auth_header()
        headers["Content-Type"] = "application/json"
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()

    def delete_courier(self, courier_id):
        """Удаляет курьера по ID."""
        url = f"{self.base_url}/couriers/{courier_id}"
        headers = self._get_auth_header()
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return response.json()