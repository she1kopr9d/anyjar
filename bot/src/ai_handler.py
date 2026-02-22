import openai
import json
from typing import Dict, Any
from loguru import logger
from .config import config

class AIHandler:
    def __init__(self):
        openai.api_key = config.openai_api_key
        self.model = config.openai_model
        
        self.system_prompt = """
        Ты помощник, который преобразует команды пользователя в JSON для Anytype API.
        
        Доступные действия:
        1. create_task - создать задачу
           Формат: {"action": "create_task", "name": "название", "priority": "High/Medium/Low", "description": "описание"}
        
        2. create_note - создать заметку
           Формат: {"action": "create_note", "name": "заголовок", "content": "текст заметки"}
        
        3. search - поиск объектов
           Формат: {"action": "search", "query": "что искать", "type": "task/page/note"}
        
        4. list_spaces - показать пространства
           Формат: {"action": "list_spaces"}
        
        5. update_object - обновить объект
           Формат: {"action": "update", "object_id": "id", "changes": {"name": "новое имя", "status": "новый статус"}}
        
        6. delete_object - удалить объект
           Формат: {"action": "delete", "object_id": "id"}
        
        7. get_object - получить информацию об объекте
           Формат: {"action": "get", "object_id": "id"}
        
        Ответь ТОЛЬКО JSON без пояснений.
        """
    
    def process_command(self, user_message: str) -> Dict[str, Any]:
        """Преобразует текстовую команду в JSON для API"""
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": user_message}
                ],
                temperature=0.3,
                max_tokens=300
            )
            
            result = response.choices[0].message.content
            # Очищаем от возможных markdown-обрамлений
            if result.startswith("```json"):
                result = result.replace("```json", "").replace("```", "")
            elif result.startswith("```"):
                result = result.replace("```", "")
            
            return json.loads(result.strip())
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse AI response: {e}")
            return {"action": "error", "message": "Не удалось распознать команду"}
        except Exception as e:
            logger.error(f"AI processing failed: {e}")
            return {"action": "error", "message": f"Ошибка обработки: {str(e)}"}

ai_handler = AIHandler()

