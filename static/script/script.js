// var button = document.getElementById("send");
var input = document.getElementById("message");
var form = document.getElementById("myForm");
var messageBox = document.getElementsByClassName("box").item(0);

input.addEventListener("keyup", addResponsesAfterKeypress);
form.addEventListener('submit', function(event) {
    event.preventDefault();
    const messageData = new FormData(form);
    fetch('/', {
        method: 'POST',
        body: messageData,
    }).then(function(response) {
        console.log("form");
        createMsgBubble("user");
        createMsgBubble("bot");
        input.value = "";
        messageBox.scrollTop = messageBox.scrollHeight;
    });
});

function addResponsesAfterKeypress(event) {
    if (inputLength() > 0 && (event.keycode === 13 || event.key === "Enter")) {
        event.preventDefault();
        form.dispatchEvent(new Event('submit'));
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

        img.src = "static/images/user.png";
        messageBubble.classList.add("user");
    } else if (type == "bot") {
        var textContent = document.createTextNode("placeholder");

        img.src = "static/images/robot.png"
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