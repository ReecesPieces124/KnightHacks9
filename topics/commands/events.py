import json
import os
from datetime import datetime

import discord
from dotenv import load_dotenv

load_dotenv()

# ////////////////////////////////////////////////////////////////////////////////////

# EVENTS
# Read from the EVENTS variable in .env. It is a JSON dict of:
#   "Event name" : {"type": "quiz", "date": "DayOfWeek Month Date"}
# "type" is one of: quiz, test, exam and selects which command shows the event
# ("next quiz" / "next test" / "next exam").
# A plain string date is also accepted; the type is then inferred from the event name.
# Example:
#   EVENTS={"Quiz 3": {"type": "quiz", "date": "Monday Nov 9"}, "Midterm": {"type": "test", "date": "Saturday Oct 17"}}

def load_events() -> dict:
    raw = os.getenv("EVENTS", "").strip()
    if not raw:
        return {}

    try:
        data = json.loads(raw)
    except (ValueError, TypeError):
        return {}

    return data if isinstance(data, dict) else {}

# ////////////////////////////////////////////////////////////////////////////////////

# ACCEPTED DATE FORMATS (WEEKDAY MAY BE FULL, ABBREVIATED, OR OMITTED)
date_formats : tuple = ("%a %b %d", "%A %b %d", "%b %d")

# PARSE "Wed Sep 24" INTO THE NEXT OCCURRENCE FROM NOW
def next_occurrence(value : str, now : datetime) -> datetime:
    text = str(value).strip()

    parsed = None
    for date_format in date_formats:
        try:
            parsed = datetime.strptime(text, date_format)
            break
        except (ValueError, TypeError):
            continue

    if parsed is None:
        return None

    # NO YEAR IN THE FORMAT, SO ASSUME THE CURRENT YEAR AND ROLL OVER IF PASSED
    try:
        candidate = parsed.replace(year=now.year)
        if candidate.date() < now.date():
            candidate = parsed.replace(year=now.year + 1)
    except ValueError:
        return None

    return candidate

# ////////////////////////////////////////////////////////////////////////////////////

# EVENT DATE FROM AN ENTRY
def event_date(value) -> str:
    if isinstance(value, dict):
        return str(value.get("date", ""))
    return str(value)

# EVENT TYPE FROM AN ENTRY (EXPLICIT, ELSE INFERRED FROM THE NAME)
def event_type(name : str, value) -> str:
    if isinstance(value, dict) and value.get("type"):
        return str(value["type"]).strip().lower()

    lowered = name.lower()
    for kind in ("quiz", "test", "exam"):
        if kind in lowered:
            return kind
    return ""

# ////////////////////////////////////////////////////////////////////////////////////

# SEND THE CHRONOLOGICALLY NEXT EVENT OF THE GIVEN TYPE
# Tests and exams are the same thing, so "next test" and "next exam" match either.
async def next_event(message : discord.Message, event_type_filter : str = None):
    events = load_events()

    accepted : tuple = ()
    if event_type_filter:
        accepted = ("test", "exam") if event_type_filter in ("test", "exam") else (event_type_filter,)

    now = datetime.now()
    upcoming = []
    for name, value in events.items():
        if accepted and event_type(name, value) not in accepted:
            continue

        when = next_occurrence(event_date(value), now)
        if when is not None:
            upcoming.append((when, name))

    if not upcoming:
        if event_type_filter:
            await message.channel.send(f"No upcoming {event_type_filter} on the schedule")
        return

    when, name = min(upcoming, key=lambda item: item[0])
    days = (when.date() - now.date()).days

    await message.channel.send(f'**{name}** is on {when.strftime("%b %d")} (in {days} {"day" if days == 1 else "days"})')
