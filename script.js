var button = document.getElementById("send");
var input = document.getElementById("message");
var messageBox = document.getElementsByClassName("box").item(0);
var userBubbleTemplate = document.getElementsByClassName("user").item(0);
var botBubbleTemplate = document.getElementsByClassName("bot").item(0);

button.addEventListener("click", addResponsesAfterSend);
input.addEventListener("keyup", addResponsesAfterKeypress);

function addResponsesAfterSend(event) {
    if (inputLength() > 0) {
        createMsgBubble("user");
        createMsgBubble("bot");
        input.value = "";
        messageBox.scrollTop = messageBox.scrollHeight;
    }
}

function addResponsesAfterKeypress(event) {
    if (inputLength() > 0 && (event.keycode === 13 || event.key === "Enter")) {
        createMsgBubble("user");
        createMsgBubble("bot");
        input.value = "";
        messageBox.scrollTop = messageBox.scrollHeight;
    }
}

function createMsgBubble(type) {
    var messageBubble = document.createElement("div");
    var img = document.createElement("img");
    var text = document.createElement("p");
    text.classList.add("text");
    messageBubble.classList.add("bubble");

    if (type == "user") {
        var textContent = document.createTextNode(input.value);

        img.src = "image/user.png";
        messageBubble.classList.add("user");
    } else if (type == "bot") {
        var textContent = document.createTextNode("placeholder");

        img.src = "image/robot.png";
        messageBubble.classList.add("bot");
    }

    text.appendChild(textContent);
    messageBubble.appendChild(img);
    messageBubble.appendChild(text);
    messageBox.appendChild(messageBubble);
}

function inputLength() {
    return input.value.length;
}