function createTemplate(HTMLString) {
    const html = document.implementation.createHTMLDocument();
    html.body.innerHTML = HTMLString;
    return html.body.children[0];
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function insertElement(Selectorcontaner, HTMLString) {
    let container = document.querySelector(Selectorcontaner)
    if (container.children.length > 0) {
        container.children[0].remove();
        insertElement(Selectorcontaner, HTMLString)
    } else if (HTMLString) {
        element = createTemplate(HTMLString);
        container.append(element)
    }
}

function appendElement(Selectorcontaner, HTMLString) {
    let container = document.querySelector(Selectorcontaner)
    element = createTemplate(HTMLString);
    container.append(element)
}

function show_alert(success, msg) {
    const type = success ? 'success':'danger'
    const mtype = success ? 'Buen Trabajo. ':'Error. '
    const HTMLString = alertInfoHTML(msg, type, mtype)
    insertElement('#InfoMsg', HTMLString)
}