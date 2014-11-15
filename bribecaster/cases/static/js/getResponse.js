var textResponses = ['Everything went well. Thank you for your text.', 'I had to pay a large bribe to attain service.', 
        'The officer said I lacked the proper paperwork. He asked me to return at a later time.', 'There was no one available to help me with my matter', 
        'I paid a bribe to get a form processed.'];

var roboReponses = ['Picked Up Call', 'Refused Call', 'Missed Call', 'Wrong Number', 'Number Does Not Exist'];

var followupResponses = ['Negative Sentiment', 'Positive Sentiment', 'Neutral Sentiment', 'Extremely Negative Sentiment', 'Extremely Positive Sentiment'];

function replyText(dom) { 
    var index = Math.floor((Math.random() * textResponses.length));
    var response = textResponses[index];
    var para = document.createElement("p");
    var node = document.createTextNode(response);
    para.appendChild(node);
    var child = document.getElementById(dom);
    child.parentNode.replaceChild(para, child);
}

function replyRobo(dom) { 
    var index = Math.floor((Math.random() * roboReponses.length));
    var response = roboReponses[index];
    var para = document.createElement("p");
    var node = document.createTextNode(response);
    para.appendChild(node);
    var child = document.getElementById(dom);
    child.parentNode.replaceChild(para, child);
}

function replyFollowup(dom) { 
    var index = Math.floor((Math.random() * followupResponses.length));
    var response = followupResponses[index];
    var para = document.createElement("p");
    var node = document.createTextNode(response);
    para.appendChild(node);
    var child = document.getElementById(dom);
    child.parentNode.replaceChild(para, child);
}