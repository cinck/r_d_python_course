const cntnrDiv = document.createElement("div")
cntnrDiv.className = "container"

const bttnsDiv = document.createElement("div");
bttnsDiv.style.display = "flex"
bttnsDiv.className = "container cntnr-bttns"
bttnsDiv.idName = "buttons";
bttnsDiv.textAlign = "center";

const bttnSpacer1 = document.createElement("div");
bttnSpacer1.style.flex = "1 1 auto"
bttnsDiv.appendChild(bttnSpacer1);

// <HW28> Task 1: Add buttons
btnNames = ["Add friend", "Send message", "Offer a job"]
btnNames.map(buttonName => {
    let button = document.createElement("button");
    button.className = "btn btn-primary";
    button.innerText = buttonName;
    button.style.flex = "0 1 max-content"
    button.style.margin = "3px";
    bttnsDiv.appendChild(button);
})

let userInfo = document.getElementById("userInfo");
userInfo.appendChild(bttnsDiv);

const bttnsDiv2 = document.createElement("div")
bttnsDiv2.style.display = "flex"
bttnsDiv2.className = "container cntnr-bttns"
bttnsDiv2.id = "add-task"
bttnsDiv2.style.paddingLeft = "5px"

const bttnSpacer2 = document.createElement("div");
bttnSpacer2.style.flex = "1 1 auto"

// <HW28> Task 6. Pass task button
const passTaskBttn = document.createElement("button");
passTaskBttn.style.flex = "0 1 max-content"
passTaskBttn.className = "btn btn-success";
passTaskBttn.innerText = "Pass task";


bttnsDiv2.appendChild(bttnSpacer2)
bttnsDiv2.appendChild(passTaskBttn)
document.getElementById("studyProgress").appendChild(bttnsDiv2).appendChild(passTaskBttn);

// <HW28> Task 6. Button click adds new row to the table
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

// <HW28> Task 2. Display random friends quantity on page load
let frndsQty = Math.round(Math.random() * 200);
document.getElementById("frnds-qty").innerText = frndsQty.toString();


// <HW28> Task 3. "Add friend" button changes name and disables after clicking
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


// <HW28> Task 4. "Send message" button changes colours when clicked.
function changeColour(bttnColour) {
    if (bttnColour === "green") {return "pink"}
    else {return "green"}
}

const sendMessageBttn = document.getElementsByTagName("button")[1];
sendMessageBttn.style.backgroundColor = "green";

sendMessageBttn.addEventListener("click", (bttnClick) => {
    bttnClick.target.style.backgroundColor = changeColour(sendMessageBttn.style.backgroundColor);
});

// <HW28> Task 5. "Offer a job" button hides and shows "Add friend button" when clicked.
function addRemoveBttn() {
    if (addFriendBttn.hidden === true) {addFriendBttn.hidden = false}
    else {addFriendBttn.hidden = true}
}

const offerJobBttn = document.getElementsByTagName("button")[2];
offerJobBttn.onclick = (event) => {addRemoveBttn()};

