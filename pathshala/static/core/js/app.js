let currentRecipient = '';
let chatInput = $('#chat-input');
let chatButton = $('#btn-send');
let userList = $('#user-list');
let messageList = $('#messages');

function updateUserList() {
    $.getJSON('api/v1/user/', function (data) {
        userList.children('.user').remove();
        for (let i = 0; i < data.length; i++) {
            const userItem = `<a class="list-group-item user">${data[i]['username']}</a>`;
            $(userItem).appendTo('#user-list');
        }
        $('.user').click(function () {
            userList.children('.active').removeClass('active');
            let selected = event.target;
            $(selected).addClass('active');
            setCurrentRecipient(selected.text);
        });
    });
        
}
 
function drawMessage(message) {
    let position = 'left';
    const date = new Date(message.timestamp);
    //const date = new Date(message['date']);
    const monthNames = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"];
    let dd = date.getDate();
    let mm = monthNames[date.getMonth()];
    let yyyy = date.getFullYear();
    let tt = date.toLocaleTimeString();
    const datu = mm + " " +dd + "," + yyyy+', '+tt ;
    
    if (message.user === currentUser) position = 'right';
    const messageItem = `
            <li class="message ${position}">
                <div class="avatar">${message.user}</div>
                    <div class="text_wrapper">
                        <div class="text">${message.body}<br>
                            <span style="font-size:12px;" class="small">${datu}</span>
                    </div>
                </div>
            </li>`;
    $(messageItem).appendTo('#messages');
}
/*function drawMessage(message) {
    let position = 'left';
    const date = new Date(message.timestamp);
    const monthNames = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"];
    let dd = date.getDate();
    let mm = monthNames[date.getMonth()];
    let yyyy = date.getFullYear();
    let tt = date.toLocaleTimeString();
    tt = tt.replace(/:\d+ /, ' ');
    const datu = mm + " " +dd + "," + yyyy+', '+tt ;

    if (message.user === currentUser) position = 'right';
    const messageItem = `
            <li class="message ${position}">
                <div class="avatar">${message.user}</div>
                    <div class="text_wrapper">
                        <div class="text">${message.body}<br>
                            <span style="font-size:12px;" class="small">${datu}</span>
                    </div>
                </div>
            </li>`;
    $(messageItem).appendTo('#messages');
}*/

function getConversation(recipient) {
    $.getJSON(`api/v1/message/?target=${recipient}`, function (data) {
        messageList.children('.message').remove();
        for (let i = data['results'].length - 1; i >= 0; i--) {
            drawMessage(data['results'][i]);
        }
        messageList.animate({scrollTop: messageList.prop('scrollHeight')});
    });

}

function getMessageById(message) {
    console.log('------------')
    id = JSON.parse(message).message
    $.getJSON(`api/v1/message/${id}/`, function (data) {
        if (data.user === currentRecipient ||
            (data.recipient === currentRecipient && data.user == currentUser)) {
            drawMessage(data);
        }
        messageList.animate({scrollTop: messageList.prop('scrollHeight')});
    });
}

function sendMessage(recipient, body) {
    $.post('api/v1/message/', {
        recipient: recipient,
        body: body
        
    }).fail(function () {
        alert('Error! Check console!');
    });
}

function setCurrentRecipient(username) {
    currentRecipient = username;
    getConversation(currentRecipient);
    enableInput();
}


function enableInput() {
    chatInput.prop('disabled', false);
    chatButton.prop('disabled', false);
    chatInput.focus();
}

function disableInput() {
    chatInput.prop('disabled', true);
    chatButton.prop('disabled', true);
}

$(document).ready(function () {
    updateUserList();
    disableInput();

let socket = new WebSocket(`ws://127.0.0.1:8000/?session_key=${sessionKey}`);
    var socket = new WebSocket(
        'ws://' + window.location.host +
        '/ws?session_key=${sessionKey}')
    
    //console.log(socket.onmessage)
    chatInput.keypress(function (e) {
        if (e.keyCode == 13)
            chatButton.click();
    });

    chatButton.click(function () {
        if (chatInput.val().length > 0) {  
            sendMessage(currentRecipient, chatInput.val());
            chatInput.val('');
        }
    });
    socket.onmessage = function (e) {
        console.log(e.data)
        getMessageById(e.data);
    };
});



