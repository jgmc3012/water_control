$formList = document.getElementById('formListInvoice')

$formList.addEventListener('submit', function (event) {
    event.preventDefault()
    const Data = getJsonFromForm("[api='water_control']")
    const method = 'GET'
    let url = this.action.replace('12345', Data['year'])
    if (Data['month']!='0') {
        url = `${url}month/${Data['month']}/`
        if (Data['day']!='0') {
            url = `${url}day/${Data['day']}/`
        }
    }
    sendData(Data, url, method)
    .then( data => {
        const date = formatDate(Data['year'], Data['month'], Data['day'])
        const HTMLString = snippetDetailList(date, data)
        insertElement('#invoice_list', HTMLString)
    })
})