# TAbot

The modular discord bot

## How to Edit

- Edit responses in `responses.py`
- Edit settings in `config.py`
- Addon example found in `addons/example.py`

## How to Run

- Create file `.env` with `DISCORD_TOKEN="YOUR TOKEN"` inside with your bot token
- Execute `run.sh` to run bot

## Events

Set upcoming dates in `.env` so the bot can answer `ta next quiz`, `ta next test`, and `ta next exam`:

```
EVENTS={"Quiz 4": "Wed Oct 22", "Test 2": "Mon Nov 3", "Final Exam": "Mon Dec 8"}
```

Each value is `DayOfWeek Month Date` (no year). The weekday may be full (`Saturday`), abbreviated (`Sat`), or omitted. Dates that have already passed roll over to next year automatically.
