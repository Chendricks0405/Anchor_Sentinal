# log_parser.py — Converts syslog.csv entries into Anchor1 input events

import csv
from bridge.bridge import bridge_input, get_anchor_state
from bridge.bridge_utils import load_memory, initialize_anchor1_memory

class Session:
    def __init__(self):
        self.core = {"Fear": 0.3, "Safety": 0.7, "Time": 0.2, "Choice": 0.4}
        self.focus = "Network"
        self.container = "Corporate LAN"
        self.goal = "Maintain System Integrity"
        self.beliefs = {
            "System stability is critical": 1.0,
            "External IPs are often threats": 0.8
        }
        self.memory_orbit = []
        self.container_links = {"Corporate LAN": {"DMZ": 0.5}}
        self.G_history = []
        self.behavior_log = []
        self.ticks = 0

session = Session()

# Load memory
memories = load_memory("memory/memory_containers.json")
initialize_anchor1_memory(session, memories)

with open("ingest/syslog.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        input_string = f"{row['event_type']} detected from {row['source']} targeting {row['target_asset']} - {row['raw_description']}"
        updated_state = bridge_input(session, input_string)
        print(f"EVENT: {input_string}")
        print(get_anchor_state(session))
        print("------")
