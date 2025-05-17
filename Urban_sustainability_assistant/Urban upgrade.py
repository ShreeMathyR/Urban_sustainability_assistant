import random
import hashlib
import datetime

# 1. Simulated AI Model Detection
def detect_urban_issues():
    issues = ["Slum Area", "Traffic Congestion", "Flood-Prone Zone"]
    actions = ["Restructure Area", "Build Flyover", "Drainage Upgrade"]
    results = random.sample(list(zip(issues, actions)), 2)
    
    print("\n--- AI Model Output ---")
    for issue, action in results:
        print(f"Issue Detected: {issue} → Action: {action}")

# 2. Simulated IoT Data Integration
def get_iot_data():
    data = {
        "Air Quality Index": random.randint(50, 200),
        "Noise Level (dB)": random.randint(60, 100),
        "Traffic Status": random.choice(["Low", "Moderate", "High"])
    }

    print("\n--- Real-Time IoT Data ---")
    for key, value in data.items():
        print(f"{key}: {value}")

# 3. Blockchain-like Civic Feedback Logger
blockchain_log = []

def add_feedback(feedback):
    timestamp = str(datetime.datetime.now())
    data_string = feedback + timestamp
    block_hash = hashlib.sha256(data_string.encode()).hexdigest()
    block = {
        "timestamp": timestamp,
        "feedback": feedback,
        "hash": block_hash
    }
    blockchain_log.append(block)
    print("\nFeedback stored securely in blockchain log.")

def show_blockchain_log():
    print("\n--- Blockchain Feedback Ledger ---")
    for block in blockchain_log:
        print(f"[{block['timestamp']}] {block['feedback']} | Hash: {block['hash']}")

# --- MAIN PROGRAM FLOW ---
if _name_ == "_main_":
    print("Urban Sustainability Assistant – Phase 4\n")

    detect_urban_issues()
    get_iot_data()

    # User Feedback Section
    user_input = input("\nEnter your feedback or concern: ")
    if user_input:
        add_feedback(user_input)

    # View the blockchain log
    show_log = input("\nDo you want to see the feedback ledger? (yes/no): ").lower()
    if show_log == "yes":
        show_blockchain_log()