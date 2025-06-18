from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample memory
robot_memory = {}

@app.route('/')
def home():
    return "Kamzy Bot is online!"

@app.route('/speak', methods=['POST'])
def speak():
    data = request.json
    message = data.get('message', '')
    return jsonify({"reply": f"Kamzy says: {message}"})

@app.route('/remember', methods=['POST'])
def remember():
    data = request.json
    key = data.get('key', '')
    value = data.get('value', '')
    if key and value:
        robot_memory[key] = value
        return jsonify({"status": "saved"})
    return jsonify({"error": "Missing key or value"}), 400

@app.route('/recall/<key>')
def recall(key):
    value = robot_memory.get(key, "I don't remember that.")
    return jsonify({"value": value})
