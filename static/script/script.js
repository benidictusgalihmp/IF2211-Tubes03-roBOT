var input = document.getElementById("message");
var form = document.getElementById("myForm");
var messageBox = document.getElementsByClassName("box").item(0);

input.addEventListener("keyup", addResponsesAfterKeypress);
form.addEventListener('submit', function(event) {
    event.preventDefault();
    var text = input.value
    // console.log(text);
    $.ajax({
        url: "/message",
        type: "get",
        data: {jsdata: text},
        success: function(response) {
            createMsgBubble("user", "");
            createMsgBubble("bot", response);
            input.value = "";
            messageBox.scrollTop = messageBox.scrollHeight;
        },
        error: function(xhr) {
          //Do Something to handle error
        }
    });
});


function addResponsesAfterKeypress(event) {
    if (inputLength() > 0 && (event.keycode === 13 || event.key === "Enter")) {
        event.preventDefault();
        form.dispatchEvent(new Event('submit'));
    }
}

function createMsgBubble(type, response) {
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
        var textContent = document.createTextNode(response);

        img.src = "static/images/robot.png"
        messageBubble.classList.add("bot");
    }

    text.appendChild(textContent);
    messageBubble.appendChild(img);
    messageBubble.appendChild(text);
    messageBox.appendChild(messageBubble);
}

function getResponse() {
    return getresponse;
}

function inputLength() {
    return input.value.length;
}