$form = document.getElementById('famile_boss') 

$form.addEventListener('submit', function (event) {
    event.preventDefault()

    const url = `${this.action}`
    const data = getJsonFromForm("[api='water_control']")
    const method = 'POST'
    sendData(data, url, 'POST')
    .then( client =>  show_alert(true, `${client.first_name} ${client.last_name} registrado con exito`) )
})