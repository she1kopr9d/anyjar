#!/bin/bash
set -e

echo "========================================="
echo "🚀 Anytype CLI Server"
echo "Версия: $(anytype version)"
echo "========================================="

if [ ! -f /root/.anytype/account.json ]; then
    echo "🔧 Аккаунт не найден. Запускаем первый вход..."
    echo "⚠️  Для первого запуска выполните:"
    echo "   docker exec -it anytype-core anytype auth create my-bot"
    echo "   docker exec -it anytype-core anytype auth apikey create tg-bot-key"
else
    echo "✅ Аккаунт найден"
fi

echo "📡 Запускаем сервер на 0.0.0.0:31012"
echo "========================================="

exec anytype serve --listen-address 0.0.0.0:31012

