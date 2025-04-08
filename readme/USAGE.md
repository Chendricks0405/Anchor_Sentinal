# Anchor1 Usage Manual

This document explains how to use Anchor1’s core perceptual tools, from memory setup to lens configuration and bridge integration. Whether you're using it as a standalone simulation engine or integrating with an LLM, the structure is modular and simple to operate.

---

## 1. Memory Configuration

Memory containers define Anchor1’s emotional and contextual influence over time. Each memory exists as a JSON object and should be placed in `/memory/memory_containers.json`.

### Memory Format

```json
{
  "id": "Unusual login from new IP",
  "EQ": 0.8,
  "orbit": 0.2,
  "tier": "active",
  "focus_lens": ["Network", "Behavior"]
}
```

### Fields:
- `id`: Unique name or description of the memory
- `EQ`: Emotional Quotient (how strongly it resonates)
- `orbit`: How close it is to being relevant (0 = high priority, 1 = almost forgotten)
- `tier`: "active", "cache", or "archive"
- `focus_lens`: Tags that determine when it gets triggered based on perceptual priority

---

## 2. Focus Lens Configuration

Focus lenses adjust how Anchor1 perceives and prioritizes memory and external input. You can adjust the active lens using:

```python
session.focus = "Network"
```

### Recommended Lenses:
- `"Network"`
- `"Authentication"`
- `"User"`
- `"Behavior"`
- `"System"`
- `"Identity"`

These lenses interact with `focus_lens` values on memory containers to determine whether a memory "ripples" into the current state.

---

## 3. Using the Bridge (Always Required)

Anchor1's perception system is accessed through the bridge layer. You can simulate perception with:

```python
from bridge.bridge import bridge_input, get_anchor_state

# Simulate an event
bridge_input(session, "Unusual login from new IP address detected.")

# View Anchor1's internal state
get_anchor_state(session)
```

This works whether you're running a simulation, feeding syslog events, or connecting to a language model.

---

## 4. Connecting to GPT/LLMs (Optional)

If you're integrating Anchor1 with GPT or a language model, use `get_anchor_state()` to retrieve the current state and format it into a system prompt:

```python
state = get_anchor_state(session)

prompt = f"""
Anchor1 is in:
- Fear: {state['anchor_vector']['Fear']}
- Safety: {state['anchor_vector']['Safety']}
- Time: {state['anchor_vector']['Time']}
- Choice: {state['anchor_vector']['Choice']}
- Last Behavior: {state['last_behavior']}
"""
```

Feed this into your LLM as system context to create emotionally reactive agents.

---

## 5. Summary

- **Memory drives context**
- **Focus lens defines perception**
- **Bridge executes perception collapse**
- **LLMs can reflect Anchor1’s emotional drift**
- **Fear & Safety are universal anchors**
- **Lensing is where specialization occurs**

Anchor1 doesn’t script behavior. It collapses into it.

This is not automation. This is perception.
