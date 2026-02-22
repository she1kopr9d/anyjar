Вот полный README с подробной документацией и инструкциями по использованию программы:

```markdown
# 🤖 Anytype Telegram Bot с нейросетью

[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/python-3.11-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![OpenAI](https://img.shields.io/badge/OpenAI-412991.svg?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com)
[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://telegram.org)
[![Anytype](https://img.shields.io/badge/Anytype-5A67D8?style=for-the-badge&logo=anytype&logoColor=white)](https://anytype.io)

## 📋 Содержание
- [Описание проекта](#-описание-проекта)
- [Архитектура](#-архитектура)
- [Возможности](#-возможности)
- [Требования](#-требования)
- [Быстрый старт](#-быстрый-старт)
- [Детальная настройка](#-детальная-настройка)
- [Использование](#-использование)
- [API Endpoints](#-api-endpoints)
- [Команды для управления](#-команды-для-управления)
- [Безопасность](#-безопасность)
- [Мониторинг и логирование](#-мониторинг-и-логирование)
- [Бэкап и восстановление](#-бэкап-и-восстановление)
- [Масштабирование](#-масштабирование)
- [Устранение неполадок](#-устранение-неполадок)
- [Разработка](#-разработка)
- [Лицензия](#-лицензия)

## 🎯 Описание проекта

Этот проект представляет собой **интеллектуального Telegram-бота** для управления пространствами Anytype через нейросеть (OpenAI GPT). Бот позволяет взаимодействовать с Anytype на естественном языке: создавать задачи, заметки, искать объекты, управлять пространствами и многое другое.

### Ключевые особенности:
- 🧠 **Нейросеть-посредник** - преобразует человеческий язык в команды API
- 🔒 **Полная приватность** - все данные хранятся локально в Docker контейнерах
- 🐳 **Docker изоляция** - легкое развертывание и масштабирование
- 🔌 **API-first подход** - прямое общение с Anytype CLI через HTTP API
- 📱 **Telegram интерфейс** - удобное управление с любого устройства

## 🏗 Архитектура

```
┌─────────────────┐     ┌─────────────────────────────────────┐     ┌─────────────┐
│   Telegram      │     │         Docker Container            │     │  Anytype    │
│   Пользователь  │────▶│                                     │────▶│  Пространство│
└─────────────────┘     │  ┌─────────────┐   ┌───────────┐  │     └─────────────┘
         │              │  │ Telegram    │   │ Anytype   │  │            │
         │              │  │ Bot (Python)│──▶│ CLI Server│  │            │
         ▼              │  └──────┬──────┘   └───────────┘  │            │
┌─────────────────┐     │         │           │             │            │
│   Нейросеть     │     │    ┌────▼────┐      │             │            │
│   (OpenAI)      │◀────│────│   API    │◀────┘             │            │
└─────────────────┘     │    │  Client  │                    │            │
                        │    └──────────┘                    │            │
                        │                                     │            │
                        └─────────────────────────────────────┘            │
                                     ▲                                      │
                                     └──────────────────────────────────────┘
                                            Локальное пространство
                                                (только для бота)
```

### Компоненты системы:

1. **Anytype CLI Server** - запущенный в Docker сервер Anytype
2. **Telegram Bot** - Python бот, обрабатывающий сообщения
3. **OpenAI API** - преобразование текста в структурированные команды
4. **Anytype API Client** - HTTP клиент для общения с Anytype
5. **Бот-аккаунт** - специальный аккаунт Anytype с ограниченным доступом

## ✨ Возможности

### 📝 Управление объектами
| Команда | Описание | Пример |
|---------|----------|---------|
| `create_task` | Создание задачи | "Создай задачу купить молоко с высоким приоритетом" |
| `create_note` | Создание заметки | "Запиши идею для проекта" |
| `search` | Поиск объектов | "Найди все задачи со статусом 'В процессе'" |
| `get_object` | Просмотр объекта | "Покажи содержимое задачи ID 123" |
| `update_object` | Обновление объекта | "Обнови статус задачи на 'Готово'" |
| `delete_object` | Удаление объекта | "Удали заметку про встречу" |

### 🚀 Управление пространствами
| Команда | Описание | Пример |
|---------|----------|---------|
| `list_spaces` | Список пространств | "Покажи мои пространства" |
| `space_info` | Информация о пространстве | "Что в пространстве 'Работа'?" |
| `join_space` | Присоединение к пространству | "Подключись к пространству по ссылке" |

### 🧠 Интеллектуальные возможности
- Понимание контекста и намерений пользователя
- Автоматическое определение типа создаваемого объекта
- Обработка синонимов и разговорных фраз
- Поддержка множественных команд в одном сообщении
- Умный поиск с учетом семантики

## 📋 Требования

### Системные требования
- **ОС**: macOS 12+ / Linux / Windows 10+ (WSL2)
- **Процессор**: 2+ ядра
- **RAM**: 4+ GB
- **Диск**: 10+ GB свободного места
- **Docker**: 20.10+
- **Docker Compose**: 2.0+

### Необходимые аккаунты
- [Anytype](https://anytype.io) аккаунт
- [Telegram Bot Token](https://t.me/botfather)
- [OpenAI API Key](https://platform.openai.com/api-keys)

### Установка зависимостей (macOS)
```bash
# Установка Homebrew (если нет)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Установка Docker
brew install docker docker-compose

# Установка Git
brew install git

# Проверка установки
docker --version
docker-compose --version
git --version
```

## 🚀 Быстрый старт

### Шаг 1: Создание проекта
```bash
# Скачать скрипт создания проекта
curl -O https://raw.githubusercontent.com/your-repo/create-anytype-bot-project.sh

# Сделать исполняемым
chmod +x create-anytype-bot-project.sh

# Запустить создание проекта
./create-anytype-bot-project.sh ~/anytype-bot
```

### Шаг 2: Настройка переменных окружения
```bash
cd ~/anytype-bot

# Отредактировать .env файл
nano .env
```

Заполните файл:
```env
# Anytype API (заполните после создания аккаунта)
ANYTYPE_API_KEY=your_api_key_here
ANYTYPE_SPACE_ID=your_space_id_here

# Telegram
TG_BOT_TOKEN=your_telegram_bot_token
ALLOWED_USER_IDS=123456789,987654321  # Ваши Telegram ID

# OpenAI
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-4
```

### Шаг 3: Запуск контейнеров
```bash
# Запуск в фоне
docker-compose up -d

# Просмотр логов
docker-compose logs -f
```

### Шаг 4: Настройка аккаунта Anytype
```bash
# Создание бот-аккаунта
docker exec -it anytype-core anytype auth create my-tg-bot

# Создание API ключа
docker exec -it anytype-core anytype auth apikey create tg-bot-key

# Скопируйте полученный ключ в .env файл

# Перезапуск бота с новым ключом
docker-compose restart tg-bot
```

### Шаг 5: Подключение к пространству
```bash
# Получить ссылку-приглашение из Anytype Desktop
# (Settings → Spaces → Share → Copy invite link)

# Присоединиться к пространству
docker exec -it anytype-core anytype space join https://anytype.io/invite/...

# Проверить подключение
docker exec -it anytype-core anytype space list
```

## 🔧 Детальная настройка

### Настройка Telegram бота

1. **Создание бота через @BotFather**:
```
/newbot
Название: Anytype Bot
Username: anytype_bot

Сохраните полученный токен
```

2. **Получение своего Telegram ID**:
```bash
# Отправьте сообщение @userinfobot в Telegram
# Скопируйте ваш ID в .env
```

### Настройка OpenAI

1. **Получение API ключа**:
   - Перейдите на [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
   - Создайте новый ключ
   - Скопируйте в .env

2. **Выбор модели**:
   - `gpt-4` - лучшая точность, дороже
   - `gpt-3.5-turbo` - быстрее, дешевле
   - Можно указать в .env: `OPENAI_MODEL=gpt-4`

### Настройка Anytype Space

1. **Создание пространства для бота** (рекомендуется):
   - Создайте отдельное пространство в Anytype Desktop
   - Назовите его "TG Bot Space"
   - Это изолирует данные бота от ваших личных

2. **Генерация invite link**:
   - В пространстве нажмите Share
   - Copy invite link
   - Используйте для подключения бота

### Продвинутая конфигурация

#### Файл `docker-compose.override.yml`
```yaml
version: '3.8'

services:
  tg-bot:
    environment:
      - LOG_LEVEL=DEBUG  # Для отладки
      - BOT_MODE=webhook  # Режим webhook вместо polling
    volumes:
      - ./bot/src:/app/src  # Монтирование кода для разработки
```

#### Настройка webhook (для production)
```env
BOT_MODE=webhook
TG_BOT_WEBHOOK_URL=https://your-domain.com/webhook
TG_BOT_WEBHOOK_PORT=8443
```

## 📱 Использование

### Основные команды в Telegram

```
/start - Начать работу с ботом
/help - Показать справку
/spaces - Список пространств
/status - Статус системы
```

### Примеры запросов

#### 📌 Создание задач
```
"Создай задачу купить молоко"
"Добавь задачу позвонить маме с высоким приоритетом"
"Запланируй встречу на завтра в 15:00"
"Создай задачу 'Написать отчет' со статусом 'В процессе'"
```

#### 📝 Работа с заметками
```
"Запиши идею для нового проекта"
"Создай заметку с заголовком 'Встреча с командой' и текстом 'Обсудили спринт'"
"Добавь в заметку 'Идеи' пункт про нейросети"
```

#### 🔍 Поиск и просмотр
```
"Найди все задачи со статусом 'Активно'"
"Покажи содержимое пространства 'Работа'"
"Что у меня запланировано на сегодня?"
"Найди заметки про отпуск"
```

#### 🔄 Обновление и удаление
```
"Обнови задачу 'Купить молоко' на 'Выполнено'"
"Поменяй статус задачи ID 123 на 'Готово'"
"Удали задачу про встречу"
"Перенеси задачу 'Позвонить' на завтра"
```

### Множественные команды
```
"Создай задачу купить хлеб и запиши заметку про ужин"
"Найди все задачи с высоким приоритетом и покажи их статусы"
```

## 🌐 API Endpoints

### Anytype API (внутренний)

| Endpoint | Метод | Описание | Параметры |
|----------|-------|----------|-----------|
| `/api/v1/spaces` | GET | Список пространств | - |
| `/api/v1/spaces/{id}` | GET | Информация о пространстве | `id` - ID пространства |
| `/api/v1/spaces/{id}/objects` | POST | Создать объект | `name`, `type_key`, `properties` |
| `/api/v1/search` | POST | Поиск объектов | `text`, `type`, `limit` |
| `/api/v1/spaces/{id}/objects/{objId}` | GET | Получить объект | `id` - ID пространства, `objId` - ID объекта |
| `/api/v1/spaces/{id}/objects/{objId}` | PATCH | Обновить объект | `id`, `objId`, `updates` |
| `/api/v1/spaces/{id}/objects/{objId}` | DELETE | Удалить объект | `id`, `objId` |

### Примеры запросов

```bash
# Получение списка пространств
curl -H "Authorization: Bearer $ANYTYPE_API_KEY" \
     http://localhost:31012/api/v1/spaces

# Создание задачи
curl -X POST \
     -H "Authorization: Bearer $ANYTYPE_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{
       "name": "Купить молоко",
       "type_key": "task",
       "properties": {
         "status": "To Do",
         "priority": "High"
       }
     }' \
     http://localhost:31012/api/v1/spaces/space_id/objects

# Поиск объектов
curl -X POST \
     -H "Authorization: Bearer $ANYTYPE_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{"text": "проект", "limit": 10}' \
     http://localhost:31012/api/v1/search
```

## 🛠 Команды для управления

### Базовые команды Docker
```bash
# Запуск проекта
docker-compose up -d

# Остановка проекта
docker-compose down

# Перезапуск
docker-compose restart

# Просмотр логов
docker-compose logs -f
docker-compose logs -f tg-bot
docker-compose logs -f anytype-server

# Масштабирование (если нужно несколько ботов)
docker-compose up -d --scale tg-bot=3
```

### Управление Anytype CLI
```bash
# Вход в контейнер
docker exec -it anytype-core sh

# Создание аккаунта
docker exec -it anytype-core anytype auth create bot-name

# Создание API ключа
docker exec -it anytype-core anytype auth apikey create key-name

# Список API ключей
docker exec -it anytype-core anytype auth apikey list

# Подключение к пространству
docker exec -it anytype-core anytype space join INVITE_LINK

# Список пространств
docker exec -it anytype-core anytype space list

# Проверка статуса
docker exec -it anytype-core anytype auth status
```

### Обслуживание
```bash
# Очистка неиспользуемых ресурсов
docker system prune -f

# Просмотр использования диска
docker system df

# Бэкап данных
./scripts/backup-data.sh

# Восстановление из бэкапа
tar -xzf backups/20240101_120000/anytype-data.tar.gz -C /var/lib/docker/volumes/anytype-data-volume/_data

# Обновление образов
docker-compose pull
docker-compose up -d --build
```

## 🔒 Безопасность

### Принципы безопасности

1. **Изоляция данных**
   - Бот-аккаунт имеет доступ только к приглашенным пространствам
   - Данные хранятся локально в Docker volumes
   - Нет передачи данных на внешние серверы (кроме OpenAI)

2. **Аутентификация**
   - API ключи для доступа к Anytype
   - Telegram ID для ограничения доступа к боту
   - OpenAI ключ для нейросети

3. **Рекомендации**
   - Регулярно обновляйте API ключи
   - Используйте отдельное пространство для бота
   - Ограничьте доступ по Telegram ID
   - Делайте регулярные бэкапы

### Файл .env (никогда не коммитьте!)
```env
# ❌ Никогда не публикуйте эти данные
ANYTYPE_API_KEY=sk_live_...  # Секретный ключ
TG_BOT_TOKEN=123456:ABC...    # Токен бота
OPENAI_API_KEY=sk-...         # Ключ OpenAI
```

### Проверка безопасности
```bash
# Проверка, кто имеет доступ к боту
docker-compose exec tg-bot python -c "
from src.config import config
print(f'Allowed users: {config.allowed_user_ids}')
"

# Проверка активных API ключей
docker exec -it anytype-core anytype auth apikey list
```

## 📊 Мониторинг и логирование

### Просмотр логов
```bash
# Все логи
docker-compose logs -f

# Логи только бота
docker-compose logs -f tg-bot

# Логи только Anytype
docker-compose logs -f anytype-server

# Логи с временными метками
docker-compose logs -f --timestamps

# Поиск в логах
docker-compose logs | grep ERROR
docker-compose logs | grep "User 123"
```

### Метрики
```python
# Встроенный Prometheus endpoint
curl http://localhost:8080/metrics

# Метрики включают:
# - Количество обработанных сообщений
# - Время ответа нейросети
# - Количество API вызовов
# - Ошибки по типам
```

### Настройка мониторинга
```yaml
# Добавить в docker-compose.yml
  prometheus:
    image: prom/prometheus
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
    ports:
      - "9090:9090"

  grafana:
    image: grafana/grafana
    ports:
      - "3000:3000"
```

## 💾 Бэкап и восстановление

### Автоматический бэкап
```bash
# Создать бэкап
./scripts/backup-data.sh

# Добавить в cron (ежедневный бэкап)
0 2 * * * /Users/username/anytype-bot/scripts/backup-data.sh
```

### Структура бэкапа
```
backups/
├── 20240101_120000/
│   ├── anytype-data.tar.gz     # Данные аккаунта
│   ├── anytype-config.tar.gz    # Конфигурация
│   └── metadata.json            # Информация о бэкапе
└── 20240102_120000/
    └── ...
```

### Восстановление
```bash
# Остановить контейнеры
docker-compose down

# Восстановить данные
docker run --rm -v anytype-data-volume:/data alpine sh -c "tar xzf - -C /data" < backups/20240101_120000/anytype-data.tar.gz

# Запустить заново
docker-compose up -d
```

## 📈 Масштабирование

### Горизонтальное масштабирование
```yaml
# docker-compose.yml
  tg-bot:
    deploy:
      replicas: 3
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
```

### Вертикальное масштабирование
```bash
# Увеличить лимиты для конкретного сервиса
docker update --cpus=2 --memory=2G anytype-core
```

### Оптимизация производительности
```bash
# Настройка лимитов в docker-compose.yml
services:
  anytype-server:
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 2G
        reservations:
          cpus: '1'
          memory: 1G
```

## 🔧 Устранение неполадок

### Проблемы с запуском

#### ❌ Docker контейнеры не стартуют
```bash
# Проверка логов
docker-compose logs

# Проверка портов
lsof -i :31012
lsof -i :8080

# Пересборка с очисткой
docker-compose down -v
docker-compose up -d --build
```

#### ❌ Бот не отвечает в Telegram
```bash
# Проверка токена
docker-compose exec tg-bot python -c "
from src.config import config
print(f'Bot token: {config.tg_bot_token[:10]}...')
"

# Проверка подключения к Telegram API
curl https://api.telegram.org/bot$TG_BOT_TOKEN/getMe
```

### Проблемы с Anytype

#### ❌ Не удается создать аккаунт
```bash
# Проверка соединения с Anytype
docker exec -it anytype-core anytype version

# Очистка данных и повторная попытка
docker-compose down -v
docker-compose up -d
docker exec -it anytype-core anytype auth create my-bot
```

#### ❌ API ключ не работает
```bash
# Проверка существующих ключей
docker exec -it anytype-core anytype auth apikey list

# Создание нового ключа
docker exec -it anytype-core anytype auth apikey create new-key

# Тест ключа
curl -H "Authorization: Bearer NEW_KEY" http://localhost:31012/api/v1/spaces
```

### Проблемы с нейросетью

#### ❌ OpenAI возвращает ошибки
```bash
# Проверка баланса OpenAI
curl https://api.openai.com/v1/dashboard/billing/usage \
     -H "Authorization: Bearer $OPENAI_API_KEY"

# Тест API
curl https://api.openai.com/v1/chat/completions \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer $OPENAI_API_KEY" \
     -d '{
       "model": "gpt-3.5-turbo",
       "messages": [{"role": "user", "content": "Hello"}]
     }'
```

### Логирование ошибок

```python
# Пример расширенного логирования в bot.py
import traceback
from loguru import logger

try:
    # какой-то код
    pass
except Exception as e:
    logger.error(f"Error: {e}")
    logger.error(f"Traceback: {traceback.format_exc()}")
    logger.error(f"Context: user={user_id}, message={user_message}")
```

## 💻 Разработка

### Локальная разработка без Docker

```bash
# Создание виртуального окружения
python3 -m venv venv
source venv/bin/activate

# Установка зависимостей
cd bot
pip install -r requirements.txt

# Запуск бота локально
export $(cat ../.env | xargs)
python -m src.bot
```

### Добавление новых команд

1. **Обновить промпт в `ai_handler.py`**:
```python
self.system_prompt += """
8. create_project - создать проект
   Формат: {"action": "create_project", "name": "название", "deadline": "дата"}
"""
```

2. **Добавить обработчик в `bot.py`**:
```python
elif action == "create_project":
    obj = anytype_api.create_object(
        name=command["name"],
        type_key="project",
        properties={"deadline": command.get("deadline")}
    )
    return f"✅ Проект '{command['name']}' создан"
```

3. **Обновить документацию**

### Тестирование

```bash
# Unit тесты
cd bot
python -m pytest tests/

# Интеграционные тесты
./scripts/test-api.sh

# Нагрузочное тестирование
ab -n 1000 -c 10 http://localhost:31012/api/v1/spaces
```

## 📚 Дополнительные ресурсы

### Документация
- [Anytype CLI GitHub](https://github.com/anyproto/anytype-cli)
- [Anytype Developer Portal](https://developers.anytype.io)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [OpenAI API](https://platform.openai.com/docs)

### Сообщество
- [Anytype Community](https://community.anytype.io)
- [Telegram Chat](https://t.me/anytype)
- [Discord](https://discord.gg/anytype)

## 📄 Лицензия

MIT License

Copyright (c) 2024 Anytype TG Bot

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## 🙏 Благодарности

- Anytype за отличную платформу и открытое API
- OpenAI за мощные языковые модели
- Сообществу Anytype за поддержку и идеи

---

**✨ Готово! У вас есть полностью документированный проект с подробными инструкциями по всем аспектам использования.**
```

Этот README включает:

1. **Полное описание проекта** - что это и зачем
2. **Детальная архитектура** - как все работает
3. **Все возможности** - что умеет бот
4. **Пошаговая инструкция** - от установки до запуска
5. **API документация** - все эндпоинты
6. **Команды управления** - полный список
7. **Безопасность** - рекомендации и практики
8. **Мониторинг** - как следить за системой
9. **Бэкапы** - как сохранять данные
10. **Масштабирование** - как расширять
11. **Устранение неполадок** - решение проблем
12. **Разработка** - как дорабатывать
13. **Лицензия** - юридическая информация

Теперь у тебя есть **полная документация** для любого пользователя или разработчика! 🎉