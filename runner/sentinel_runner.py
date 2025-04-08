# sentinel_runner.py — Anchor1 Sentinel Drift Simulation

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
        self.container_links = {"Corporate LAN": {"DMZ": 0.5}, "DMZ": {"Corporate LAN": 0.5}}
        self.G_history = []
        self.behavior_log = []
        self.ticks = 0

session = Session()

# Load memory containers
memories = load_memory("memory_containers.json")
initialize_anchor1_memory(session, memories)

# Simulated input (threat observation)
input_event = "Unusual login from new IP address detected."

# Run perception update
updated_state = bridge_input(session, input_event)

# Print the updated state
print("Anchor1 Sentinel State:")
for k, v in updated_state.items():
    print(f"{k}: {v}")
