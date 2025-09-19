# Telegram FX Signals Bot (Railway)

## Included
- `main_full_bot_signals_multi_rl.py` — main bot with signals & rate limiting
- `Procfile` — defines Railway worker start
- `requirements.txt` — dependencies
- `runtime.txt` — force Railway to use Python 3.11.9 (fix imghdr error)
- `README.md` — instructions

## Railway Variables
- `TELEGRAM_BOT_TOKEN` — token from BotFather
- `TWELVE_DATA_KEY` — TwelveData API key
- optional: `TD_RATE_LIMIT_PER_MIN` (default 8)

## Deploy
1. Push these files to GitHub repo.
2. On Railway: New Project → Deploy from GitHub → select repo.
3. Add Variables above.
4. Redeploy.
5. In Telegram: /start

Python version is pinned to 3.11.9 via `runtime.txt`.
