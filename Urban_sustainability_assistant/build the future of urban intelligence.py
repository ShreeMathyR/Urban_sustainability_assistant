import random
import hashlib
import time
from IPython.display import display, Markdown
import ipywidgets as widgets

# -----------------------------
# 1. AI Urban Sprawl Detection
# -----------------------------
def analyze_satellite_data():
    """Simulated AI analysis of satellite imagery for urban issues."""
    return {
        "issues": ["Informal Settlements", "Traffic Congestion", "Low Infrastructure Density"],
        "suggestions": ["Re-zone area A", "Add bus lanes to Zone B", "Upgrade drainage in Sector C"]
    }

# -----------------------------
# 2. IoT Sensor Data Simulation
# -----------------------------
def get_iot_data():
    """Simulated IoT sensor readings."""
    return {
        "Air Quality Index": random.randint(50, 150),
        "Noise Level (dB)": random.randint(40, 100),
        "Traffic Index": random.randint(60, 120)
    }

# -----------------------------
# 3. Blockchain-like Feedback System
# -----------------------------
blockchain = []

def create_block(data):
    block = {
        'timestamp': time.time(),
        'data': data,
        'previous_hash': blockchain[-1]['hash'] if blockchain else '0',
    }
    block['hash'] = hashlib.sha256(str(block).encode()).hexdigest()
    return block

def submit_feedback(feedback_text):
    """Stores feedback in a simulated blockchain."""
    block = create_block({"feedback": feedback_text})
    blockchain.append(block)
    return "Feedback securely stored in blockchain."

# -----------------------------
# 4. Interface Components
# -----------------------------
analyze_btn = widgets.Button(description="Run AI Analysis", button_style='info')
ai_output = widgets.Output()

feedback_area = widgets.Textarea(placeholder='Describe urban issues here...')
submit_btn = widgets.Button(description="Submit Feedback", button_style='success')
fb_output = widgets.Output()

iot_btn = widgets.Button(description="Fetch IoT Data", button_style='warning')
iot_output = widgets.Output()

# -----------------------------
# 5. Event Handlers
# -----------------------------
def on_analyze_clicked(b):
    ai_output.clear_output()
    result = analyze_satellite_data()
    with ai_output:
        display(Markdown(f"*Detected Issues:* {', '.join(result['issues'])}"))
        display(Markdown(f"*Planning Suggestions:* {', '.join(result['suggestions'])}"))

def on_submit_clicked(b):
    fb_output.clear_output()
    message = submit_feedback(feedback_area.value)
    with fb_output:
        display(Markdown(f"{message}"))

def on_iot_clicked(b):
    iot_output.clear_output()
    data = get_iot_data()
    with iot_output:
        for key, value in data.items():
            display(Markdown(f"{key}:** {value}"))

# Button Bindings
analyze_btn.on_click(on_analyze_clicked)
submit_btn.on_click(on_submit_clicked)
iot_btn.on_click(on_iot_clicked)

# -----------------------------
# 6. Layout and Display
# -----------------------------
display(Markdown("# Urban Sustainability Assistant – Phase 3 Demo"))

display(Markdown("## 1. AI Urban Sprawl Detection"))
display(analyze_btn, ai_output)

display(Markdown("## 2. Submit Civic Feedback"))
display(feedback_area, submit_btn, fb_output)

display(Markdown("## 3. IoT Sensor Data"))
display(iot_btn, iot_output)