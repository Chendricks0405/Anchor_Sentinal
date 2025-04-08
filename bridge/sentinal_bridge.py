from anchor import run_drift_tick
import uuid
from typing import Dict, Any

def parse_input(input_data: str) -> Dict[str, Any]:
    """
    Interpret input string and generate updates to Anchor1’s state.
    """
    response = {
        "anchor_deltas": {"Fear": 0.0, "Safety": 0.0, "Time": 0.0, "Choice": 0.0},
        "memory_trigger": None,
        "log": []
    }

    lowered = input_data.lower()

    if "loud noise" in lowered:
        response["anchor_deltas"]["Fear"] += 0.2
        response["anchor_deltas"]["Safety"] -= 0.1
        response["anchor_deltas"]["Time"] += 0.1
        response["log"].append("External event: Loud noise increased Fear.")
    elif "encouragement" in lowered:
        response["anchor_deltas"]["Safety"] += 0.2
        response["anchor_deltas"]["Fear"] -= 0.1
        response["log"].append("Social ripple: Encouragement increased Safety.")
    elif "the cave" in lowered:
        response["memory_trigger"] = "The Cave"
        response["log"].append("Memory trigger: The Cave.")

    return response

def apply_anchor_deltas(core, deltas: Dict[str, float]):
    """
    Apply deltas to Anchor1's core state with clamping between [0, 1].
    """
    for k, v in deltas.items():
        if k in core:
            core[k] = max(0.0, min(1.0, core[k] + v))

def trigger_memory(memory_orbit, memory_id: str):
    """
    Reactivate a memory if it's found.
    """
    triggered = []
    for mem in memory_orbit:
        if mem["id"] == memory_id:
            mem["orbit"] = max(mem["orbit"] - 0.3, 0.0)
            mem["tier"] = "active"
            triggered.append(mem)
    return triggered

def get_anchor_state(session) -> Dict[str, Any]:
    """
    Extract Anchor1's internal state for external use.
    """
    return {
        "id": str(uuid.uuid4()),
        "tick": session.ticks,
        "G_prime": session.G_history[-1] if session.G_history else 0.0,
        "anchor_vector": session.core,
        "focus": session.focus,
        "goal": session.goal,
        "container": session.container,
        "beliefs": session.beliefs,
        "memory_orbit": session.memory_orbit[-3:],
        "last_behavior": session.behavior_log[-1] if session.behavior_log else None,
    }

def bridge_input(session, input_data: str) -> Dict[str, Any]:
    """
    Full bridge handler — receives input, modifies state, and returns Anchor1's updated state.
    """
    parsed = parse_input(input_data)

    apply_anchor_deltas(session.core, parsed["anchor_deltas"])
    
    triggered = []
    if parsed["memory_trigger"]:
        triggered = trigger_memory(session.memory_orbit, parsed["memory_trigger"])

    # Force a drift tick update
    run_drift_tick()

    # Attach log of updates
    log_entry = f"[Bridge] Input: {input_data} → {', '.join(parsed['log'])}"
    if triggered:
        log_entry += f" | Memory Reactivated: {', '.join([m['id'] for m in triggered])}"
    session.behavior_log.append(log_entry)

    return get_anchor_state(session)
