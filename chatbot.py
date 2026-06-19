from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Chatbot logic
def chatbot_response(message):
    msg = message.lower()

    if any(word in msg for word in ["hello", "hi", "hey"]):
        return "Hello. How can I help you today?"

    elif "time" in msg:
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}"

    elif "date" in msg:
        return f"Today's date is {datetime.now().strftime('%d-%m-%Y')}"

    elif "your name" in msg:
        return "I am a Flask-based voice chatbot."

    elif "how are you" in msg:
        return "I am functioning properly. How can I assist you?"

    elif "joke" in msg:
        return "Why do programmers prefer dark mode? Because light attracts bugs."

    elif "help" in msg:
        return "Ask about time, date, jokes, or greetings."

    elif "president of india" in msg:
        return "The current President of India is Droupadi Murmu."

    elif "world cup" in msg:
        return "The FIFA World Cup 2026 winner is not decided yet."

    elif "bye" in msg:
        return "Goodbye. Have a good day."

    else:
        return "I did not understand that. Try asking for help."


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get", methods=["POST"])
def get_bot_response():
    user_msg = request.json["message"]
    response = chatbot_response(user_msg)
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)