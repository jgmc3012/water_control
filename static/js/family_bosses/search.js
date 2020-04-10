const $formSearch = document.getElementById('form_search_client')
const $formDetail = document.getElementById('famile_boss')
const $btnDelete = document.getElementById('detail_delete')

const $containerSearch = document.getElementById('container_search')
const $containerForm = document.getElementById('container_famile_boss')
$formDetail.action += '12345/'


sendForm($formSearch, 'GET',data => {
    $containerForm.classList.add('d-none')
    return data['search_card_id']
}, data => {
    for (key in data) {
        $formDetail[key].value = data[key]
    }
    $formDetail.old_card_id.value = data.card_id
    show_alert(true,'Edite los datos del usuario y presione "Actualizar"')
    $containerForm.classList.remove('d-none')
    $containerSearch.classList.add('d-none')

})

sendForm($formDetail, 'PUT', data => data.old_card_id, res => {
    show_alert(true,`El usuario ${res.first_name} fue actualizado exitosamente`)
    $containerForm.classList.add('d-none')
    $containerSearch.classList.remove('d-none')
})


$btnDelete.addEventListener('click', event =>{

    const data = getJsonFromForm("[api='water_control']")
    const url = $formDetail.action.replace('12345', data['old_card_id'])
    sendData(data, url, 'DELETE')
    .then(response => {
        if (response.ok) {
            show_alert(response.ok,`El usuario fue eliminado exitosmente`)
        } else {
            show_alert(response.ok,`El usuario tiene facturas pendientes por pagar.`)
        }
        $containerForm.classList.add('d-none')
        $containerSearch.classList.remove('d-none')
    })
})