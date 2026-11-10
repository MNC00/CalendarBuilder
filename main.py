
import os
import src.utilities as ut

INPUT_PATH = os.path.join(os.path.dirname(__file__), "InputFile_UNIeTRINI.yaml")
OUTPUT_FILE = "CalendarioUNIeTRINI.ics"


# INPUT LOAD
events = ut.load_events(INPUT_PATH)

# ICS BUILDING
ics_lines = [
    "BEGIN:VCALENDAR",
    "VERSION:2.0",
    "PRODID:-//Calendario Partite CSI Roma//IT",
]

for i, event in enumerate(events, 1):
    ics_lines.extend(ut.build_event(i, *event))

ics_lines.append("END:VCALENDAR")

content = "\r\n".join(ics_lines) + "\r\n"

# EXPORT FILE FINALE    
path = os.path.join(os.path.dirname(__file__), "output", OUTPUT_FILE)
os.makedirs(os.path.dirname(path), exist_ok=True)

with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(content)

print(f"Creato file completo: {path}")
