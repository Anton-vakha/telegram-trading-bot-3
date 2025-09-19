import os, re, requests
t = os.getenv("TELEGRAM_BOT_TOKEN","").strip()
print("[ENV_PRESENT]", bool(t), "[LEN]", len(t), "[HAS_COLON]", (":" in t))
print("[HEAD]", repr(t[:8]), "[TAIL]", repr(t[-8:]))
fmt_ok = bool(re.match(r"^\d+:[A-Za-z0-9_-]{35}$", t))
print("FORMAT_OK:", fmt_ok)
if t:
    r = requests.get(f"https://api.telegram.org/bot{t}/getMe", timeout=10)
    print("GETME:", r.status_code, r.text[:160])
else:
    print("GETME: NO_TOKEN")
