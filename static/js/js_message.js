// setup chat scoket
const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/chat/public_room/'
);

// on socket open
chatSocket.onopen = function (e) {
    console.log('Chat socket successfully connected.');
};

// on socket close
chatSocket.onclose = function (e) {
    console.log('Chat socket closed unexpectedly');
};

// on receiving message on group
chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    const message = data.message;
    
    setMessage(message);
};

// sending the text message to server
document.querySelector('#addMessage').onclick = function(e) {
        const messageInputDom = document.querySelector('#textMessage');
        const message = messageInputDom.value;

        chatSocket.send(JSON.stringify({
            'message': message
        }));
        
        messageInputDom.value = '';
};

// helper func setting message
function setMessage(message){
    var div = document.createElement('div');
    div.className = 'alert alert-success alert-dismissible fade show';
    div.setAttribute('role', 'alert');

    var message = document.createTextNode(message);
    div.appendChild(message);
     
    var closeButton = document.createElement('button');
    closeButton.type = 'button';
    closeButton.className = 'btn-close';
    closeButton.setAttribute('data-bs-dismiss', 'alert');
    closeButton.setAttribute('aria-label', 'Close');
    div.appendChild(closeButton);

    var container = document.getElementById('messages');  
    container.appendChild(div);
}