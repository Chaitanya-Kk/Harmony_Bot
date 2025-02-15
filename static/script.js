document.addEventListener("DOMContentLoaded", () => {
    const userInput = document.getElementById("user-input");
    const sendButton = document.getElementById("send-button");
    const chatBox = document.getElementById("chat-box");
    const suggestionsBox = document.getElementById("suggestions");

    function addMessage(message, sender) {
        const messageDiv = document.createElement("div");
        messageDiv.classList.add("message", sender);
        messageDiv.textContent = message;
        chatBox.appendChild(messageDiv);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    function sendMessage() {
        const message = userInput.value.trim();
        if (!message) return;

        addMessage(message, "user");
        userInput.value = "";
        suggestionsBox.innerHTML = ""; // Clear suggestions when message is sent
        suggestionsBox.style.display = "none";

        fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message }),
        })
            .then((response) => response.json())
            .then((data) => {
                addMessage(data.response, "bot");
            })
            .catch((error) => {
                console.error("Error:", error);
                addMessage("Something went wrong. Please try again.", "bot");
            });
    }

    sendButton.addEventListener("click", sendMessage);
    userInput.addEventListener("keypress", (e) => {
        if (e.key === "Enter") sendMessage();
    });

    // **Real-time autocomplete**
    userInput.addEventListener("input", function() {
        let query = this.value.trim();
        if (query.length > 1) {  // Fetch only if at least 2 characters are typed
            fetch(`/autocomplete?query=${query}`)
                .then(response => response.json())
                .then(data => showSuggestions(data.matches));
        } else {
            suggestionsBox.innerHTML = "";
            suggestionsBox.style.display = "none";
        }
    });

    function showSuggestions(matches) {
        suggestionsBox.innerHTML = ""; // Clear previous suggestions
        if (matches.length === 0) {
            suggestionsBox.style.display = "none"; // Hide if no suggestions
            return;
        }

        matches.forEach(match => {
            let item = document.createElement("li");
            item.textContent = match;
            item.onclick = () => {
                userInput.value = match;  // Fill input with selected suggestion
                suggestionsBox.innerHTML = "";
                suggestionsBox.style.display = "none"; // Hide suggestions after selection
            };
            suggestionsBox.appendChild(item);
        });

        suggestionsBox.style.display = "block"; // Show dropdown
    }

    // Hide suggestions when clicking outside input box
    document.addEventListener("click", function(event) {
        if (!userInput.contains(event.target) && !suggestionsBox.contains(event.target)) {
            suggestionsBox.style.display = "none";
        }
    });
});
