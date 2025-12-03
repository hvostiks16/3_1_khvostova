import requests

class NetworkHelper:
    BASE_URL = "http://127.0.0.1:8001/api/"
    TOKEN = "07a74909f9d572d92a91b6b17648cfa85eebb5aa"

    @staticmethod
    def _headers():
        return {
            "Authorization": f"Token {NetworkHelper.TOKEN}",
            "Content-Type": "application/json",
        }

    @staticmethod
    def get_list(resource: str):
        url = f"{NetworkHelper.BASE_URL}{resource}/"
        response = requests.get(url, headers=NetworkHelper._headers())
        response.raise_for_status()
        return response.json()

    @staticmethod
    def get_item(resource: str, item_id: int):
        url = f"{NetworkHelper.BASE_URL}{resource}/{item_id}/"
        response = requests.get(url, headers=NetworkHelper._headers())
        response.raise_for_status()
        return response.json()

    @staticmethod
    def create_item(resource: str, data: dict):
        url = f"{NetworkHelper.BASE_URL}{resource}/"
        response = requests.post(url, json=data, headers=NetworkHelper._headers())
        response.raise_for_status()
        return response.json()

    @staticmethod
    def update_item(resource: str, item_id: int, data: dict):
        url = f"{NetworkHelper.BASE_URL}{resource}/{item_id}/"
        response = requests.put(url, json=data, headers=NetworkHelper._headers())
        response.raise_for_status()
        return response.json()

    @staticmethod
    def patch_item(resource: str, item_id: int, data: dict):
        url = f"{NetworkHelper.BASE_URL}{resource}/{item_id}/"
        response = requests.patch(url, json=data, headers=NetworkHelper._headers())
        response.raise_for_status()
        return response.json()

    @staticmethod
    def delete_item(resource: str, item_id: int):
        url = f"{NetworkHelper.BASE_URL}{resource}/{item_id}/"
        response = requests.delete(url, headers=NetworkHelper._headers())
        if response.status_code in (200, 204):
            return True
        response.raise_for_status()
        return False

