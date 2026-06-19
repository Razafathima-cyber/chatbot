
// Send message to Flask
function sendMessage() {
    let input = document.getElementById("user-input");
    let message = input.value;

    if (!message) return;

    addMessage("You: " + message, "user");

    fetch("/get", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    })
    .then(res => res.json())
    .then(data => {
        addMessage("Bot: " + data.response, "bot");
        speak(data.response);
    });

    input.value = "";
}

// Add message to chat
function addMessage(text, sender) {
    let chatBox = document.getElementById("chat-box");

    let div = document.createElement("div");
    div.className = sender;
    div.innerHTML = text;

    chatBox.appendChild(div);
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Text-to-speech
function speak(text) {
    let speech = new SpeechSynthesisUtterance(text);
    speech.lang = "en-US";
    window.speechSynthesis.speak(speech);
}

// Voice input (Speech-to-Text)
function startVoice() {
    let recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();

    recognition.lang = "en-US";

    recognition.start();

    recognition.onresult = function(event) {
        let voiceText = event.results[0][0].transcript;
        document.getElementById("user-input").value = voiceText;
        sendMessage();
    };
}