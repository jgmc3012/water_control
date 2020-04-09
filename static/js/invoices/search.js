$form = document.getElementById('searchInvoices')

$form.addEventListener('submit', function (event) {
    event.preventDefault()
    const $card_id = document.getElementById('card_id')
    const url = `${this.action}`.replace('12345', $card_id.value.trim())
    const method = 'GET'
    sendData({}, url, method)
    .then( data => {
        if (data.length > 0) {
            HTMLString = SnippetListInvoices(data)
            insertElement('#invoice_list', HTMLString)
        } else {
            show_alert(true, `El cliente con id ${data.house_id} no tiene facturas pendientes`) 
        }
    })
})