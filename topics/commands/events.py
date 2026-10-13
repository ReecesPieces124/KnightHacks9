import json
import os
from datetime import datetime

import discord
from dotenv import load_dotenv

load_dotenv()

# ////////////////////////////////////////////////////////////////////////////////////

# EVENTS
# Read from the EVENTS variable in .env. It is a JSON dict of:
#   "Event name" : "DayOfWeek Month Date"
# Example:
#   EVENTS={"Quiz 4": "Wed Oct 22", "Test 2": "Mon Nov 3", "Final Exam": "Mon Dec 8"}

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

# SEND THE CHRONOLOGICALLY NEXT EVENT
async def next_event(message : discord.Message):
    events = load_events()
    if not events:
        return False

    now = datetime.now()
    upcoming = [
        (when, name)
        for name, value in events.items()
        if (when := next_occurrence(str(value), now)) is not None
    ]

    if not upcoming:
        return False

    when, name = min(upcoming, key=lambda item: item[0])
    days = (when.date() - now.date()).days

    await message.channel.send(f'**{name}** is on {when.strftime("%b %d")} (in {days} {"day" if days == 1 else "days"})')
