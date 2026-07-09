//  VOICE OUTPUT 

function speak(text) {

    window.speechSynthesis.cancel();

    const speech = new SpeechSynthesisUtterance(text); //convert text to speech

    speech.lang = "en-GB";
    speech.rate = 1.5;
    speech.pitch = 1;
    speech.volume = 1;

    window.speechSynthesis.speak(speech); //speak
}


// SEND MESSAGE 

async function sendMessage() {

    const input = document.getElementById("user-input");
    const message = input.value.trim();

    if (message === "") {
        return;
    }

    const chatBox = document.getElementById("chat-box");

    // User message
    chatBox.innerHTML += `
        <div class="user">
            <div class="user-message">
                ${message}
            </div>
        </div>
    `;

    input.value = "";

    chatBox.scrollTop = chatBox.scrollHeight;

    // Typing animation
    chatBox.innerHTML += `
        <div class="bot" id="typing">
            <div class="bot-message">
                Responding...
            </div>
        </div>
    `;

    chatBox.scrollTop = chatBox.scrollHeight;

    try {

        const response = await fetch("/get_response", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message
            })
        });

        const data = await response.json();

        const typingDiv = document.getElementById("typing");

        if (typingDiv) {
            typingDiv.remove();
        }

        // Bot response
        chatBox.innerHTML += `
            <div class="bot">
                <div class="bot-message">
                    ${data.response}
                </div>
            </div>
        `;

        // Voice output
        speak(data.response);

        chatBox.scrollTop = chatBox.scrollHeight;

    }

    catch (error) {

        const typingDiv = document.getElementById("typing");

        if (typingDiv) {
            typingDiv.remove();
        }

        chatBox.innerHTML += `
            <div class="bot">
                <div class="bot-message">
                     Unable to connect to chatbot backend.
                </div>
            </div>
        `;

        console.error(error);
    }
}


//  ENTER KEY 

document.getElementById("user-input")
.addEventListener("keypress", function(event) {

    if (event.key === "Enter") {
        sendMessage();
    }

});


//VOICE INPUT

const SpeechRecognition =
    window.SpeechRecognition ||
    window.webkitSpeechRecognition;

if (SpeechRecognition) {

    const recognition = new SpeechRecognition();

    recognition.lang = "en-US";
    recognition.continuous = false;
    recognition.interimResults = false;

    const micButton = document.getElementById("mic-btn");

    micButton.addEventListener("click", () => {

        micButton.innerHTML = "🎙️ Listening...";

        recognition.start();
    });

    recognition.onresult = function(event) {

        const transcript =
            event.results[0][0].transcript;

        document.getElementById(
            "user-input"
        ).value = transcript;

        micButton.innerHTML = "🎙️";

        sendMessage();
    };

    recognition.onerror = function(event) {

        console.error(
            "Speech Recognition Error:",
            event.error
        );

        micButton.innerHTML = "🎙️";
    };

    recognition.onend = function() {
        micButton.innerHTML = "🎙️";
    };

}


// SIDEBAR MENU 

const menuBtn =
    document.getElementById("menu-btn");

const sidebar =
    document.getElementById("sidebar");

menuBtn.addEventListener("click", function() {

    sidebar.classList.toggle("active");

});


// NEW CHAT

document.getElementById("new-chat-btn")
.addEventListener("click", function() {

    document.getElementById(
        "chat-box"
    ).innerHTML = "";

    window.speechSynthesis.cancel();

});

// ==============================
// CHAT HISTORY
// ==============================

document.getElementById("history-btn").addEventListener("click", async function () {

    const historyList = document.getElementById("history-list");

    historyList.innerHTML = "<h3>Recent Chats</h3>";

    try {

        const response = await fetch("/history");
        const history = await response.json();

        if (history.length === 0) {

            historyList.innerHTML += `
                <p>No chat history found.</p>
            `;

            return;
        }

        // Show latest first
        history.reverse().forEach(item => {

            historyList.innerHTML += `
                <div class="history-item">
                    <strong>${item.query}</strong><br>
                    <small>${item.time}</small>
                </div>
            `;

        });

    }

    catch (error) {

        console.error(error);

        historyList.innerHTML += `
            <p>Unable to load history.</p>
        `;

    }

});