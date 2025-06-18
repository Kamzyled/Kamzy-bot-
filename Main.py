import os
from flask import Flask, request, jsonify
import openai

app = Flask(__kamzy__)

# Get OpenAI API key from Render secret
openai)

@app.route("/")
def home():
    return "Kamzy's Robot Assistant is Live!"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    message = data.get("message", "")

    if not message:
        return jsonify({"error": "No message provided."}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful robot assistant that behaves like a smart friend and explains things clearly."},
                {"role": "user", "content": message}
            ]
        )
        answer = response["choices"][0]["message"]["content"]
        return jsonify({"answer": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
