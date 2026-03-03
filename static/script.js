function toggleMode() {
    document.body.classList.toggle("dark");
}

async function sendMessage() {

    const input = document.getElementById("userInput");
    const chatBox = document.getElementById("chatBox");

    const message = input.value;

    chatBox.innerHTML += `<div class="text-right mb-2"><b>You:</b> ${message}</div>`;
    input.value = "";

    // Typing animation
    const typingDiv = document.createElement("div");
    typingDiv.innerHTML = "<i>Agent is typing...</i>";
    chatBox.appendChild(typingDiv);

    const response = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message })
    });

    const data = await response.json();

    typingDiv.remove();

    chatBox.innerHTML += `
<div class="flex justify-start mb-2">
  <div class="bg-gray-700 text-white p-2 rounded-xl max-w-xs">
    ${data.response}
    <div class="text-xs mt-1 opacity-70">
      Persona: ${data.persona} | Confidence: ${data.confidence}
    </div>
  </div>
</div>
`;

    chatBox.scrollTop = chatBox.scrollHeight;
}