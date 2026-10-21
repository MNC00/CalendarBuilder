
from datetime import datetime, timedelta
import yaml

def load_events(path: str) -> list:
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return [(e["title"], e["description"], e["start"], e["duration"], e.get("location", "")) for e in data["events"]]


def ics_escape(text: str) -> str:
    text = text.replace("\u2019", "'")
    return text.replace("\\", "\\\\").replace(",", "\\,").replace(";", "\\;").replace("\n", "\\n")


def fold_line(line: str, limit: int = 75) -> str:
    folded_lines = []
    current_line = ""
    current_bytes = 0

    for char in line:
        char_bytes = len(char.encode("utf-8"))
        if current_bytes + char_bytes > limit:
            folded_lines.append(current_line)
            current_line = " " + char
            current_bytes = 1 + char_bytes
        else:
            current_line += char
            current_bytes += char_bytes

    folded_lines.append(current_line)
    return "\r\n".join(folded_lines)


def build_event(uid, title, desc, start_str, duration_min, location) -> list:
    dt_local = datetime.strptime(start_str, "%d/%m/%Y %H:%M")
    dt_utc = dt_local - timedelta(hours=1)
    dt_end_utc = dt_utc + timedelta(minutes=duration_min)
    lines = [
        "BEGIN:VEVENT",
        f"UID:{uid}@partite-roma",
        f"DTSTAMP:{datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}",
        f"DTSTART:{dt_utc.strftime('%Y%m%dT%H%M%SZ')}",
        f"DTEND:{dt_end_utc.strftime('%Y%m%dT%H%M%SZ')}",
        f"SUMMARY:{ics_escape(title)}",
        f"DESCRIPTION:{ics_escape(desc)}",
        f"LOCATION:{ics_escape(location)}",
        "END:VEVENT",
    ]
    return [fold_line(line) for line in lines]