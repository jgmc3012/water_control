$form = document.getElementById('form_house')

$form.addEventListener('submit', function (event) {
    event.preventDefault()

    const url = `${this.action}`
    const data = getJsonFromForm("[api='water_control']")
    const method = 'POST'
    sendData(data, url, 'POST')
    .then( data =>  show_alert(true, `Casa ${data.house_id} registrada con exito`) )
})