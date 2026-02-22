#!/bin/bash
BACKUP_DIR="./backups/$(date +%Y%m%d_%H%M%S)"
mkdir -p $BACKUP_DIR

echo "📦 Бэкап данных Anytype..."

docker run --rm -v anytype-data-volume:/data alpine tar czf - -C /data . > $BACKUP_DIR/anytype-data.tar.gz
docker run --rm -v anytype-config-volume:/config alpine tar czf - -C /config . > $BACKUP_DIR/anytype-config.tar.gz

echo "✅ Бэкап сохранен в $BACKUP_DIR"
echo "   Размер: $(du -sh $BACKUP_DIR | cut -f1)"

