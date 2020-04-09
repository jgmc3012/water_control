$form = document.getElementById('measurer_update') 
console.log('AQUI ESTOY')
$form.addEventListener('submit', function (event) {
    event.preventDefault()
    const $house = document.getElementById('house_id')
    if (!$house) {
        show_alert(false, 'Debe rellenar el campo de "Identificación".')
    } else {
        const url = `${this.action}`.replace('12345',$house.value.trim())
        const data = getJsonFromForm("[api='water_control']")
        const method = 'PUT'
        sendData(data, url, method)
        .then( data =>  show_alert(true, `Medidor de la casa ${data.house} Actualizados.
        Hay una factura pendiente de por ${data.amount} por los cargos del servicio de agua.`))
    }
})