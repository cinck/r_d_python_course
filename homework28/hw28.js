const cntnrDiv = document.createElement("div")
cntnrDiv.className = "container"

const bttnsDiv = document.createElement("div");
bttnsDiv.className = "container cntnr-bttns"
bttnsDiv.idName = "buttons";
bttnsDiv.textAlign = "center";

btnNames = ["Add friend", "Send message", "Offer a job"]
btnNames.map(buttonName => {
    let button = document.createElement("button");
    button.className = "btn btn-primary";
    button.innerText = buttonName;
    button.style.margin = "3px";
    bttnsDiv.appendChild(button);
})

let userInfo = document.getElementById("userInfo");
userInfo.appendChild(bttnsDiv);

const passTaskBttn = document.createElement("button");
passTaskBttn.className = "btn btn-success";
passTaskBttn.innerText = "Pass task";

const bttnsDiv2 = document.createElement("div")
bttnsDiv2.className = "container cntnr-bttns"
bttnsDiv2.id = "add-task"
bttnsDiv2.style.paddingLeft = "5px"
bttnsDiv2.appendChild(passTaskBttn)
document.getElementById("studyProgress").appendChild(bttnsDiv2).appendChild(passTaskBttn);

function addRow() {
    newRow = document.createElement("tr");
    newRow.appendChild(document.createElement("td")).innerText = Math.round(Math.random() * 100).toString();
    newRow.appendChild(document.createElement("td")).innerText = "Task name";
    newRow.appendChild(document.createElement("td")).innerText = "10/10"
    document.getElementById("homeworks").appendChild(newRow);
}

passTaskBttn.onclick = (event) => {
    addRow()
}

let frndsQty = Math.round(Math.random() * 200);
document.getElementById("frnds-qty").innerText = frndsQty.toString();

const addFriendBttn = document.getElementsByTagName("button")[0];
addFriendBttn.addEventListener("click", (buttonClickEvent) => {
    buttonClickEvent.target.style.backgroundColor = "grey";
    buttonClickEvent.target.innerText = "Waiting confirmation";
    buttonClickEvent.target.disabled = true;
});

addFriendBttn.onclick = (event) => {
    fQty = Number(document.getElementById("frnds-qty").innerText) + 1;
    document.getElementById("frnds-qty").innerText = fQty;
};

function changeColour(bttnColour) {
    if (bttnColour === "green") {return "pink"}
    else {return "green"}
}

const sendMessageBttn = document.getElementsByTagName("button")[1];
sendMessageBttn.style.backgroundColor = "green";

sendMessageBttn.addEventListener("click", (bttnClick) => {
    bttnClick.target.style.backgroundColor = changeColour(sendMessageBttn.style.backgroundColor);
});

function addRemoveBttn() {
    if (addFriendBttn.hidden === true) {addFriendBttn.hidden = false}
    else {addFriendBttn.hidden = true}
}

const offerJobBttn = document.getElementsByTagName("button")[2];
offerJobBttn.onclick = (event) => {addRemoveBttn()};

