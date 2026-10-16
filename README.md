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

Set upcoming dates in `.env` so the bot can answer `ta next quiz`, `ta next test`, and `ta next exam` (each shows the next event of that type):

```
EVENTS={"Quiz 3": {"type": "quiz", "date": "Monday Nov 9"}, "The Midterm": {"type": "test", "date": "Saturday Oct 17"}, "The Final Exam": {"type": "exam", "date": "Saturday Dec 5"}}
```

- `type` is `quiz`, `test`, or `exam` and picks which command shows the event. Tests and exams are treated as the same thing, so `next test` and `next exam` both return the nearest test/exam; `next quiz` is separate.
- `date` is `DayOfWeek Month Date` (no year). The weekday may be full (`Saturday`), abbreviated (`Sat`), or omitted. Dates that have already passed roll over to next year automatically.
- A plain string date is also accepted, in which case the type is inferred from the event name.
