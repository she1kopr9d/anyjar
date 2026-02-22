import requests
from typing import Optional, Dict, Any, List
from loguru import logger
from .config import config

class AnytypeAPI:
    def __init__(self):
        self.base_url = config.anytype_api_url
        self.api_key = config.anytype_api_key
        self.space_id = config.anytype_space_id
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def _request(self, method: str, endpoint: str, data: Optional[Dict] = None) -> Dict:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        try:
            response = requests.request(method, url, headers=self.headers, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"API request failed: {e}")
            return {"error": str(e)}
    
    def list_spaces(self) -> List[Dict]:
        """Получить список всех пространств"""
        result = self._request("GET", "spaces")
        return result.get("spaces", [])
    
    def create_object(self, name: str, type_key: str = "note", properties: Dict = None) -> Dict:
        """Создать новый объект"""
        data = {
            "name": name,
            "type_key": type_key,
            "layout": "basic",
            "properties": properties or []
        }
        return self._request("POST", f"spaces/{self.space_id}/objects", data)
    
    def search_objects(self, query: str, type_filter: str = None, limit: int = 10) -> List[Dict]:
        """Поиск объектов"""
        data = {
            "text": query,
            "limit": limit
        }
        if type_filter:
            data["type"] = type_filter
        
        result = self._request("POST", "search", data)
        return result.get("objects", [])
    
    def get_object(self, object_id: str) -> Dict:
        """Получить объект по ID"""
        return self._request("GET", f"spaces/{self.space_id}/objects/{object_id}")
    
    def update_object(self, object_id: str, updates: Dict) -> Dict:
        """Обновить объект"""
        return self._request("PATCH", f"spaces/{self.space_id}/objects/{object_id}", updates)
    
    def delete_object(self, object_id: str) -> Dict:
        """Удалить объект"""
        return self._request("DELETE", f"spaces/{self.space_id}/objects/{object_id}")

anytype_api = AnytypeAPI()

