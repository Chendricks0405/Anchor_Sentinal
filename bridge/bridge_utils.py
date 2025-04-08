def load_memory(file_path):
    """Loads memory containers from the given JSON file."""
    import json
    with open(file_path, 'r') as f:
        return json.load(f)

def initialize_anchor1_memory(session, memory_data):
    """Initializes Anchor1's memory orbit from the loaded memory containers."""
    session.memory = memory_data
