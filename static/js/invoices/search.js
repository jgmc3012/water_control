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
            addEventListenerToFormPay(data[0].client)
        } else {
            show_alert(true, `El cliente con no tiene facturas pendientes`) 
        }
    })
})

const addEventListenerToFormPay = card_id => {
    const $formPay = document.getElementById('payInvoices')
    $formPay.addEventListener('submit', function(event) {
        event.preventDefault()
        const url = `${this.action}`.replace('12345', card_id)
        const method = 'PUT'
        const data = getJsonFromForm("[api='water_control']")
        sendData(data, url, method)
        .then( data =>{
            if (data.ok) {
               show_alert(true, `Se pagaron todas las facturas del cliente exitosamente. Debe retornarle al cliente la cantidad de $${data.change} sobrantes de su cuenta saldada.`)
               insertElement('#invoice_list', '')
            } else {
                insertElement('#InfoMsg', alertInfoHTML(`Se procesaron ${data.number_of_payments} facturas exitosamente. Debe retornarle al cliente un total de $${data.change}, dado a que este no fue sufuciente para continuar pagando sus facturas pendientes. \n\nMas abajo se listan las facturas pendientes.`, 'warning', 'Importante: '))
                HTMLString = SnippetListInvoices(data.unpaid_invoices)
                insertElement('#invoice_list', HTMLString)
                addEventListenerToFormPay(data.unpaid_invoices[0].client)
            }
            if (data.number_of_payments > 0) {
                appendElement('#InfoMsg', alertInfoHTML(`Se le enviara al cliente por correo un resumen con de las facturas pagadas.`, 'success', 'En proceso: '))
            }
        })
    })
}