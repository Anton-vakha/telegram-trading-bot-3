# Telegram FX Signals Bot (Railway)

## Что входит
- `main_full_bot_signals_multi_rl.py` — основной бот с rate-limiter и фильтрами сигналов
- `Procfile` — запуск worker-а на Railway
- `requirements.txt` — зависимости

## Переменные окружения (Railway → Variables)
- `TELEGRAM_BOT_TOKEN` — токен бота из BotFather
- `TWELVE_DATA_KEY` — API ключ TwelveData
- (опционально) `TD_RATE_LIMIT_PER_MIN` — лимит запросов в минуту (по умолчанию 8)

## Деплой
1. Создать репозиторий на GitHub и загрузить эти три файла.
2. На Railway: New Project → Deploy from GitHub → выбрать репозиторий.
3. В разделе Variables добавить переменные указаные выше.
4. Нажать *Redeploy*.
5. В Telegram написать боту команду `/start`.

## Команды
- `/start` — включить сигналы
- `/stop` — выключить сигналы
- `/stats` — простая статистика
- `/pairs` — управление списком валютных пар
  - `/pairs list`
  - `/pairs add EUR_USD USDJPY` (поддерживаются `_` и `/`)
  - `/pairs remove EUR_USD`
  - `/pairs set EUR_USD GBP_USD ...`
  - `/pairs clear`

## Примечания
- TwelveData отдаёт время в UTC. Для локального времени можно добавить конвертацию в функции `compute_entry_time`.
- Rate limiter не позволит превышать бесплатные 8 запросов/минуту.
