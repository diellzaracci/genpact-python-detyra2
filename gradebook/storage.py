import json
import os
import logging

#spari mu siguru qe follderat ekzistojne
os.makedirs("data", exist_ok=True)
os.makedirs("logs", exist_ok=True)

DATA_PATH = "data/gradebook.json"

#Konfigurimi i llogave
logging.basicConfig( 
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_data():
    if not os.path.exists(DATA_PATH):
        return {"students": [], "courses": [], "enrollments": []}

    try:
        with open(DATA_PATH, "r") as f:
            content = f.read()
            data = json.loads(content)
            return data
        
    except json.JSONDecodeError as e:
        print("JSONDecodeError:", e)
        return {"students": [], "courses": [], "enrollments": []}
    
def save_data(data):
    """Save data to JSON file."""
    try:
        with open(DATA_PATH, "w") as f:
            json.dump(data, f, indent=4)

        logging.info("Data saved successfully.")

    except Exception as e:
        logging.error(f"Error saving data: {e}")
        print("Failed to save data.")